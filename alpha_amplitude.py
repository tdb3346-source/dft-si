from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
at = read("rattled_si.xyz"); at.calc = calc
fm = at.get_forces().ravel(); fg = np.load("forces_si_gpaw.npy").ravel()
alpha = float(fm @ fg) / float(fg @ fg)
cos = float(fm @ fg) / (np.linalg.norm(fm) * np.linalg.norm(fg))
print(f"Si @ 0.05 A: alpha = {alpha:.3f}, cosine = {cos:.3f}   (0.02 A gave 0.543 / 0.997)")
