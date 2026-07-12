from ase.spacegroup import crystal
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from gpaw import GPAW, PW

atoms = crystal(['Cs', 'Pb', 'I'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5), (0.5, 0.5, 0)],
                spacegroup=221,
                cellpar=[6.29, 6.29, 6.29, 90, 90, 90])
atoms.calc = GPAW(mode=PW(600), kpts=(4, 4, 4), xc='PBE', txt='cspbi3_relax_gpaw.log')
BFGS(FrechetCellFilter(atoms), logfile='cspbi3_relax_bfgs.log').run(fmax=0.01)
print("a0 =", atoms.cell.cellpar()[0])
