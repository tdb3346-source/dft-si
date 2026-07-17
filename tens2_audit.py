from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("tens2_neb.traj", index="-11:")
E = []
for k in [0, 4, 5, 6]:
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'tens2_img{k}.log')
    e = im.get_potential_energy()
    E.append((k, e))
    print("image", k, "E =", round(float(e), 4), flush=True)
E0 = E[0][1]
rel = [(k, e - E0) for k, e in E]
print("GPAW rel energies tension:", [(k, round(v, 3)) for k, v in rel])
gb = max(v for _, v in rel)
print("GPAW BARRIER tension =", round(float(gb), 3), "eV")
print("MACE BARRIER tension = 0.112 eV")
print("MACE overpredicts by", round(100 * (0.112 - gb) / gb, 1), "percent")
print("unstrained reference: GPAW 0.108, MACE 0.152, plus 41 percent")
