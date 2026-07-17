from ase.io import read, write
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
cell = pris.get_cell()

for eps, tag in [(-0.02, "comp2"), (+0.02, "tens2")]:
    at = pris.copy()
    c = cell.copy()
    c[2] = c[2] * (1 + eps)              # strain along z only
    at.set_cell(c, scale_atoms=True)
    # remove one iodine that sits in the strained direction
    I_idx = [a.index for a in at if a.symbol == 'I']
    del at[I_idx[0]]
    write(f"vac_{tag}.xyz", at)
    print(f"{tag}: c-axis {cell[2][2]:.3f} -> {c[2][2]:.3f} A ({eps*100:+.0f}%), {len(at)} atoms")
