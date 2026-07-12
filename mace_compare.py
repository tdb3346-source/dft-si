from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print(f"{'mat':8s}{'RMSE eV/A':>12s}{'max|dF|':>10s}")
for name in ["si", "sto", "cspbi3"]:
    at = read(f"rattled_{name}.xyz"); at.calc = calc
    d = at.get_forces() - np.load(f"forces_{name}_gpaw.npy")
    print(f"{name:8s}{np.sqrt((d**2).mean()):12.4f}{abs(d).max():10.4f}")
