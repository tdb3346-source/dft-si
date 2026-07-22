from ase.io import read
from mace.calculators import mace_mp
import numpy as np

_calc = None
def calc():
    global _calc
    if _calc is None:
        _calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    return _calc

def gate(atoms, name="?", check_relaxed=True, ref_density=None):
    """Pre-flight structure sanity. Returns (ok, report). Run BEFORE any compute."""
    r = {}
    # 1. min interatomic distance (catch atom-on-atom)
    d = atoms.get_all_distances(mic=True)
    np.fill_diagonal(d, np.inf)
    dmin = float(d.min())
    r["min_dist"] = (round(dmin,3), "OK" if dmin > 1.5 else "REJECT atom-collision")
    # 2. no NaN/inf positions
    finite = np.isfinite(atoms.get_positions()).all()
    r["positions_finite"] = ("OK" if finite else "REJECT non-finite coords")
    # 3. relaxed-minimum test (model-specific)
    if check_relaxed and dmin > 1.5 and finite:
        atoms.calc = calc()
        fmax = float(np.abs(atoms.get_forces()).max())
        r["relaxed"] = (round(fmax,3), "REAL" if fmax < 0.05 else "NOT-RELAXED")
    # 4. density vs reference (phase check)
    if ref_density is not None:
        vol = atoms.get_volume(); mass = sum(atoms.get_masses())
        dens = mass/vol * 1.66054  # amu/A^3 -> g/cm^3
        off = abs(dens-ref_density)/ref_density*100
        r["density"] = (round(dens,2), f"{off:.0f}% vs ref", "OK" if off<10 else "PHASE-MISMATCH")
    # verdict
    reject = any("REJECT" in str(v) for v in r.values())
    ok = not reject
    print(f"STRUCTURE GATE: {name}")
    for k,v in r.items(): print(f"  {k}: {v}")
    print(f"  -> {'PASS' if ok else 'REJECT'}\n")
    return ok, r

if __name__ == "__main__":
    from ase.build import bulk
    # PASS: relaxed group-IV
    at = bulk("Si","diamond",a=5.431,cubic=True); at.calc=calc()
    from ase.optimize import BFGS; from ase.filters import FrechetCellFilter
    BFGS(FrechetCellFilter(at),logfile=None).run(fmax=0.01,steps=100)
    gate(at, "relaxed Si (should PASS)")
    # REJECT: atom collision
    bad = bulk("Si","diamond",a=5.431,cubic=True); p=bad.get_positions(); p[1]=p[0]+0.3; bad.set_positions(p)
    gate(bad, "atom-collision (should REJECT)", check_relaxed=False)
    # real delta: relaxed but check density
    y = read("delta_cspbi3_real.xyz")
    gate(y, "delta-CsPbI3 (relaxed, density flag)")
