from ase.io import read
import numpy as np
from gpaw import GPAW, PW

settings = {
    "si":     dict(mode=PW(500), kpts=(8, 8, 8)),   # EDIT if si_dft.ipynb grep says otherwise
    "sto":    dict(mode=PW(900), kpts=(6, 6, 6)),
    "cspbi3": dict(mode=PW(600), kpts=(6, 6, 6)),
}
for name, s in settings.items():
    at = read(f"rattled_{name}.xyz")
    at.calc = GPAW(xc='PBE', txt=f"forces_{name}_gpaw.log", **s)
    f = at.get_forces()
    np.save(f"forces_{name}_gpaw.npy", f)
    print(name, "GPAW max|F| =", round(float(abs(f).max()), 4), "eV/A")
