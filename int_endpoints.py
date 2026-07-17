from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

at = read("cspbi3_int_222.xyz")
extra = len(at) - 1                       # the interstitial we added
pos = at.positions[extra].copy()

# hop target: reflect the interstitial across its nearest lattice iodine
others = [a.index for a in at if a.symbol == 'I' and a.index != extra]
d = at.get_distances(extra, others, mic=True)
neighbor = others[int(d.argmin())]
target = 2 * at.positions[neighbor] - pos   # kick-out / exchange geometry

fin = at.copy()
fin.positions[extra] = target
fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='int_fin_relax.log').run(fmax=0.02)
write("int_fin_mace.xyz", fin)

ini = at.copy()
ini.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
Ei = ini.get_potential_energy(); Ef = fin.get_potential_energy()
print("E(init) =", round(float(Ei), 4), " E(fin) =", round(float(Ef), 4))
print("difference =", round(float(Ef - Ei), 4), "eV")
print("KILL-CHECK: |diff| < 0.05 eV means the two sites are equivalent - path is legitimate")
