from ase.spacegroup import crystal
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

# delta-CsPbI3 (yellow), orthorhombic Pnma (#62), published lattice ~a=10.46 b=4.80 c=17.78
# approximate Wyckoff positions for the non-perovskite edge-sharing phase
try:
    y = crystal(['Cs','Pb','I','I'],
                basis=[(0.25,0.25,0.10),(0.25,0.25,0.42),
                       (0.25,0.25,0.28),(0.03,0.25,0.53)],
                spacegroup=62, cellpar=[10.46,4.80,17.78,90,90,90])
    print("built delta-CsPbI3:", y.get_chemical_formula(), len(y), "atoms")
    y.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    f0 = float(np.abs(y.get_forces()).max())
    print("before relax max|F|:", round(f0,3))
    BFGS(FrechetCellFilter(y), logfile=None).run(fmax=0.05, steps=300)
    f1 = float(np.abs(y.get_forces()).max())
    E = y.get_potential_energy()/ (len(y)//5)   # per f.u. (CsPbI3 = 5 atoms)
    print("after relax max|F|:", round(f1,3), "REAL" if f1<0.05 else "not converged")
    print("E_yellow/fu:", round(E,4), "eV")
    from ase.io import write; write("delta_cspbi3_real.xyz", y)
except Exception as e:
    print("ERROR:", e)
