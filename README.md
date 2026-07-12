
## Phase 2: oracle vs surrogate (MACE-MP medium, float64, CPU)
| material | property | my GPAW oracle | MACE-MP | delta vs oracle | oracle vs expt |
|---|---|---|---|---|---|
| Si | a0 (A) | 5.476 | 5.4551 | -0.38% | +0.83% |
| SrTiO3 | a0 (A) | 3.9441 | 3.9429 | -0.03% | +1.00% |
| CsPbI3 | a0 (A) | 6.390 | 6.3903 | +0.005% | +1.59% |
| all | bandgap | oracle-only | n/a | n/a | out of MLIP scope by construction |

Limitation (documented): equilibrium-lattice agreement says nothing about off-equilibrium honesty
(forces, phase ordering, barriers). That is the next test, and the P4 Phase 2 benchmark.

### Force check (0.05 A rattle, seed 42; GPAW reference at oracle settings)
| material | RMS F_gpaw (eV/A) | RMSE (eV/A) | rel % | note |
|---|---|---|---|---|
| Si | 0.785 | 0.315 | 40.1 | uniform rattle = violent for stiff Si; OOD suspect, matched-severity test queued |
| SrTiO3 | 0.368 | 0.027 | 7.4 | sweet spot |
| CsPbI3 | 0.049 | 0.0118 | 24.3 | best absolute, worst-but-one relative: noise floor vs tiny forces |

Adjudication note: CsPbI3 oracle 6.390 confirmed by two independent runs (k 6x6x6, cutoffs 600/refit; k 4x4x4 rejected at +0.21% - k-point convergence, not cutoff).
Headline limitation (documented): equilibrium-lattice agreement does not certify forces - same crystal shows +0.003% on a0 and 24.3% relative force error. Off-equilibrium honesty is the P4 Phase 2 benchmark, opening experiment pre-registered in LOG.md.
