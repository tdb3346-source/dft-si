from ase.spacegroup import crystal
from ase.io import read, write
from ase.mep import NEB
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

# CsPbCl3 cubic - lattice ~5.6 A (smaller than Br's 5.87)
unit = crystal(['Cs','Pb','Cl'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
               spacegroup=221, cellpar=[5.6]*3 + [90]*3)
sc = unit.repeat((2,2,2))
sc.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(FrechetCellFilter(sc)).run(fmax=0.02, steps=200)
a0 = sc.get_cell().cellpar()[0] / 2
print(f"CsPbCl3 MACE a0 = {a0:.4f} A", flush=True)
write("cspbcl3_relaxed.xyz", sc)

Cl = [a.index for a in sc if a.symbol == 'Cl']
vac = sc.copy(); del vac[Cl[0]]
vac.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(vac, logfile='cl_init.log').run(fmax=0.02, steps=200)
write("cl_init.xyz", vac)

for i in [a.index for a in sc if a.symbol == 'Cl']:
    if np.linalg.norm(vac.get_positions() - sc.positions[i], axis=1).min() > 1.0:
        hole = sc.positions[i]; break
Ci = [a.index for a in vac if a.symbol == 'Cl']
hop = Ci[int(np.linalg.norm(vac.get_positions()[Ci] - hole, axis=1).argmin())]
fin = vac.copy(); fin.positions[hop] = hole
dmin = fin.get_distances(hop, [j for j in range(len(fin)) if j != hop], mic=True).min()
print(f"structure check {dmin:.3f} A", flush=True)
if dmin < 2.0:
    print("REJECTED"); raise SystemExit
fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='cl_fin.log').run(fmax=0.02, steps=200)
diff = fin.get_potential_energy() - vac.get_potential_energy()
print(f"endpoint diff {diff:+.4f} eV", flush=True)
if abs(diff) > 0.05:
    print("GATE FAILED"); raise SystemExit
write("cl_fin.xyz", fin)

imgs = [vac] + [vac.copy() for _ in range(9)] + [fin]
for im in imgs:
    im.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
neb = NEB(imgs, climb=True, method='improvedtangent')
neb.interpolate()
BFGS(neb, logfile='cl_neb.log', trajectory='cl_neb.traj').run(fmax=0.05, steps=300)
E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
print(f"CsPbCl3 MACE energies {np.round(E,3)}", flush=True)
print(f"CsPbCl3 MACE BARRIER {E.max():.3f} eV at image {int(E.argmax())}", flush=True)
