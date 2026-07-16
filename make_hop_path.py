from ase.io import read, write
import numpy as np

vac = read("cspbi3_vac_222_relaxed.xyz")
pris = read("cspbi3_pristine_222.xyz")

# where the vacancy is: the pristine I site with no atom near it in the relaxed cell
I_pris = [a.index for a in pris if a.symbol == 'I']
pos_vac = None
for i in I_pris:
    d = np.linalg.norm(vac.get_positions() - pris.positions[i], axis=1).min()
    if d > 1.0:
        pos_vac = pris.positions[i]; break
print("vacancy site:", np.round(pos_vac, 3))

# nearest iodine to the hole = the one that will hop in
I_vac = [a.index for a in vac if a.symbol == 'I']
d = np.linalg.norm(vac.get_positions()[I_vac] - pos_vac, axis=1)
hopper = I_vac[int(d.argmin())]
print("hopping atom: index", hopper, " distance to hole =", round(float(d.min()), 3), "A")

# midpoint image = crude saddle
mid = vac.copy()
mid.positions[hopper] = 0.5 * (vac.positions[hopper] + pos_vac)
write("cspbi3_saddle_crude.xyz", mid)
print("saddle image written")
