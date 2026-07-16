from ase.io import read, write
from ase.optimize import BFGS
from mace.calculators import mace_mp
import numpy as np

# start from the GPAW-relaxed vacancy, but re-relax it in MACE's own landscape
init = read("cspbi3_vac_222_relaxed.xyz")
init.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(init, logfile='init_mace_relax.log').run(fmax=0.02)
write("vac_init_mace.xyz", init)
Ei = init.get_potential_energy()

fin = read("cspbi3_vac_final_relaxed.xyz")
fin.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(fin, logfile='fin_mace_relax.log').run(fmax=0.02)
write("vac_fin_mace.xyz", fin)
Ef = fin.get_potential_energy()

print("E(init, MACE-relaxed) =", round(float(Ei), 4))
print("E(fin,  MACE-relaxed) =", round(float(Ef), 4))
print("difference =", round(float(Ef - Ei), 4), "eV")
print("KILL-CHECK: both endpoints now relaxed in the SAME engine; |diff| should be < 0.02 eV")
