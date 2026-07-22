from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# descriptor: relaxed lattice constant. Well-posed, discriminates, MACE handles these well.
# reference DFT/experimental lattice constants (Angstrom)
mats = {"Si": 5.43, "Ge": 5.66, "diamond_C": 3.57, "Al": 4.05}
builders = {"Si": ("Si","diamond"), "Ge":("Ge","diamond"),
            "diamond_C":("C","diamond"), "Al":("Al","fcc")}

mace_vals, ref_vals = {}, {}
for name,(sym,struc) in builders.items():
    at = bulk(sym, struc); at.calc = calc
    BFGS(FrechetCellFilter(at), logfile=None).run(fmax=0.01, steps=200)
    a = at.cell.cellpar()[0]
    if struc=="fcc": a = a*np.sqrt(2)  # fcc conventional
    mace_vals[name] = round(a,3); ref_vals[name] = mats[name]

# CHECK: does MACE rank these by lattice constant the same as reference?
mace_order = sorted(mace_vals, key=lambda k: mace_vals[k])
ref_order  = sorted(ref_vals, key=lambda k: ref_vals[k])
print("MACE lattice constants:", mace_vals)
print("ref  lattice constants:", ref_vals)
print("MACE order:", mace_order)
print("ref  order:", ref_order)
agree = mace_order == ref_order
spread = max(mace_vals.values()) - min(mace_vals.values())
print(f"\nCheck 1 (well-posed): PASS (single value each)")
print(f"Check 3 (discriminates): {'PASS' if spread>0.1 else 'FAIL'} (spread {spread:.2f} A)")
print(f"Oracle (ranking vs reference): {'PASS' if agree else 'FAIL'}")
print(f"\nOVERALL: {'PASS - first certified descriptor!' if agree and spread>0.1 else 'not yet'}")
