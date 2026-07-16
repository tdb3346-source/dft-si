from ase.io import read
import numpy as np
from gpaw import GPAW, PW

at = read("cspbi3_saddle_crude.xyz")
at.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt='saddle_gpaw.log')
f = at.get_forces()
np.save("forces_saddle_gpaw.npy", f)
print("saddle GPAW done. max|F| =", round(float(abs(f).max()), 4), "eV/A")
