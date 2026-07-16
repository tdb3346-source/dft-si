from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from gpaw import GPAW, PW
import numpy as np

initial = read("cspbi3_vac_222_relaxed.xyz")
pris = read("cspbi3_pristine_222.xyz")

# locate the hole (pristine I site with no atom nearby in the relaxed vacancy cell)
for i in [a.index for a in pris if a.symbol == 'I']:
    if np.linalg.norm(initial.get_positions() - pris.positions[i], axis=1).min() > 1.0:
        hole = pris.positions[i]; break

# the hopper = nearest I to the hole
I_idx = [a.index for a in initial if a.symbol == 'I']
d = np.linalg.norm(initial.get_positions()[I_idx] - hole, axis=1)
hopper = I_idx[int(d.argmin())]

# final state: that iodine has moved into the hole
final = initial.copy()
final.positions[hopper] = hole

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for im in images:
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=None)

neb = NEB(images, climb=True)
neb.interpolate()
BFGS(neb, logfile='neb_bfgs.log').run(fmax=0.10)

E = np.array([im.get_potential_energy() for im in images])
E -= E[0]
top = int(E.argmax())
write("cspbi3_saddle_relaxed.xyz", images[top])
np.save("forces_saddle_relaxed_gpaw.npy", images[top].get_forces())
print("NEB done. energies (eV):", np.round(E, 3))
print("BARRIER =", round(float(E.max()), 3), "eV   (climbing image =", top, ")")
