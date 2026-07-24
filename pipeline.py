"""
P5 ON-RAMP PIPELINE  -  the first end-to-end run of the verifier as a SYSTEM.
=============================================================================
Structure Gate (Tool 3) -> Descriptor Checker (Tool 1) -> Model-Fidelity (Tool 2) -> verdict

WHY THIS FILE EXISTS
--------------------
Audit finding (Jul 23): descriptor_checker.py was a SKELETON. Check 0 and the
oracle check were STUBS, and the two test descriptors returned hardcoded numbers.
The engine routed correctly, but no descriptor had ever been scored by MACE and
no oracle had ever run. Running a trust-map on that would have been confident
garbage at scale.

This file supplies the three missing connectors:
  1. REAL descriptors that call MACE (lattice constant, cohesive energy, bulk modulus)
  2. Check 0 delegated to structure_gate.gate() - a real instrument, not a stub
  3. A REAL oracle_fn that calls GPAW, on the spot-check subset only

ENV: run in `mace` for MACE-only mode. The GPAW oracle needs `dft`.
     Both are NOT in one env. See --mode flag. Fails loudly if imports missing.

USAGE
-----
  conda activate mace
  python pipeline.py --mode mace          # broad gates, no oracle  (minutes)
  python pipeline.py --mode oracle-list   # prints which systems need GPAW

  conda activate dft
  python pipeline.py --mode oracle        # GPAW on spot-check subset (batch!)
"""

import sys
import json
import argparse

# ---------------------------------------------------------------------------
# ENV GUARD - the split has bitten twice (ModuleNotFoundError). Fail clearly.
# ---------------------------------------------------------------------------
def require(modname, envname):
    try:
        __import__(modname)
    except ImportError:
        sys.exit(
            f"\n*** WRONG ENV ***\n"
            f"Could not import '{modname}'. That lives in the `{envname}` env.\n"
            f"Run:  conda activate {envname}\n"
            f"(Fresh terminals open in (base). This has cost us two sessions.)\n"
        )

import numpy as np
from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState

from descriptor_checker import (
    validate_descriptor, CheckResult, Verdict,
    check1_well_posed, check3_discriminates,
)


# ---------------------------------------------------------------------------
# THE MATERIAL SET  -  designed to ADJUDICATE the two blind predictions.
#   Benji : PARTIAL - breaks on ionic / layered / heavy (not magnetism)
#   Mentor: PARTIAL - breaks on magnetic transition metals (Fe/Ni)
# If the set contained only TMs, Benji couldn't lose. Only rocksalts, mentor
# couldn't lose. It contains BOTH, so the prediction is scoreable either way.
#
# ref_a = experimental lattice constant (Angstrom), conventional cubic cell.
# ref_density in g/cm^3 for the Tool 3 phase check.
# ---------------------------------------------------------------------------
SYSTEMS = [
    # --- group-IV baseline: the known-PASS control ---
    dict(name="C",    sym="C",  struct="diamond",  ref_a=3.567, ref_density=3.51, tag="baseline"),
    dict(name="Si",   sym="Si", struct="diamond",  ref_a=5.431, ref_density=2.33, tag="baseline"),
    dict(name="Ge",   sym="Ge", struct="diamond",  ref_a=5.658, ref_density=5.32, tag="baseline"),
    dict(name="Sn",   sym="Sn", struct="diamond",  ref_a=6.489, ref_density=5.77, tag="baseline"),
    # --- simple / noble metals: control ---
    dict(name="Al",   sym="Al", struct="fcc",      ref_a=4.050, ref_density=2.70, tag="metal"),
    dict(name="Cu",   sym="Cu", struct="fcc",      ref_a=3.615, ref_density=8.96, tag="metal"),
    # --- MENTOR'S HYPOTHESIS: magnetic transition metals ---
    dict(name="Fe",   sym="Fe", struct="bcc",      ref_a=2.867, ref_density=7.87, tag="magnetic-TM"),
    dict(name="Ni",   sym="Ni", struct="fcc",      ref_a=3.524, ref_density=8.91, tag="magnetic-TM"),
    # --- BENJI'S HYPOTHESIS: ionic rocksalts + heavy element ---
    dict(name="NaCl", sym="NaCl", struct="rocksalt", ref_a=5.640, ref_density=2.16, tag="ionic"),
    dict(name="MgO",  sym="MgO",  struct="rocksalt", ref_a=4.212, ref_density=3.58, tag="ionic"),
    dict(name="LiF",  sym="LiF",  struct="rocksalt", ref_a=4.027, ref_density=2.64, tag="ionic"),
    dict(name="Pb",   sym="Pb", struct="fcc",      ref_a=4.950, ref_density=11.34, tag="heavy"),
]


