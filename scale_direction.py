from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print(f"{'mat':12s}{'alpha':>8s}{'cosine':>8s}{'rel% raw':>10s}{'rel% rescaled':>14s}")
for name, xyz, npy in [("si_v2","rattled_si_v2.xyz","forces_si_v2_gpaw.npy"),
                       ("sto","rattled_sto.xyz","forces_sto_gpaw.npy"),
                       ("cspbi3_v2","rattled_cspbi3_v2.xyz","forces_cspbi3_v2_gpaw.npy")]:
    at = read(xyz); at.calc = calc
    fm = at.get_forces().ravel(); fg = np.load(npy).ravel()
    alpha = float(fm @ fg) / float(fg @ fg)          # best single scale GPAW->MACE
    cos = float(fm @ fg) / (np.linalg.norm(fm) * np.linalg.norm(fg))
    rel_raw = 100 * np.linalg.norm(fm - fg) / np.linalg.norm(fg)
    rel_rescaled = 100 * np.linalg.norm(fm/alpha - fg) / np.linalg.norm(fg)
    print(f"{name:12s}{alpha:8.3f}{cos:8.3f}{rel_raw:10.1f}{rel_rescaled:14.1f}")
