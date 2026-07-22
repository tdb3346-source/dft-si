from ase.io import read
import numpy as np
from gpaw import GPAW, PW
imgs = read("neb_mace_11.traj", index="-11:")
saved = [-110.2926,-110.3887,-110.4680,-110.3760,-110.2346,-110.1845,-110.2365]
E = list(saved)
for k in [7,8,9,10]:
    im = imgs[k]; im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'bf_{k}.log')
    e = im.get_potential_energy(); E.append(e)
    print(f"image {k}: {e:.4f}", flush=True)
E = np.array(E) - E[0]
print("FULL 11:", np.round(E,3), flush=True)
print("REFEREE IODIDE BARRIER =", round(float(E.max()),3), "eV", flush=True)
