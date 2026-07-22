from ase.io import read
from ase.mep import NEB
from ase.optimize import BFGS
from mace.calculators import MACECalculator, mace_mp
import numpy as np

# get the model file path once, then build independent calculators from it
_probe = mace_mp(model="medium", default_dtype="float64", device="cpu")
MODEL = _probe.parameters.get('model_paths', None) if hasattr(_probe,'parameters') else None

def fresh():
    # independent MACE calculator each call
    return mace_mp(model="medium", default_dtype="float64", device="cpu", return_raw_model=False)

def barrier(tag):
    full = read(f"candfull_{tag}.xyz")
    vac  = read(f"cand_{tag}.xyz")
    vac.calc = fresh()
    BFGS(vac, logfile=f'rank_{tag}_i.log').run(fmax=0.02, steps=200)
    hole = None
    for i in [a.index for a in full if a.symbol == 'I']:
        if np.linalg.norm(vac.get_positions() - full.positions[i], axis=1).min() > 1.0:
            hole = full.positions[i]; break
    Ii = [a.index for a in vac if a.symbol == 'I']
    hop = Ii[int(np.linalg.norm(vac.get_positions()[Ii] - hole, axis=1).argmin())]
    fin = vac.copy(); fin.positions[hop] = hole
    dmin = fin.get_distances(hop, [j for j in range(len(fin)) if j != hop], mic=True).min()
    if dmin < 2.0:
        print(f"{tag}: STRUCTURE REJECT {dmin:.2f}", flush=True); return None
    fin.calc = fresh()
    BFGS(fin, logfile=f'rank_{tag}_f.log').run(fmax=0.02, steps=200)
    diff = fin.get_potential_energy() - vac.get_potential_energy()
    if abs(diff) > 0.10:
        print(f"{tag}: ENDPOINT GATE FAIL {diff:+.3f}", flush=True); return None
    imgs = [vac] + [vac.copy() for _ in range(9)] + [fin]
    for im in imgs: im.calc = fresh()
    neb = NEB(imgs, climb=True, method='improvedtangent', allow_shared_calculator=True)
    neb.interpolate()
    BFGS(neb, logfile=f'rank_{tag}_neb.log', trajectory=f'rank_{tag}_neb.traj').run(fmax=0.05, steps=300)
    E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
    b = float(E.max())
    print(f"{tag}: MACE barrier {b:.3f} eV (endpoint diff {diff:+.3f})", flush=True)
    return b

res = {}
for tag in ["base", "br", "rb", "k"]:
    try:
        res[tag] = barrier(tag)
    except Exception as e:
        print(f"{tag}: ERROR {e}", flush=True); res[tag] = None
print("RANKING:", flush=True)
ok = {k: v for k, v in res.items() if v is not None}
for tag, b in sorted(ok.items(), key=lambda x: x[1]):
    print(f"  {tag}: {b:.3f} eV", flush=True)
