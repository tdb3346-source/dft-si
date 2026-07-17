from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("neb_mace_11.traj", index="-11:")
E = []
for k in [0, 4, 5, 6]:                    # endpoint + the three around the peak
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'audit11_img{k}.log')
    e = im.get_potential_energy()
    E.append((k, e))
    print(f"image {k}: E = {e:.4f} eV", flush=True)
E0 = E[0][1]
rel = [(k, e - E0) for k, e in E]
print("GPAW rel energies on MACE-11 path:", [(k, round(v, 3)) for k, v in rel])
peak = max(v for _, v in rel)
print("GPAW BARRIER (on MACE-11 path) =", round(float(peak), 3), "eV")
print("MACE-11 BARRIER = 0.152 eV   | prior round: GPAW 0.121 vs MACE 0.149 (MACE +23%)")
