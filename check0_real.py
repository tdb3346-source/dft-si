from ase.io import read
from mace.calculators import mace_mp
import numpy as np, glob

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

def is_real(fname, ftol=0.05):
    """Real structure = relaxed minimum = max force below ftol eV/A."""
    at = read(fname); at.calc = calc
    fmax = float(np.abs(at.get_forces()).max())
    return fmax, fmax < ftol

# test on structures we have: relaxed ones should pass, raw/approximated should fail
tests = ["cspbi3_vac_222_relaxed.xyz", "cand_base.xyz", "cand_br.xyz"]
for f in tests:
    try:
        fmax, ok = is_real(f)
        print(f"{f:32s} max|F|={fmax:.3f}  {'REAL' if ok else 'NOT-RELAXED'}", flush=True)
    except Exception as e:
        print(f"{f}: {e}", flush=True)
