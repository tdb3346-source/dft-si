from ase.spacegroup import crystal
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from mace.calculators import mace_mp

atoms = crystal(['Sr', 'Ti', 'O'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5), (0.5, 0.5, 0)],
                spacegroup=221,
                cellpar=[3.94, 3.94, 3.94, 90, 90, 90])
atoms.calc = mace_mp(model="medium", default_dtype="float64", device="cpu")
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
print(atoms.cell.cellpar())
