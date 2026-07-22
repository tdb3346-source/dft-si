from ase.io import read
import numpy as np

imgs = read("cl_gpawneb.traj", index="-7:")
E = np.array([im.get_potential_energy() for im in imgs]); E -= E[0]
print("partial Cl GPAW-own-path energies:", np.round(E, 3))
print("partial Cl barrier (unconverged, 16 steps):", round(float(E.max()), 3), "eV")
print("vs: single-point-on-MACE-path 0.188 | MACE 0.108")
