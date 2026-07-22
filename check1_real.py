from ase.spacegroup import crystal
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

def mk(): return mace_mp(model="medium", default_dtype="float64", device="cpu")

def build_vac(subs, a=6.39):
    u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
                spacegroup=221, cellpar=[a]*3+[90]*3)
    at = u.repeat((2,2,2))
    for frm,to,n in subs:
        for i in [x.index for x in at if x.symbol==frm][:n]: at[i].symbol=to
    full = at.copy()
    I = [x.index for x in at if x.symbol=='I']
    vac = at.copy(); hole = vac.positions[I[0]].copy(); del vac[I[0]]
    return full, vac, hole

def wellposed(subs, tol=0.10):
    """Returns endpoint diff (eV). |diff|<tol = well-defined hop. None = broke."""
    full, vac, hole = build_vac(subs)
    vac.calc = mk(); BFGS(vac, logfile=None).run(fmax=0.03, steps=200)
    I = [x.index for x in vac if x.symbol=='I']
    hop = I[int(np.linalg.norm(vac.get_positions()[I]-hole,axis=1).argmin())]
    fin = vac.copy(); fin.positions[hop]=hole
    dmin = fin.get_distances(hop,[j for j in range(len(fin)) if j!=hop],mic=True).min()
    if dmin < 2.0: return None
    fin.calc = mk(); BFGS(fin, logfile=None).run(fmax=0.03, steps=200)
    return fin.get_potential_energy() - vac.get_potential_energy()

CANDS = {"base":[], "br":[('I','Br',6)], "rb":[('Cs','Rb',2)], "k":[('Cs','K',2)]}
n_bad = 0
for tag, subs in CANDS.items():
    d = wellposed(subs)
    ok = d is not None and abs(d) < 0.10
    if not ok: n_bad += 1
    print(f"{tag}: diff={d if d is None else round(d,3)}  {'well-posed' if ok else 'ILL-POSED'}", flush=True)
print(f"\nCHECK 1: {n_bad}/4 ill-posed -> {'FAIL' if n_bad/4>0.25 else 'PASS'}", flush=True)
