from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

initial = read("cspbi3_vac_222_relaxed.xyz")
pris = read("cspbi3_pristine_222.xyz")
for i in [a.index for a in pris if a.symbol == 'I']:
    if np.linalg.norm(initial.get_positions() - pris.positions[i], axis=1).min() > 1.0:
        hole = pris.positions[i]; break
I_idx = [a.index for a in initial if a.symbol == 'I']
d = np.linalg.norm(initial.get_positions()[I_idx] - hole, axis=1)
hopper = I_idx[int(d.argmin())]

final = initial.copy()
final.positions[hopper] = hole
final.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(final, logfile='final_relax.log').run(fmax=0.02)
write("cspbi3_vac_final_relaxed.xyz", final)

ei = initial.copy(); ei.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print("E(initial) =", round(float(ei.get_potential_energy()), 4))
print("E(final)   =", round(float(final.get_potential_energy()), 4))
print("difference =", round(float(final.get_potential_energy() - ei.get_potential_energy()), 4), "eV")
print("KILL-CHECK: |difference| should be < ~0.05 eV (equivalent sites by symmetry)")
