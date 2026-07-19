from ase.io import read, write
import numpy as np
from gpaw import GPAW, PW

base = read("cspbi3_vac_222_relaxed.xyz")
cell0 = base.get_cell().copy()
strains = [0.0, 0.0025, 0.005, 0.0075, 0.010, 0.0125, 0.015, 0.0175, 0.020]
for eps in strains:
    at = base.copy()
    c = cell0.copy(); c[2] = c[2] * (1 + eps)
    at.set_cell(c, scale_atoms=True)
    write(f"gate_{eps:.4f}.xyz", at)
    at.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'gate_{eps:.4f}.log')
    e = at.get_potential_energy(); f = at.get_forces()
    np.save(f"gate_E_{eps:.4f}.npy", np.array([e]))
    np.save(f"gate_F_{eps:.4f}.npy", f)
    print(f"eps={eps*100:.2f}%  E={e:.4f} eV  max|F|={abs(f).max():.4f}", flush=True)
print("GPAW half done", flush=True)
