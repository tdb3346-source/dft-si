import sys
from ase.spacegroup import crystal
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from mace.calculators import mace_mp

a = float(sys.argv[1])
atoms = crystal(['Cs', 'Pb', 'I'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5), (0.5, 0.5, 0)],
                spacegroup=221,
                cellpar=[a, a, a, 90, 90, 90])
atoms.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
print(atoms.cell.cellpar())
