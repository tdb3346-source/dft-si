from ase.io import read, write
from ase.optimize import BFGS
from gpaw import GPAW, PW
import numpy as np

atoms = read("cspbi3_vac_222.xyz")
atoms.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt='vac_relax_gpaw.log')
BFGS(atoms, logfile='vac_relax_bfgs.log').run(fmax=0.02)
write("cspbi3_vac_222_relaxed.xyz", atoms)
pb = [a.index for a in atoms if a.symbol == 'Pb']
d = atoms.get_distances(pb[0], pb[1:], mic=True)
print("relaxed. min Pb-Pb =", round(float(d.min()), 4), "A  (pristine = 6.390)")
