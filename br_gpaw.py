from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("br_neb.traj", index="-11:")
E = []
for k in [0, 5]:
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'br_g{k}.log')
    e = im.get_potential_energy()
    E.append(e)
    print(f"Br image {k}: E = {e:.4f} eV", flush=True)
b = E[1] - E[0]
print(f"CsPbBr3 GPAW BARRIER = {b:.3f} eV", flush=True)
print(f"CsPbBr3 MACE = 0.139 eV -> overpredicts by {100*(0.139-b)/b:.1f} percent", flush=True)
print("compare CsPbI3 unstrained: GPAW 0.108, MACE 0.152, +41%", flush=True)
