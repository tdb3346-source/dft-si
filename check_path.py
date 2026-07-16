from ase.io import read
import numpy as np

imgs = read("neb_mace.traj", index="-7:")   # last 7 = final band
pris = read("cspbi3_pristine_222.xyz")
init = read("vac_init_mace.xyz")
for i in [a.index for a in pris if a.symbol == 'I']:
    if np.linalg.norm(init.get_positions() - pris.positions[i], axis=1).min() > 1.0:
        hole = pris.positions[i]; break
I_idx = [a.index for a in init if a.symbol == 'I']
hopper = I_idx[int(np.linalg.norm(init.get_positions()[I_idx] - hole, axis=1).argmin())]
print("image | hopper dist to hole | max displacement of ANY other atom")
ref = init.get_positions()
for k, im in enumerate(imgs):
    d = np.linalg.norm(im.positions[hopper] - hole)
    other = np.linalg.norm(im.get_positions() - ref, axis=1)
    other[hopper] = 0
    print(f"  {k}   |   {d:.3f} A          |   {other.max():.3f} A")
