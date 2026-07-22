from ase.io import read
from ase.mep import NEB
from ase.optimize import BFGS
from gpaw import GPAW, PW
import numpy as np, time

# Referee-proof iodide barrier: GPAW's OWN NEB path, 7 images, generous step cap.
# Uses the already-relaxed vacancy endpoints from earlier work.
print("start", time.ctime(), flush=True)
initial = read("cspbi3_vac_222_relaxed.xyz")
final = read("cspbi3_vac_final_relaxed.xyz")
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for im in images:
    im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt='ob_gpaw.log')
neb = NEB(images, climb=True, method='improvedtangent', allow_shared_calculator=True)
neb.interpolate()
opt = BFGS(neb, logfile='ob_bfgs.log', trajectory='ob.traj')
try:
    opt.run(fmax=0.05, steps=80)
except Exception as e:
    print("stopped", e, flush=True)
E = np.array([im.get_potential_energy() for im in images]); E -= E[0]
print("energies", np.round(E,3), flush=True)
print("GPAW OWN-PATH IODIDE BARRIER =", round(float(E.max()),3), "eV", time.ctime(), flush=True)
print("compare: single-point-on-MACE-path gave 0.108 | MACE 0.152", flush=True)
