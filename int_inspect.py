from ase.io import read
import numpy as np

at = read("cspbi3_int_222.xyz")
extra = len(at) - 1
print("interstitial at:", np.round(at.positions[extra], 3))
d = at.get_distances(extra, range(len(at)-1), mic=True)
order = np.argsort(d)[:6]
print("\nnearest 6 neighbours to the interstitial:")
for i in order:
    print(f"  {at[i].symbol:2s} idx {i:2d}   d = {d[i]:.3f} A")
