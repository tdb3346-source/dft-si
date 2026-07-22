from ase.io import read
import numpy as np
imgs = read("ob.traj", index="-7:")
E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
print("partial iodide GPAW-own-path energies:", np.round(E,3))
print("partial barrier (unconverged):", round(float(E.max()),3), "eV")
print("compare: single-point-on-MACE-path 0.108 | MACE 0.152")
