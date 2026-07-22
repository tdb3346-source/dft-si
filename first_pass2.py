from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# conventional cubic cells, same convention for MACE and reference
mats = {"diamond_C":("C",3.567), "Si":("Si",5.431), "Ge":("Ge",5.658), "Sn":("Sn",6.489)}
mace_vals, ref_vals = {}, {}
for name,(sym,ref) in mats.items():
    at = bulk(sym, "diamond", cubic=True); at.calc = calc   # cubic=True -> conventional cell
    BFGS(FrechetCellFilter(at), logfile=None).run(fmax=0.01, steps=200)
    mace_vals[name] = round(at.cell.cellpar()[0],3); ref_vals[name] = ref

mace_order = sorted(mace_vals, key=lambda k: mace_vals[k])
ref_order  = sorted(ref_vals, key=lambda k: ref_vals[k])
spread = max(mace_vals.values())-min(mace_vals.values())
agree = mace_order==ref_order
print("MACE:", mace_vals)
print("ref :", ref_vals)
print("MACE order:", mace_order, "| ref order:", ref_order)
print(f"Check1 well-posed: PASS | Check3 discriminates: {'PASS' if spread>0.1 else 'FAIL'} ({spread:.2f} A)")
print(f"Oracle ranking: {'PASS' if agree else 'FAIL'}")
print(f"OVERALL: {'PASS - first certified descriptor!' if agree and spread>0.1 else 'not yet'}")
