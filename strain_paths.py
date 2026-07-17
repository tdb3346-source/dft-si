from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

def build(tag):
    at = read(f"vac_{tag}.xyz")
    at.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(at, logfile=f'{tag}_init.log').run(fmax=0.02, steps=200)
    write(f"{tag}_init.xyz", at)

    pris = read("cspbi3_pristine_222.xyz")
    # the hole = pristine I site with nothing near it
    for i in [a.index for a in pris if a.symbol == 'I']:
        if np.linalg.norm(at.get_positions() - pris.positions[i], axis=1).min() > 1.0:
            hole = pris.positions[i]; break
    I_idx = [a.index for a in at if a.symbol == 'I']
    hopper = I_idx[int(np.linalg.norm(at.get_positions()[I_idx] - hole, axis=1).argmin())]

    fin = at.copy(); fin.positions[hopper] = hole
    dmin = fin.get_distances(hopper, [j for j in range(len(fin)) if j != hopper], mic=True).min()
    print(f"{tag}: STRUCTURE CHECK nearest atom = {dmin:.3f} A", flush=True)
    if dmin < 2.0:
        print(f"{tag}: REJECTED"); return
    fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    BFGS(fin, logfile=f'{tag}_fin.log').run(fmax=0.02, steps=200)
    write(f"{tag}_fin.xyz", fin)
    diff = fin.get_potential_energy() - at.get_potential_energy()
    print(f"{tag}: endpoint diff = {diff:.4f} eV  (gate: |diff| < 0.05)", flush=True)
    if abs(diff) > 0.05:
        print(f"{tag}: GATE FAILED - endpoints not equivalent"); return

    imgs = [at] + [at.copy() for _ in range(9)] + [fin]
    for im in imgs:
        im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
    neb = NEB(imgs, climb=True, method='improvedtangent')
    neb.interpolate()
    BFGS(neb, logfile=f'{tag}_neb.log', trajectory=f'{tag}_neb.traj').run(fmax=0.05, steps=300)
    E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
    print(f"{tag}: MACE energies {np.round(E,3)}", flush=True)
    print(f"{tag}: MACE BARRIER = {E.max():.3f} eV at image {int(E.argmax())}", flush=True)

for tag in ["comp2", "tens2"]:
    print("=" * 40, tag, flush=True)
    build(tag)
