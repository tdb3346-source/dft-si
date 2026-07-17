from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

initial = read("vac_init_mace.xyz")
final = read("vac_fin_mace.xyz")
images = [initial] + [initial.copy() for _ in range(9)] + [final]
for im in images:
    im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
neb = NEB(images, climb=True, method='improvedtangent')
neb.interpolate()
BFGS(neb, logfile='neb11_bfgs.log', trajectory='neb_mace_11.traj').run(fmax=0.05, steps=300)

E = np.array([im.get_potential_energy() for im in images]); E -= E[0]
top = int(E.argmax())
print("MACE-11 energies (eV):", np.round(E, 3))
print("MACE-11 BARRIER =", round(float(E.max()), 3), "eV  (peak image", top, "of 10)")
print("compare: MACE-7 barrier was 0.149 eV at image 3 of 6")
