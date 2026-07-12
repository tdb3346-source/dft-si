from ase.build import bulk
from ase.spacegroup import crystal
from ase.io import write

si = bulk("Si", "diamond", a=5.476, cubic=True)
sto = crystal(['Sr','Ti','O'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
              spacegroup=221, cellpar=[3.9441]*3 + [90]*3)
csp = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
              spacegroup=221, cellpar=[6.390]*3 + [90]*3)
for name, at in [("si", si), ("sto", sto), ("cspbi3", csp)]:
    at.rattle(stdev=0.05, seed=42)
    write(f"rattled_{name}.xyz", at)
    print(name, len(at), "atoms rattled, written")
