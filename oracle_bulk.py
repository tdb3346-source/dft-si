"""
ORACLE: GPAW bulk modulus via Birch-Murnaghan EOS  -  Fe, Si, C
================================================================
WHY: the MACE run gave Fe -58%, Si -24%, C +1% vs EXPERIMENT. Two explanations
with opposite consequences:
   (a) MACE genuinely fails on curvature (2nd-derivative) -> real finding
   (b) the EOS protocol in pipeline.py is bad            -> my bug, finding evaporates
Experiment can't separate these, because experimental B0 differs from PBE B0 for
real physical reasons (finite T, zero-point, xc error). Only running the SAME
protocol through the oracle separates protocol-error from model-error.

PROTOCOL MATCHING (this is the whole point - do not "improve" it):
  - relax cell+positions FIRST with the code's own calculator (each code sits at
    its own minimum; comparing curvature at different volumes is a confound)
  - then 5 isotropic volume points at scale = 0.94,0.97,1.00,1.03,1.06 (^1/3 on cell)
  - fit birchmurnaghan, report B in GPa
  - IDENTICAL strains + identical fit to pipeline.py's bulk_modulus_descriptor

TRAPS HANDLED:
  - Fe is FERROMAGNETIC. Non-spin-polarized PBE gets bcc Fe badly wrong and would
    produce a FAKE agreement with MACE, hiding a real failure. spinpol=True.
  - C (diamond) needs a harder cutoff than metals.
  - Unconverged relaxation -> return None. Never report a number from a run that
    did not converge (standing discipline: refuse technical wins).

ENV: `dft` (GPAW). NOT `mace`.
RUNTIME: this is a BATCH job. Fe with spin polarization is the slow one.
         Do not sit through it serially. Start it, walk away, read the log after.

USAGE:
    conda activate dft
    python oracle_bulk.py            # all three
    python oracle_bulk.py Fe         # just one
"""

import sys
import json
import numpy as np

try:
    from gpaw import GPAW, PW
except ImportError:
    sys.exit(
        "\n*** WRONG ENV ***\n"
        "GPAW not found. Run:  conda activate dft\n"
        "(MACE lives in `mace`, GPAW in `dft`. This split has cost two sessions.)\n"
    )

from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState

# Same strain ladder as pipeline.py. Do not change without changing both.
SCALES = (0.94, 0.97, 1.00, 1.03, 1.06)

SYSTEMS = {
    # name: (symbol, structure, exp lattice const, PW cutoff eV, kpts, spinpol, magmom)
    "Fe": dict(sym="Fe", struct="bcc",     a=2.867, ecut=600, kpts=(8, 8, 8),
               spinpol=True,  magmom=2.2,
               note="ferromagnetic - spinpol REQUIRED or B0 is nonsense"),
    "Si": dict(sym="Si", struct="diamond", a=5.431, ecut=500, kpts=(6, 6, 6),
               spinpol=False, magmom=0.0,
               note="the -24% case; well-behaved semiconductor"),
    "C":  dict(sym="C",  struct="diamond", a=3.567, ecut=800, kpts=(6, 6, 6),
               spinpol=False, magmom=0.0,
               note="MACE's BEST case (+1%) - the control. If GPAW disagrees "
                    "HERE, the protocol itself is broken."),
}


def make_calc(cfg, label):
    kw = dict(mode=PW(cfg["ecut"]), xc="PBE", kpts=cfg["kpts"],
              txt=f"gpaw_eos_{label}.txt", symmetry={"point_group": False})
    if cfg["spinpol"]:
        kw["spinpol"] = True
    return GPAW(**kw)


def gpaw_bulk_modulus(name):
    cfg = SYSTEMS[name]
    print(f"\n{'=' * 68}\nORACLE: {name}   ({cfg['note']})\n{'=' * 68}")

    at0 = bulk(cfg["sym"], cfg["struct"], a=cfg["a"], cubic=True)
    if cfg["spinpol"]:
        at0.set_initial_magnetic_moments([cfg["magmom"]] * len(at0))

    # --- step 1: relax to GPAW's OWN minimum (protocol match) ---
    at0.calc = make_calc(cfg, f"{name}_relax")
    opt = BFGS(FrechetCellFilter(at0), logfile=f"gpaw_eos_{name}_relax.log")
    conv = opt.run(fmax=0.02, steps=60)
    if not conv:
        print(f"  [{name}] relaxation UNCONVERGED -> refusing to report B0.")
        return None
    a_relaxed = float(at0.get_volume() ** (1 / 3))
    print(f"  relaxed a = {a_relaxed:.4f} A  (exp {cfg['a']:.3f})")

    # --- step 2: EOS points, identical strains to the MACE run ---
    vols, enes = [], []
    for sc in SCALES:
        at = at0.copy()
        at.set_cell(at0.get_cell() * sc ** (1 / 3), scale_atoms=True)
        if cfg["spinpol"]:
            at.set_initial_magnetic_moments([cfg["magmom"]] * len(at))
        at.calc = make_calc(cfg, f"{name}_{sc}")
        e = float(at.get_potential_energy())
        vols.append(at.get_volume())
        enes.append(e)
        print(f"    scale {sc:.2f}  V={vols[-1]:8.3f} A^3  E={e:10.4f} eV")

    # --- step 3: same fit ---
    eos = EquationOfState(vols, enes, eos="birchmurnaghan")
    v0, e0, B = eos.fit()
    B_gpa = float(B * 160.2176634)          # eV/A^3 -> GPa
    print(f"  --> B0(GPAW) = {B_gpa:.1f} GPa    (V0 = {v0:.3f} A^3)")
    return dict(B_gpa=round(B_gpa, 1), a_relaxed=round(a_relaxed, 4),
                v0=round(float(v0), 3))


if __name__ == "__main__":
    targets = sys.argv[1:] or ["C", "Si", "Fe"]      # cheap -> expensive
    out = {}
    for t in targets:
        if t not in SYSTEMS:
            print(f"skip unknown {t}")
            continue
        try:
            out[t] = gpaw_bulk_modulus(t)
        except Exception as e:
            print(f"  [{t}] RAISED {type(e).__name__}: {e}")
            out[t] = None

    with open("oracle_bulk.json", "w") as fh:
        json.dump(out, fh, indent=2)

    # --- the adjudication table ---
    mace = {"C": 446.2, "Si": 74.5, "Fe": 71.8}
    expt = {"C": 443.0, "Si": 98.0, "Fe": 170.0}
    print(f"\n\n{'=' * 68}\nADJUDICATION: is the derivative-order finding real?\n{'=' * 68}")
    print(f"{'sys':5s} {'MACE':>8s} {'GPAW':>8s} {'expt':>8s}   {'MACE vs GPAW':>13s}")
    for t in targets:
        if out.get(t):
            g = out[t]["B_gpa"]
            err = (mace[t] - g) / g * 100
            print(f"{t:5s} {mace[t]:8.1f} {g:8.1f} {expt[t]:8.1f}   {err:+12.1f}%")
    print("\nREAD IT THIS WAY:")
    print("  MACE ~= GPAW everywhere      -> protocol was fine, MACE fine, "
          "'finding' was just PBE-vs-experiment. Finding DIES.")
    print("  MACE far off GPAW on Fe/Si but close on C -> MACE genuinely fails "
          "curvature, material-dependently. Finding SURVIVES.")
    print("  GPAW far off EXPERIMENT on C too -> the PROTOCOL is broken "
          "(5 points too coarse / strain range wrong). My bug. Finding DIES.")
