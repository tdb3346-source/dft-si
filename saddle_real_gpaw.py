from ase.io import read, write
import numpy as np
from gpaw import GPAW, PW

imgs = read("neb_mace.traj", index="-7:")
at = imgs[3]                      # the peak, dead center
write("saddle_real.xyz", at)
at.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt='saddle_real_gpaw.log')
f = at.get_forces()
np.save("forces_saddle_real_gpaw.npy", f)
print("saddle (image 3) GPAW done. max|F| =", round(float(abs(f).max()), 4),
      " RMS|F| =", round(float(np.sqrt((f**2).mean())), 4), "eV/A")
