from ase.io import read
import numpy as np
from mace.calculators import mace_mp

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
print(f"{'mat':12s}{'RMS_F':>10s}{'RMSE':>10s}{'rel%':>8s}")
for name, xyz, npy in [("si_v2","rattled_si_v2.xyz","forces_si_v2_gpaw.npy"),
                       ("sto","rattled_sto.xyz","forces_sto_gpaw.npy"),
                       ("cspbi3_v2","rattled_cspbi3_v2.xyz","forces_cspbi3_v2_gpaw.npy")]:
    at = read(xyz); at.calc = calc
    fg = np.load(npy); d = at.get_forces() - fg
    rmse = np.sqrt((d**2).mean()); rms = np.sqrt((fg**2).mean())
    print(f"{name:12s}{rms:10.4f}{rmse:10.4f}{100*rmse/rms:8.1f}")
f500 = np.load("forces_si_gpaw.npy"); f600 = np.load("forces_si_check600_gpaw.npy")
d = f600 - f500; n = np.sqrt((d**2).mean())
print("GPAW self-noise, Si (PW500 vs 600): RMSE =", round(float(n),4),
      "eV/A =", round(100*float(n)/float(np.sqrt((f500**2).mean())),1), "% of RMS_F")
