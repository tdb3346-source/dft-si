from ase.io import read
import numpy as np
from gpaw import GPAW, PW

for tag in ["s067", "s133"]:
    imgs = read(f"{tag}_neb.traj", index="-11:")
    E = []
    for k in [0, 5]:
        im = imgs[k]
        im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'{tag}_g{k}.log')
        e = im.get_potential_energy()
        E.append(e)
        print(f"{tag} image {k}: E = {e:.4f} eV", flush=True)
    b = E[1] - E[0]
    print(f"{tag}: GPAW BARRIER = {b:.3f} eV", flush=True)
    print(f"{tag}: MACE overpredicts by {100*((0.141 if tag=='s067' else 0.130)-b)/b:.1f} percent", flush=True)
print("reference: 0% GPAW 0.108 MACE 0.152 = +41% | 2% GPAW 0.092 MACE 0.112 = +21%", flush=True)
