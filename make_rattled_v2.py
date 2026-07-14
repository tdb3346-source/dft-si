from ase.build import bulk
from ase.spacegroup import crystal
from ase.io import write

si = bulk("Si", "diamond", a=5.476, cubic=True)
csp = crystal(['Cs','Pb','I'], basis=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0)],
              spacegroup=221, cellpar=[6.390]*3 + [90]*3)
for name, at, amp in [("si", si, 0.02), ("cspbi3", csp, 0.20)]:
    at.rattle(stdev=amp, seed=43)
    write(f"rattled_{name}_v2.xyz", at)
    print(name, "rattled at", amp, "A, written")
