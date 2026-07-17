from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

at = read("cspbi3_int_222.xyz")
extra = len(at) - 1
d_all = at.get_distances(extra, range(len(at)-1), mic=True)
pb = [i for i in range(len(at)-1) if at[i].symbol == 'Pb']
pb_near = sorted(pb, key=lambda i: d_all[i])[:2]      # the two Pb it bridges now
print("currently bridging Pb:", pb_near, "at", np.round([d_all[i] for i in pb_near], 3))

# find a DIFFERENT Pb pair: keep one Pb, find its next-nearest Pb neighbour
anchor = pb_near[0]
d_pb = at.get_distances(anchor, pb, mic=True)
cands = [(pb[k], d_pb[k]) for k in range(len(pb)) if pb[k] not in (anchor, pb_near[1]) and d_pb[k] > 0.1]
partner = min(cands, key=lambda x: x[1])[0]
print("new bridge: Pb", anchor, "+ Pb", partner)

# midpoint of the new Pb pair, nudged off-axis like the current site
mid = at.positions[anchor] + 0.5 * at.get_distance(anchor, partner, mic=True, vector=True)
fin = at.copy()
fin.positions[extra] = mid

# STRUCTURE KILL-CHECK BEFORE ANY OPTIMIZER (catch #23's lesson)
dmin = fin.get_distances(extra, range(len(fin)-1), mic=True).min()
print("KILL-CHECK: nearest atom to new position =", round(float(dmin), 3), "A")
if dmin < 2.0:
    print("REJECTED - too close, would explode. Stopping."); raise SystemExit
print("geometry sane, relaxing...")

fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='int_hop_relax.log').run(fmax=0.02, steps=400)
write("int_fin_mace.xyz", fin)
ini = at.copy(); ini.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print("E(init) =", round(float(ini.get_potential_energy()), 4),
      " E(fin) =", round(float(fin.get_potential_energy()), 4),
      " diff =", round(float(fin.get_potential_energy() - ini.get_potential_energy()), 4), "eV")
