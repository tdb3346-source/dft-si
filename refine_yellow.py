from ase.spacegroup import crystal
from ase.io import read, write
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# BLACK: relax cubic fully incl. cell
u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
            spacegroup=221, cellpar=[6.39]*3+[90]*3)
black = u.repeat((2,2,2)); black.calc = calc
BFGS(FrechetCellFilter(black), logfile=None).run(fmax=0.02, steps=400)
Eb = black.get_potential_energy()/8
print(f"E_black/fu = {Eb:.4f}", flush=True)

# YELLOW: re-relax the delta cell more tightly
y = read("delta_cspbi3_real.xyz"); y.calc = calc
BFGS(FrechetCellFilter(y), logfile=None).run(fmax=0.02, steps=400)
Ey = y.get_potential_energy()/(len(y)//5)
write("delta_cspbi3_real.xyz", y)
print(f"E_yellow/fu = {Ey:.4f}", flush=True)

dE = (Eb-Ey)*1000
print(f"dE(black-yellow) = {dE:+.1f} meV/fu  (target: +20 to +100)", flush=True)
print("VERDICT:", "PASS - in range!" if 20<=abs(dE)<=100 else f"still off - {abs(dE):.0f} meV", flush=True)
