from ase.build import bulk
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from mace.calculators import mace_mp

atoms = bulk("Si", "diamond", a=5.43)
atoms.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
print("a0 =", atoms.cell.cellpar()[0])
