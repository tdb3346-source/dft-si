from ase.io import read
import numpy as np
from gpaw import GPAW, PW

imgs = read("neb_mace.traj", index="-7:")
E = []
for k, im in enumerate(imgs):
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'audit_img{k}.log')
    e = im.get_potential_energy()
    E.append(e)
    print(f"image {k}: E = {e:.4f} eV", flush=True)
E = np.array(E) - E[0]
np.save("barrier_gpaw_on_mace_path.npy", E)
print("GPAW energies on MACE path (eV):", np.round(E, 3))
print("GPAW BARRIER =", round(float(E.max()), 3), "eV   (peak at image", int(E.argmax()), ")")
print("MACE BARRIER = 0.149 eV (peak at image 3)")
