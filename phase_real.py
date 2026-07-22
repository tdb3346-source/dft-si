from ase.spacegroup import crystal
from ase.io import read
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from mace.calculators import mace_mp
import numpy as np

calc = mace_mp(model="medium", default_dtype="float64", device="cpu")

# black (cubic perovskite), relaxed
u = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
            spacegroup=221, cellpar=[6.39]*3+[90]*3)
black = u.repeat((1,1,1)); black.calc = calc
BFGS(FrechetCellFilter(black), logfile=None).run(fmax=0.03, steps=300)
Eb = black.get_potential_energy()/1   # 1 f.u. in unit cell
fb = float(np.abs(black.get_forces()).max())

yellow = read("delta_cspbi3_real.xyz"); yellow.calc = calc
Ey = yellow.get_potential_energy()/(len(yellow)//5)
fy = float(np.abs(yellow.get_forces()).max())

dE = (Eb - Ey)*1000
print(f"E_black/fu = {Eb:.4f}  (max|F| {fb:.3f})")
print(f"E_yellow/fu = {Ey:.4f}  (max|F| {fy:.3f})")
print(f"dE(black-yellow) = {dE:+.1f} meV/fu")
print("negative = black more stable | positive = yellow more stable (the rot)")
