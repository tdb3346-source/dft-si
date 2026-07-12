from ase.spacegroup import crystal
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from gpaw import GPAW, PW

atoms = crystal(['Sr', 'Ti', 'O'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5), (0.5, 0.5, 0)],
                spacegroup=221,
                cellpar=[3.905, 3.905, 3.905, 90, 90, 90])
atoms.calc = GPAW(mode=PW(900), kpts=(6, 6, 6), xc='PBE', txt='sto_relax_gpaw.log')
BFGS(FrechetCellFilter(atoms), logfile='sto_relax_bfgs.log').run(fmax=0.01)
print("a0 =", atoms.cell.cellpar()[0])
