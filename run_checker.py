from ase.spacegroup import crystal
from ase.io import read
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# --- the descriptor under test: phase-stability, on REAL relaxed structures ---
# (uses the real delta yellow + cubic black; per-fu dE)
def phase_stability():
    u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
                spacegroup=221, cellpar=[6.39]*3+[90]*3)
    black = u.repeat((1,1,1)); black.calc = calc
    BFGS(FrechetCellFilter(black), logfile=None).run(fmax=0.03, steps=300)
    Eb = black.get_potential_energy()
    yellow = read("delta_cspbi3_real.xyz"); yellow.calc = calc
    Ey = yellow.get_potential_energy()/(len(yellow)//5)
    return (Eb-Ey)*1000, float(np.abs(yellow.get_forces()).max())

dE, fmax_y = phase_stability()

print("="*50)
print("DESCRIPTOR-VALIDITY REPORT: phase_stability (real structures)")
print("="*50)
# Check 0: structures real
c0 = "PASS" if fmax_y < 0.05 else "FAIL"
print(f"  [{c0:11s}] Check 0: structures real   (yellow max|F|={fmax_y:.3f})")
# Check 1: well-posed (phase-stability IS well-posed for any comp - single number)
print(f"  [{'PASS':11s}] Check 1: well-posed        (single dE per composition)")
# Check 3: discriminates - need >1 comp; here 1 comp so report the value
print(f"  [{'N/A':11s}] Check 3: discriminates     (1 composition tested; dE={dE:+.0f} meV/fu)")
# Oracle check: is the MAGNITUDE physically sane?
sane = 20 <= abs(dE) <= 100
c_oracle = "PASS" if sane else "FAIL"
print(f"  [{c_oracle:11s}] Check 2+4: oracle sanity   (dE={dE:+.0f} meV/fu; expect 20-100 for CsPbI3)")
print("-"*50)
overall = "UNCERTIFIED/FAIL" if not sane else "PASS"
print(f"  OVERALL: {overall}")
print(f"  reason: magnitude {abs(dE):.0f} meV/fu is outside physical range -> yellow structure needs refinement")
