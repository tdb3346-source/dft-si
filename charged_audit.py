from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("neb_mace_11.traj", index="-11:")
E = []
for k in [0, 4, 5, 6]:
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE',
                   charge=+1, txt=f'charged_img{k}.log')
    e = im.get_potential_energy()
    E.append((k, e))
    print(f"image {k} (charge +1): E = {e:.4f} eV", flush=True)
E0 = E[0][1]
rel = [(k, e - E0) for k, e in E]
print("GPAW +1 rel energies:", [(k, round(v, 3)) for k, v in rel])
print("V_I+ BARRIER (on neutral path) =", round(float(max(v for _, v in rel)), 3), "eV")
print("compare: neutral V_I0 barrier = 0.108 eV | MACE (neutral only) = 0.152 eV")
