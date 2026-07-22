from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("cl_neb.traj", index="-11:")
E = []
for k in [0, 5]:
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'cl_g{k}.log')
    e = im.get_potential_energy()
    E.append(e)
    print(f"Cl image {k}: E = {e:.4f} eV", flush=True)
b = E[1] - E[0]
print(f"CsPbCl3 GPAW BARRIER = {b:.3f} eV", flush=True)
print(f"CsPbCl3 MACE = 0.108 eV -> overpredicts by {100*(0.108-b)/b:.1f} percent", flush=True)
print("TREND: CsPbI3 +41% | CsPbBr3 +11% | CsPbCl3 = ?", flush=True)