def make_atoms(s):
    """Build the conventional cell at the EXPERIMENTAL lattice constant."""
    return bulk(s["sym"], s["struct"], a=s["ref_a"], cubic=True)


# ---------------------------------------------------------------------------
# MACE CALCULATOR (shared, loaded once)
# ---------------------------------------------------------------------------
_mace = None
def mace_calc():
    global _mace
    if _mace is None:
        from mace.calculators import mace_mp
        _mace = mace_mp(model="medium", default_dtype="float64", device="cpu")
    return _mace


def relax_mace(atoms, fmax=0.01, steps=200):
    """Relax cell+positions with MACE. Returns (atoms, converged_bool, fmax_final)."""
    atoms = atoms.copy()
    atoms.calc = mace_calc()
    opt = BFGS(FrechetCellFilter(atoms), logfile=None)
    conv = opt.run(fmax=fmax, steps=steps)
    f = float(np.abs(atoms.get_forces()).max())
    return atoms, bool(conv), f


# ===========================================================================
# REAL DESCRIPTORS  -  these actually call MACE. No canned numbers.
# Contract: descriptor_fn(composition) -> float | None
#           None means "not well-defined for this composition"
# ===========================================================================

_cache = {}

def lattice_constant_descriptor(s):
    """
    DESCRIPTOR 1: relaxed cubic lattice constant (Angstrom), via MACE.
    Returns None if the relaxation fails to converge or the structure
    fails the pre-flight gate - that is an HONEST ill-posed signal.
    """
    key = ("a", s["name"])
    if key in _cache:
        return _cache[key]
    try:
        at, conv, f = relax_mace(make_atoms(s))
        if not conv:
            _cache[key] = None
            return None                      # UNCONVERGED is not an answer
        # conventional cubic cell -> a = V^(1/3)
        a = float(at.get_volume() ** (1 / 3))
        _cache[key] = a
        return a
    except Exception as e:
        print(f"    [{s['name']}] lattice descriptor raised: {type(e).__name__}: {e}")
        _cache[key] = None
        return None


def cohesive_energy_descriptor(s):
    """
    DESCRIPTOR 2: cohesive energy per atom (eV/atom), via MACE.
    E_coh = E_isolated_atoms/N - E_bulk/N   (reported POSITIVE = bound)
    NOTE: isolated-atom energies from an MLIP are a known weak point; this
    descriptor is EXPECTED to be shakier than lattice constant. That is the
    point - we are testing whether Tool 1 catches it.
    """
    key = ("ecoh", s["name"])
    if key in _cache:
        return _cache[key]
    try:
        at, conv, f = relax_mace(make_atoms(s))
        if not conv:
            _cache[key] = None
            return None
        e_bulk = float(at.get_potential_energy()) / len(at)

        # isolated atoms in a big box
        from ase import Atoms
        e_iso_total, n = 0.0, 0
        for symbol in set(at.get_chemical_symbols()):
            count = at.get_chemical_symbols().count(symbol)
            iso = Atoms(symbol, positions=[[0, 0, 0]], cell=[12, 12, 12], pbc=True)
            iso.calc = mace_calc()
            e_iso_total += float(iso.get_potential_energy()) * count
            n += count
        e_iso = e_iso_total / n
        ecoh = e_iso - e_bulk
        _cache[key] = ecoh
        return ecoh
    except Exception as e:
        print(f"    [{s['name']}] cohesive descriptor raised: {type(e).__name__}: {e}")
        _cache[key] = None
        return None


def bulk_modulus_descriptor(s):
    """
    DESCRIPTOR 3: bulk modulus B0 (GPa) from a Birch-Murnaghan EOS fit, via MACE.
    Returns None if the EOS fit fails - a real ill-posed signal (soft/unstable cell).
    """
    key = ("B", s["name"])
    if key in _cache:
        return _cache[key]
    try:
        at0, conv, f = relax_mace(make_atoms(s))
        if not conv:
            _cache[key] = None
            return None
        vols, enes = [], []
        for scale in (0.94, 0.97, 1.00, 1.03, 1.06):
            at = at0.copy()
            at.set_cell(at0.get_cell() * scale ** (1 / 3), scale_atoms=True)
            at.calc = mace_calc()
            vols.append(at.get_volume())
            enes.append(float(at.get_potential_energy()))
        eos = EquationOfState(vols, enes, eos="birchmurnaghan")
        v0, e0, B = eos.fit()
        B_gpa = float(B * 160.2176634)  # eV/A^3 -> GPa
        if not np.isfinite(B_gpa) or B_gpa <= 0:
            _cache[key] = None
            return None
        _cache[key] = B_gpa
        return B_gpa
    except Exception as e:
        print(f"    [{s['name']}] bulk-modulus descriptor raised: {type(e).__name__}: {e}")
        _cache[key] = None
        return None


