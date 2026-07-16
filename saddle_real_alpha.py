from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
at = read("saddle_real.xyz"); at.calc = calc
fm = at.get_forces().ravel()
fg = np.load("forces_saddle_real_gpaw.npy").ravel()
alpha = float(fm @ fg) / float(fg @ fg)
cos = float(fm @ fg) / (np.linalg.norm(fm) * np.linalg.norm(fg))
rel = 100 * np.linalg.norm(fm - fg) / np.linalg.norm(fg)
print(f"REAL SADDLE (NEB image 3): alpha = {alpha:.3f}, cosine = {cos:.3f}, rel% = {rel:.1f}")
print(f"   RMS_F gpaw = {np.sqrt((fg**2).mean()):.4f} eV/A  (max {abs(fg).max():.3f})")
print(f"   compare: rattled 0.2A alpha 0.882 (RMS 0.46) | crude midpoint 0.832 (RMS 1.49)")
