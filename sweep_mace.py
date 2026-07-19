from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

pris = read("cspbi3_pristine_222.xyz")
cell0 = pris.get_cell().copy()

for eps, tag in [(0.0067, "s067"), (0.0133, "s133")]:
    at = pris.copy()
    c = cell0.copy(); c[2] = c[2] * (1 + eps)
    at.set_cell(c, scale_atoms=True)
    I_idx = [a.index for a in at if a.symbol == 'I']
    del at[I_idx[0]]
    at.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(at, logfile=f'{tag}_i.log').run(fmax=0.02, steps=200)
    write(f"{tag}_init.xyz", at)

    p2 = pris.copy(); p2.set_cell(c, scale_atoms=True)
    for i in [a.index for a in p2 if a.symbol == 'I']:
        if np.linalg.norm(at.get_positions() - p2.positions[i], axis=1).min() > 1.0:
            hole = p2.positions[i]; break
    Ii = [a.index for a in at if a.symbol == 'I']
    hop = Ii[int(np.linalg.norm(at.get_positions()[Ii] - hole, axis=1).argmin())]
    fin = at.copy(); fin.positions[hop] = hole
    dmin = fin.get_distances(hop, [j for j in range(len(fin)) if j != hop], mic=True).min()
    print(f"{tag}: structure check {dmin:.3f} A", flush=True)
    if dmin < 2.0:
        print(f"{tag}: REJECTED"); continue
    fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(fin, logfile=f'{tag}_f.log').run(fmax=0.02, steps=200)
    diff = fin.get_potential_energy() - at.get_potential_energy()
    print(f"{tag}: endpoint diff {diff:+.4f} eV", flush=True)
    if abs(diff) > 0.10:
        print(f"{tag}: GATE FAILED"); continue

    imgs = [at] + [at.copy() for _ in range(9)] + [fin]
    for im in imgs:
        im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    neb = NEB(imgs, climb=True, method='improvedtangent')
    neb.interpolate()
    BFGS(neb, logfile=f'{tag}_neb.log', trajectory=f'{tag}_neb.traj').run(fmax=0.05, steps=300)
    E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
    print(f"{tag}: MACE energies {np.round(E,3)}", flush=True)
    print(f"{tag}: MACE BARRIER {E.max():.3f} eV at image {int(E.argmax())}", flush=True)
