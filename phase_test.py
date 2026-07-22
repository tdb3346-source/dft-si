from ase.spacegroup import crystal
from ase.io import write
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np, time

def mk(): return mace_mp(model="medium", default_dtype="float64", device="cpu")

def build(subs, yellow=False, a=6.39):
    u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
                spacegroup=221, cellpar=[a]*3+[90]*3)
    at = u.repeat((2,2,2))
    if yellow:
        c = at.get_cell().copy(); c[0]*=0.90; c[1]*=1.15; c[2]*=0.95
        at.set_cell(c, scale_atoms=True)
        at.positions += np.random.default_rng(0).normal(scale=0.30, size=at.positions.shape)
    for frm,to,n in subs:
        idx=[x.index for x in at if x.symbol==frm][:n]
        for i in idx: at[i].symbol=to
    return at

def relax(at):
    at.calc = mk()
    BFGS(FrechetCellFilter(at), logfile=None).run(fmax=0.03, steps=300)
    return at.get_potential_energy()/8   # per formula unit

CANDS = {"base":[], "br":[('I','Br',6)], "rb":[('Cs','Rb',2)], "k":[('Cs','K',2)]}
res = {}
for tag, subs in CANDS.items():
    Eb = relax(build(subs, yellow=False))
    Ey = relax(build(subs, yellow=True))
    res[tag] = (Eb-Ey)*1000
    print(f"{tag}: dE(black-yellow) = {res[tag]:+.1f} meV/fu   {time.ctime()}", flush=True)

print("\nRANKING (more negative = black more stable = better):", flush=True)
for tag,d in sorted(res.items(), key=lambda x:x[1]):
    print(f"  {tag:5s} {d:+7.1f} meV/fu", flush=True)
v=np.array(list(res.values())); print(f"\nSPREAD = {v.max()-v.min():.1f} meV/fu", flush=True)
print("(<10 = does NOT discriminate; >20 = discriminates, descriptor usable)", flush=True)
print("NOTE: yellow phase is APPROXIMATED (same recipe all 4) - this is a SCREEN-VALIDITY test, not final numbers", flush=True)
