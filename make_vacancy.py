from ase.spacegroup import crystal
from ase.io import write

# pristine cubic CsPbI3, our adjudicated oracle lattice
unit = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
               spacegroup=221, cellpar=[6.390]*3 + [90]*3)
sc = unit.repeat((2,2,2))
write("cspbi3_pristine_222.xyz", sc)
print("pristine:", len(sc), "atoms", sc.get_chemical_formula())

# remove one iodine -> the vacancy
idx = [a.index for a in sc if a.symbol == 'I'][0]
sc_vac = sc.copy()
del sc_vac[idx]
write("cspbi3_vac_222.xyz", sc_vac)
print("vacancy:", len(sc_vac), "atoms", sc_vac.get_chemical_formula())
