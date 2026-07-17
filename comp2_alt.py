from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
cell = pris.get_cell().copy()
cell[2] = cell[2] * 0.98

for pick in [4, 8, 12]:                     # three different iodines
    at = pris.copy()
    at.set_cell(cell, scale_atoms=True)
    I_idx = [a.index for a in at if a.symbol == 'I']
    del at[I_idx[pick]]
    at.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(at, logfile=f'alt{pick}_init.log').run(fmax=0.02, steps=200)

    p2 = pris.copy(); p2.set_cell(cell, scale_atoms=True)
    for i in [a.index for a in p2 if a.symbol == 'I']:
        if np.linalg.norm(at.get_positions() - p2.positions[i], axis=1).min() > 1.0:
            hole = p2.positions[i]; break
    Ii = [a.index for a in at if a.symbol == 'I']
    hopper = Ii[int(np.linalg.norm(at.get_positions()[Ii] - hole, axis=1).argmin())]

    fin = at.copy(); fin.positions[hopper] = hole
    dmin = fin.get_distances(hopper, [j for j in range(len(fin)) if j != hopper], mic=True).min()
    if dmin < 2.0:
        print(f"pick {pick}: structure reject ({dmin:.2f} A)", flush=True); continue
    fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(fin, logfile=f'alt{pick}_fin.log').run(fmax=0.02, steps=200)
    diff = fin.get_potential_energy() - at.get_potential_energy()
    print(f"pick {pick}: endpoint diff = {diff:+.4f} eV", flush=True)
