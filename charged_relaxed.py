from ase.io import read, write
from ase.optimize import BFGS
import numpy as np
from gpaw import GPAW, PW

imgs = read("neb_mace_11.traj", index="-11:")

end = imgs[0].copy()
end.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', charge=+1, txt='chg_end.log')
BFGS(end, logfile='chg_end_bfgs.log').run(fmax=0.03, steps=60)
Ee = end.get_potential_energy()
write("chg_end_relaxed.xyz", end)
print("endpoint relaxed (charge +1): E =", round(float(Ee), 4), flush=True)

pk = imgs[5].copy()
pk.calc = GPAW(mode=PW(600), kpts=(2,2,2), xc='PBE', charge=+1, txt='chg_peak.log')
BFGS(pk, logfile='chg_peak_bfgs.log').run(fmax=0.03, steps=60)
Ep = pk.get_potential_energy()
write("chg_peak_relaxed.xyz", pk)
print("peak relaxed (charge +1): E =", round(float(Ep), 4), flush=True)

print("RELAXED V_I+ BARRIER =", round(float(Ep - Ee), 3), "eV")
print("compare: frozen V_I+ 0.094 | frozen V_I0 0.108 | MACE 0.152")
print("Tao needs ~<=0.06 to explain 10x rate vs neutral")