DESCRIPTORS = {
    "lattice_constant": (lattice_constant_descriptor, "Angstrom", 0.02),
    "cohesive_energy":  (cohesive_energy_descriptor,  "eV/atom",  0.05),
    "bulk_modulus":     (bulk_modulus_descriptor,     "GPa",      2.0),
}


# ===========================================================================
# CHECK 0, FOR REAL  -  delegates to Tool 3 (structure_gate.gate).
# Replaces the unconditional-PASS stub.
# ===========================================================================

def check0_via_structure_gate(descriptor_fn, compositions, oracle_fn, cfg):
    """
    CHECK 0 - are the structures real? Delegates to the Structure Gate (Tool 3),
    which is a REAL instrument: min-distance, finite coords, relaxed-minimum
    (model-specific), density-vs-reference.

    A structure that is not a relaxed minimum, or whose density is far from the
    published reference, is not a valid substrate for ANY descriptor.
    """
    import structure_gate

    n_bad, details = 0, {}
    for s in compositions:
        try:
            at, conv, f = relax_mace(make_atoms(s))
            ok, rep = structure_gate.gate(
                at, name=s["name"], check_relaxed=True, ref_density=s["ref_density"]
            )
            phase_ok = True
            if "density" in rep:
                phase_ok = "PHASE-MISMATCH" not in str(rep["density"])
            if not ok or not conv or not phase_ok:
                n_bad += 1
                details[s["name"]] = f"gate_ok={ok} converged={conv} phase_ok={phase_ok}"
        except Exception as e:
            n_bad += 1
            details[s["name"]] = f"raised {type(e).__name__}"

    frac = n_bad / max(len(compositions), 1)
    verdict = Verdict.FAIL if frac > cfg.get("bad_structure_tolerance", 0.25) else Verdict.PASS
    return CheckResult(
        name="Check 0: structures real (via Tool 3)",
        verdict=verdict,
        detail=f"{n_bad}/{len(compositions)} structures failed the Structure Gate. "
               + ("FAIL - descriptor would be computed on bad geometry."
                  if verdict == Verdict.FAIL else "PASS - substrates are real."),
        numbers={"n_bad": n_bad, "n_total": len(compositions), **details},
    )


# ===========================================================================
# THE REAL ORACLE  -  GPAW. Runs ONLY on the spot-check subset.
# ===========================================================================

def gpaw_lattice_constant(s, ecut=500, kpts=(8, 8, 8)):
    """
    ORACLE: relaxed lattice constant from GPAW (PBE). Requires the `dft` env.
    This is the expensive truth-test. Called on extremes + suspicious point only.
    """
    require("gpaw", "dft")
    from gpaw import GPAW, PW

    at = make_atoms(s)
    at.calc = GPAW(mode=PW(ecut), xc="PBE", kpts=kpts,
                   txt=f"gpaw_{s['name']}.txt", symmetry={"point_group": False})
    opt = BFGS(FrechetCellFilter(at), logfile=f"gpaw_{s['name']}_opt.log")
    conv = opt.run(fmax=0.02, steps=60)
    if not conv:
        print(f"  [{s['name']}] GPAW UNCONVERGED - refusing to report a number.")
        return None
    return float(at.get_volume() ** (1 / 3))


def pick_spotcheck_subset(descriptor_fn, compositions, k_extremes=2):
    """
    SPOT-CHECK STRATEGY (from the spec): the EXTREMES + the SUSPICIOUS point.
      - fast-model best and worst (if the oracle flips them, ranking is dead)
      - plus the largest |MACE - experiment| deviation = where a confound hides
    Returns a list of systems to hand the oracle.
    """
    scored = [(s, descriptor_fn(s)) for s in compositions]
    good = [(s, v) for s, v in scored if v is not None]
    if len(good) < 2:
        return [s for s, _ in good]
    good.sort(key=lambda t: t[1])
    picks = [good[0][0], good[-1][0]]                      # extremes
    dev = sorted(good, key=lambda t: -abs(t[1] - t[0]["ref_a"]))
    for s, _ in dev:                                        # suspicious point
        if s not in picks:
            picks.append(s)
            break
    return picks


# ===========================================================================
# THE PIPELINE
# ===========================================================================

