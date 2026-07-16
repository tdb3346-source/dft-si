from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
initial = read("vac_init_mace.xyz")
pris = read("cspbi3_pristine_222.xyz")
for i in [a.index for a in pris if a.symbol == 'I']:
    if np.linalg.norm(initial.get_positions() - pris.positions[i], axis=1).min() > 1.0:
        hole = pris.positions[i]; break
I_idx = [a.index for a in initial if a.symbol == 'I']
d = np.linalg.norm(initial.get_positions()[I_idx] - hole, axis=1)
hopper = I_idx[int(d.argmin())]
final = read("vac_fin_mace.xyz")

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for im in images:
    im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
neb = NEB(images, climb=True, method='improvedtangent')
neb.interpolate()
BFGS(neb, logfile='neb_mace_bfgs.log', trajectory='neb_mace.traj').run(fmax=0.05)

E = np.array([im.get_potential_energy() for im in images]); E -= E[0]
top = int(E.argmax())
write("saddle_mace_path.xyz", images[top])
print("MACE NEB energies (eV):", np.round(E, 3))
print("MACE BARRIER =", round(float(E.max()), 3), "eV   (image", top, ")")
