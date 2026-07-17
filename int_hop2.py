from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

at = read("cspbi3_int_222.xyz")
extra = len(at) - 1
d = at.get_distances(extra, range(len(at)-1), mic=True)

# the lattice iodine it shares the bridge with
I_lat = [i for i in range(len(at)-1) if at[i].symbol == 'I']
partner_I = min(I_lat, key=lambda i: d[i])
offset = at.get_distance(partner_I, extra, mic=True, vector=True)   # the "beside it" vector
print("bridge partner: I idx", partner_I, " offset =", np.round(offset, 3), " |offset| =", round(float(np.linalg.norm(offset)),3))

# a DIFFERENT lattice iodine to hop to: nearest one that isn't the partner
cands = sorted([i for i in I_lat if i != partner_I], key=lambda i: d[i])
for target_I in cands[:4]:
    newpos = at.positions[target_I] + offset
    trial = at.copy(); trial.positions[extra] = newpos
    dmin = trial.get_distances(extra, range(len(trial)-1), mic=True).min()
    print(f"  candidate I idx {target_I}: nearest-atom = {dmin:.3f} A", "OK" if dmin > 2.5 else "reject")
    if dmin > 2.5:
        fin = trial; chosen = target_I; break
else:
    print("no sane target found"); raise SystemExit

print("hopping to bridge at I idx", chosen, "- relaxing...")
fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='int_hop2_relax.log').run(fmax=0.02, steps=400)
write("int_fin_mace.xyz", fin)
ini = at.copy(); ini.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
Ei, Ef = ini.get_potential_energy(), fin.get_potential_energy()
print("E(init) =", round(float(Ei),4), " E(fin) =", round(float(Ef),4), " diff =", round(float(Ef-Ei),4), "eV")
print("KILL-CHECK: |diff| < 0.05 eV = equivalent sites = legitimate path")
