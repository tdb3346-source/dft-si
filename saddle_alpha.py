from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
at = read("cspbi3_saddle_crude.xyz"); at.calc = calc
fm = at.get_forces().ravel()
fg = np.load("forces_saddle_gpaw.npy").ravel()
alpha = float(fm @ fg) / float(fg @ fg)
cos = float(fm @ fg) / (np.linalg.norm(fm) * np.linalg.norm(fg))
rel = 100 * np.linalg.norm(fm - fg) / np.linalg.norm(fg)
print(f"SADDLE (crude): alpha = {alpha:.3f}, cosine = {cos:.3f}, rel% = {rel:.1f}")
print(f"   compare: rattled CsPbI3 0.2A gave alpha 0.882, cos 0.999, rel% 12.5")
print(f"   RMS_F gpaw = {np.sqrt((fg**2).mean()):.3f} eV/A")
