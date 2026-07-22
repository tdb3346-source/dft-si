from ase import Atoms
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.io import write, read
from ase.spacegroup import crystal
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# delta-CsPbI3, Pnma (#62), Trots & Myagkota 2008 refined
# a=10.4342 b=4.7905 c=17.7610 ; refined Wyckoff 4c positions (x,1/4,z)
y = crystal(['Cs','Pb','I','I','I'],
    basis=[(0.4834,0.25,0.6656),   # Cs
           (0.1667,0.25,0.4491),   # Pb
           (0.2942,0.25,0.3241),   # I1
           (0.4901,0.25,0.0410),   # I2
           (0.0142,0.25,0.3818)],  # I3
    spacegroup=62, cellpar=[10.4342,4.7905,17.7610,90,90,90])
print("delta built:", y.get_chemical_formula(), len(y), "atoms", flush=True)

y.calc = calc
print("before max|F|:", round(float(np.abs(y.get_forces()).max()),3), flush=True)
BFGS(FrechetCellFilter(y), logfile=None).run(fmax=0.03, steps=400)
print("after max|F|:", round(float(np.abs(y.get_forces()).max()),3), flush=True)
Ey = y.get_potential_energy()/(len(y)//5)
write("delta_cspbi3_real.xyz", y)

# black, relaxed
u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
            spacegroup=221, cellpar=[6.39]*3+[90]*3)
b = u.repeat((2,2,2)); b.calc = calc
BFGS(FrechetCellFilter(b), logfile=None).run(fmax=0.03, steps=400)
Eb = b.get_potential_energy()/8

dE = (Eb-Ey)*1000
print(f"E_black/fu={Eb:.4f}  E_yellow/fu={Ey:.4f}", flush=True)
print(f"dE(black-yellow) = {dE:+.1f} meV/fu  (target +20 to +100)", flush=True)
print("VERDICT:", "PASS!" if 20<=abs(dE)<=100 else f"still off - {abs(dE):.0f} meV", flush=True)
