from ase.io import read
import numpy as np
from mace.calculators import mace_mp

strains = [0.0, 0.0025, 0.005, 0.0075, 0.010, 0.0125, 0.015, 0.0175, 0.020]
calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
rows = []
print(f"{'eps%':>6}{'dE/atom meV':>13}{'F_rmse':>9}{'F_max_err':>11}{'worst atom':>12}")
for eps in strains:
    at = read(f"gate_{eps:.4f}.xyz")
    eg = float(np.load(f"gate_E_{eps:.4f}.npy")[0])
    fg = np.load(f"gate_F_{eps:.4f}.npy")
    at.calc = calc
    em = at.get_potential_energy(); fm = at.get_forces()
    d = fm - fg
    per_atom = np.linalg.norm(d, axis=1)
    w = int(per_atom.argmax())
    rows.append((eps, eg, em, per_atom))
    print(f"{eps*100:6.2f}{1000*(em-eg)/len(at):13.2f}{np.sqrt((d**2).mean()):9.4f}"
          f"{per_atom.max():11.4f}{w:6d} ({at[w].symbol})")

print("\n--- energy CHANGE relative to the 0% structure (the real test) ---")
E0g, E0m = rows[0][1], rows[0][2]
for eps, eg, em, _ in rows:
    print(f"eps={eps*100:5.2f}%  dE_gpaw={eg-E0g:+.4f}  dE_mace={em-E0m:+.4f}  "
          f"error={((em-E0m)-(eg-E0g))*1000:+8.1f} meV")

print("\n--- per-atom force error localization (top 5 at max strain) ---")
at = read(f"gate_{strains[-1]:.4f}.xyz")
pa = rows[-1][3]
for i in np.argsort(pa)[-5:][::-1]:
    print(f"  atom {i:2d} ({at[i].symbol}): |dF| = {pa[i]:.4f} eV/A")
print(f"  median |dF| = {np.median(pa):.4f}  -> ratio worst/median = {pa.max()/np.median(pa):.1f}x")