def run_mace_mode():
    require("mace", "mace")
    print("=" * 74)
    print("P5 ON-RAMP  -  verifier as a SYSTEM, first end-to-end run")
    print("Blind predictions on record (Tool 5):")
    print("   Benji : PARTIAL - breaks on ionic/layered/heavy")
    print("   Mentor: PARTIAL - breaks on magnetic TMs (Fe/Ni)")
    print("=" * 74)

    results = {}
    for dname, (dfn, unit, noise) in DESCRIPTORS.items():
        print(f"\n\n{'#' * 74}\n#  DESCRIPTOR: {dname}  ({unit})\n{'#' * 74}")
        cfg = {"noise_floor": noise, "illposed_tolerance": 0.25,
               "bad_structure_tolerance": 0.25}

        # Check 0 for real (Tool 3), then the engine's real checks 1 and 3.
        c0 = check0_via_structure_gate(dfn, SYSTEMS, None, cfg)
        c1 = check1_well_posed(dfn, SYSTEMS, None, cfg)
        c3 = check3_discriminates(dfn, SYSTEMS, None, cfg)

        print(f"\n  [{c0.verdict.value:11s}] {c0.name}\n      {c0.detail}")
        print(f"  [{c1.verdict.value:11s}] {c1.name}\n      {c1.detail}")
        print(f"  [{c3.verdict.value:11s}] {c3.name}\n      {c3.detail}")

        vals = {s["name"]: dfn(s) for s in SYSTEMS}
        results[dname] = {"values": vals,
                          "check0": c0.verdict.value,
                          "check1": c1.verdict.value,
                          "check3": c3.verdict.value}

        # per-system table, with % error vs experiment for lattice constant
        print(f"\n  {'system':6s} {'tag':13s} {'MACE':>10s}  {'ref':>8s}  {'err%':>7s}")
        for s in SYSTEMS:
            v = vals[s["name"]]
            if dname == "lattice_constant" and v is not None:
                err = (v - s["ref_a"]) / s["ref_a"] * 100
                print(f"  {s['name']:6s} {s['tag']:13s} {v:10.3f}  {s['ref_a']:8.3f}  {err:+7.2f}")
            else:
                shown = "None" if v is None else f"{v:.3f}"
                print(f"  {s['name']:6s} {s['tag']:13s} {shown:>10s}  {'-':>8s}  {'-':>7s}")

        if dname == "lattice_constant":
            oracle_targets = pick_spotcheck_subset(dfn, SYSTEMS)
            names = [t["name"] for t in oracle_targets]
            print(f"\n  ORACLE SPOT-CHECK TARGETS (run in `dft` env): {names}")
            results[dname]["oracle_targets"] = names

    with open("p5_onramp_mace.json", "w") as fh:
        json.dump(results, fh, indent=2, default=str)
    print("\n\nWrote p5_onramp_mace.json")
    print("\nNEXT: conda activate dft && python pipeline.py --mode oracle")


def run_oracle_mode():
    require("gpaw", "dft")
    try:
        with open("p5_onramp_mace.json") as fh:
            prev = json.load(fh)
    except FileNotFoundError:
        sys.exit("Run --mode mace first (need the spot-check targets).")

    names = prev.get("lattice_constant", {}).get("oracle_targets", [])
    targets = [s for s in SYSTEMS if s["name"] in names]
    print(f"GPAW oracle on spot-check subset: {[t['name'] for t in targets]}")
    print("(batch job - do NOT sit through this serially)\n")

    out = {}
    for s in targets:
        print(f"--- GPAW: {s['name']} ---")
        a = gpaw_lattice_constant(s)
        out[s["name"]] = a
        print(f"    a_GPAW = {a}\n")

    with open("p5_onramp_oracle.json", "w") as fh:
        json.dump(out, fh, indent=2)
    print("Wrote p5_onramp_oracle.json")
    print("\nNEXT: python pipeline.py --mode verdict  (in either env)")


def run_verdict_mode():
    """Tool 2 fidelity audit: does MACE's ranking survive the oracle?"""
    from model_fidelity import fidelity_audit
    with open("p5_onramp_mace.json") as fh:
        mace_res = json.load(fh)
    with open("p5_onramp_oracle.json") as fh:
        oracle_res = json.load(fh)

    pairs = [(n, mace_res["lattice_constant"]["values"][n], a)
             for n, a in oracle_res.items() if a is not None]
    if len(pairs) < 2:
        sys.exit("Need >=2 oracle points to audit ranking.")
    fast = [p[1] for p in pairs]
    orc = [p[2] for p in pairs]
    print(f"Systems audited: {[p[0] for p in pairs]}")
    fidelity_audit("lattice_constant (MACE vs GPAW)", fast, orc)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="mace",
                    choices=["mace", "oracle", "oracle-list", "verdict"])
    args = ap.parse_args()

    if args.mode == "mace":
        run_mace_mode()
    elif args.mode == "oracle":
        run_oracle_mode()
    elif args.mode == "verdict":
        run_verdict_mode()
    else:
        print("Spot-check targets come from p5_onramp_mace.json after --mode mace")
