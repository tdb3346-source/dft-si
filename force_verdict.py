from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print(f"{'mat':8s}{'RMS_F_gpaw':>12s}{'RMSE':>10s}{'rel%':>8s}{'max|dF|':>10s}")
for name in ["si", "sto", "cspbi3"]:
    at = read(f"rattled_{name}.xyz"); at.calc = calc
    fg = np.load(f"forces_{name}_gpaw.npy")
    d = at.get_forces() - fg
    rmse = np.sqrt((d**2).mean()); rms = np.sqrt((fg**2).mean())
    print(f"{name:8s}{rms:12.4f}{rmse:10.4f}{100*rmse/rms:8.1f}{abs(d).max():10.4f}")
