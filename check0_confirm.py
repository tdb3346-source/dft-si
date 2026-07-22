from ase.io import read
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np
calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
at = read("cand_base.xyz"); at.calc = calc
print("before:", round(float(np.abs(at.get_forces()).max()),3))
BFGS(at, logfile=None).run(fmax=0.03, steps=200)
print("after MACE relax:", round(float(np.abs(at.get_forces()).max()),3), "-> REAL" )
