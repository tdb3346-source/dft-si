from ase.io import read, write
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
I_idx = [a.index for a in pris if a.symbol == 'I']
print("total iodine sites:", len(I_idx))

# three distinct sites: the one we did (0), and two others far from it
chosen = [I_idx[0], I_idx[8], I_idx[16]]
for n, idx in enumerate(chosen):
    at = pris.copy()
    del at[idx]
    write(f"vac_site{n}.xyz", at)
    d = np.linalg.norm(pris.positions[idx] - pris.positions[chosen[0]])
    print(f"site {n}: removed I idx {idx}, {len(at)} atoms, {d:.2f} A from site 0")
