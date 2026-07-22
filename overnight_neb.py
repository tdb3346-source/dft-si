from ase.io import read
from ase.mep import NEB
from ase.optimize import BFGS
from gpaw import GPAW, PW
import numpy as np, time

def gpaw_neb(tag, init_file, fin_file):
    print("=====", tag, "starting", time.ctime(), flush=True)
    initial = read(init_file); final = read(fin_file)
    images = [initial] + [initial.copy() for _ in range(5)] + [final]
    for im in images:
        im.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', txt=tag+'_gpawneb.log')
    neb = NEB(images, climb=True, method='improvedtangent')
    neb.interpolate()
    opt = BFGS(neb, logfile=tag+'_gpawneb_bfgs.log', trajectory=tag+'_gpawneb.traj')
    try:
        opt.run(fmax=0.10, steps=40)
    except Exception as e:
        print(tag, "stopped", e, flush=True)
    E = np.array([im.get_potential_energy() for im in images]); E -= E[0]
    print(tag, "energies", np.round(E,3), flush=True)
    print(tag, "BARRIER", round(float(E.max()),3), "eV image", int(E.argmax()), time.ctime(), flush=True)
    return float(E.max())

r = {}
r['Cl'] = gpaw_neb("cl", "cl_init.xyz", "cl_fin.xyz")
r['Br'] = gpaw_neb("br", "br_init.xyz", "br_fin.xyz")
r['I']  = gpaw_neb("i", "cspbi3_vac_222_relaxed.xyz", "cspbi3_vac_final_relaxed.xyz")
print("===== FINAL own-path barriers", flush=True)
print("I", round(r['I'],3), "Br", round(r['Br'],3), "Cl", round(r['Cl'],3), flush=True)
print("vs single-point-on-MACE-path: I 0.108 Br 0.126 Cl 0.188", flush=True)
