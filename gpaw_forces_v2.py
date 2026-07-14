from ase.io import read
import numpy as np
from gpaw import GPAW, PW

jobs = {
    "si_v2":       ("rattled_si_v2.xyz",     dict(mode=PW(500), kpts=(8,8,8))),
    "cspbi3_v2":   ("rattled_cspbi3_v2.xyz", dict(mode=PW(600), kpts=(6,6,6))),
    "si_check600": ("rattled_si.xyz",        dict(mode=PW(600), kpts=(8,8,8))),
}
for name, (fname, s) in jobs.items():
    at = read(fname)
    at.calc = GPAW(xc='PBE', txt=f"forces_{name}_gpaw.log", **s)
    f = at.get_forces()
    np.save(f"forces_{name}_gpaw.npy", f)
    print(name, "GPAW max|F| =", round(float(abs(f).max()), 4), "eV/A")
