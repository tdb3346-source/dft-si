from ase.io import read, write
import numpy as np
from gpaw import GPAW, PW

# ASE's NEB writes each image's trajectory; grab the final geometry of each
imgs = []
for i in range(5):
    try:
        imgs.append(read(f"neb{i}.traj", index=-1))
    except Exception as e:
        print("no traj for image", i, "-", e)
if not imgs:
    print("NO TRAJECTORIES - fallback needed"); raise SystemExit
print("recovered", len(imgs), "images")
E = []
for k, im in enumerate(imgs):
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'rescue_{k}.log')
    E.append(im.get_potential_energy())
E = np.array(E) - E[0]
top = int(E.argmax())
write("cspbi3_saddle_relaxed.xyz", imgs[top])
np.save("forces_saddle_relaxed_gpaw.npy", imgs[top].get_forces())
print("energies (eV):", np.round(E, 3))
print("BARRIER (unconverged NEB) =", round(float(E.max()), 3), "eV  image", top)
