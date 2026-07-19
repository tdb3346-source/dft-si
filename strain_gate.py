from ase.io import read
import numpy as np
from gpaw import GPAW, PW
from mace.calculators import mace_mp

base = read("cspbi3_vac_222_relaxed.xyz")
cell0 = base.get_cell().copy()
strains = [0.0, 0.0025, 0.005, 0.0075, 0.010, 0.0125, 0.015, 0.0175, 0.020]
mace = mace_mp(model="medium", default_dtype="float64", device="cpu")
rows = []
for eps in strains:
    at = base.copy()
    c = cell0.copy(); c[2] = c[2] * (1 + eps)
    at.set_cell(c, scale_atoms=True)          # fractional coords fixed
    at.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=f'gate_{eps:.4f}.log')
    eg = at.get_potential_energy(); fg = at.get_forces()
    at2 = at.copy(); at2.calc = mace
    em = at2.get_potential_energy(); fm = at2.get_forces()
    d = fm - fg
    per_atom = np.linalg.norm(d, axis=1)
    worst = int(per_atom.argmax())
    rows.append((eps, eg, em, fg, fm))
    np.save(f"gate_forces_{eps:.4f}.npy", np.stack([fg, fm]))
    print(f"eps={eps*100:.2f}%  dE/atom={1000*(em-eg)/len(at):+.2f} meV  "
          f"Frmse={np.sqrt((d**2).mean()):.4f}  Fmax_err={per_atom.max():.4f}  "
          f"worst_atom={worst}({at[worst].symbol})", flush=True)
E0g = rows[0][1]; E0m = rows[0][2]
print("\n--- relative to 0% structure ---")
for eps, eg, em, _, _ in rows:
    print(f"eps={eps*100:.2f}%  dE_gpaw={eg-E0g:+.4f}  dE_mace={em-E0m:+.4f}  diff={((em-E0m)-(eg-E0g))*1000:+.1f} meV", flush=True)
