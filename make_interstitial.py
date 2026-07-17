from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
I_idx = [a.index for a in pris if a.symbol == 'I']
pos = pris.positions[I_idx[0]].copy()
new_pos = pos + np.array([2.9, 0.0, 0.0])

at = pris.copy()
at.append('I')
at.positions[-1] = new_pos
print("interstitial cell:", len(at), "atoms", at.get_chemical_formula())

at.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(at, logfile='int_relax.log').run(fmax=0.02)
write("cspbi3_int_222.xyz", at)
print("relaxed. E =", round(float(at.get_potential_energy()), 4), "eV")

others = [a.index for a in at if a.symbol == 'I' and a.index != len(at)-1]
d = at.get_distances(len(at)-1, others, mic=True)
print("KILL-CHECK: nearest I-I =", round(float(d.min()), 3), "A  (expect ~3.0-3.6 for a bridge, NOT <2.7)")
