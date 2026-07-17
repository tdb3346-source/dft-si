from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
cell = pris.get_cell().copy(); cell[2] = cell[2] * 0.98

at = pris.copy(); at.set_cell(cell, scale_atoms=True)
I_idx = [a.index for a in at if a.symbol == 'I']
del at[I_idx[4]]
at.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(at, logfile='comp4_init.log').run(fmax=0.02, steps=200)
write("comp4_init.xyz", at)

p2 = pris.copy(); p2.set_cell(cell, scale_atoms=True)
for i in [a.index for a in p2 if a.symbol == 'I']:
    if np.linalg.norm(at.get_positions() - p2.positions[i], axis=1).min() > 1.0:
        hole = p2.positions[i]; break
Ii = [a.index for a in at if a.symbol == 'I']
hopper = Ii[int(np.linalg.norm(at.get_positions()[Ii] - hole, axis=1).argmin())]

fin = at.copy(); fin.positions[hopper] = hole
fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='comp4_fin.log').run(fmax=0.02, steps=200)
write("comp4_fin.xyz", fin)
print("endpoint diff =", round(float(fin.get_potential_energy() - at.get_potential_energy()), 4), "eV", flush=True)

imgs = [at] + [at.copy() for _ in range(9)] + [fin]
for im in imgs:
    im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
neb = NEB(imgs, climb=True, method='improvedtangent')
neb.interpolate()
BFGS(neb, logfile='comp4_neb.log', trajectory='comp4_neb.traj').run(fmax=0.05, steps=300)
E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
print("comp4 MACE energies:", np.round(E, 3), flush=True)
print("comp4 MACE BARRIER =", round(float(E.max()), 3), "eV at image", int(E.argmax()), flush=True)
