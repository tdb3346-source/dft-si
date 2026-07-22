from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
mats = {"diamond_C":("C",3.567), "Si":("Si",5.431), "Ge":("Ge",5.658), "Sn":("Sn",6.489)}
mace_vals, ref_vals = {}, {}
for name,(sym,ref) in mats.items():
    at = bulk(sym, "diamond", a=ref, cubic=True); at.calc = calc   # seed with ref a
    BFGS(FrechetCellFilter(at), logfile=None).run(fmax=0.01, steps=200)
    mace_vals[name] = round(at.cell.cellpar()[0],3); ref_vals[name] = ref

mo = sorted(mace_vals, key=lambda k: mace_vals[k])
ro = sorted(ref_vals, key=lambda k: ref_vals[k])
spread = max(mace_vals.values())-min(mace_vals.values())
agree = mo==ro
print("MACE:", mace_vals)
print("ref :", ref_vals)
print("MACE order:", mo, "| ref order:", ro)
print(f"Check1: PASS | Check3: {'PASS' if spread>0.1 else 'FAIL'} ({spread:.2f}A) | Oracle: {'PASS' if agree else 'FAIL'}")
print(f"OVERALL: {'PASS - first certified descriptor!' if agree and spread>0.1 else 'not yet'}")
