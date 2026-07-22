from ase.io import read
import numpy as np
from gpaw import GPAW, PW
import time

imgs = read("neb_mace_11.traj", index="-11:")
E = []
for k in range(11):
    im = imgs[k]
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'bf_{k}.log')
    e = im.get_potential_energy()
    E.append(e)
    print(f"image {k}: {e:.4f} eV   {time.ctime()}", flush=True)
E = np.array(E) - E[0]
print("FULL 11-point energies:", np.round(E,3), flush=True)
print("REFEREE IODIDE BARRIER =", round(float(E.max()),3), "eV", flush=True)
print("compare: 4-point 0.108 | MACE 0.152", flush=True)
