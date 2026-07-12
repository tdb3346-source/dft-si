Pre-run, Leg 3: MACE CsPbI3 within +/-2% of reference 6.290; direction bet: EXPANDS (PBE-family overshoot, third material); worst leg of three: |delta| > 0.4%.

## Leg 3 SCORED + session close (Jul 12, ~1:30 AM)
CsPbI3: MACE a0 = 6.39032, angles 90.000, fmax 0.0009. vs oracle 6.390 -> delta +0.005%. BEST leg, not worst.
Bets: direction HIT, +/-2% HIT, worst-leg (|delta|>0.4% vs oracle) MISS - both signatures.
Why: cubic CsPbI3 equilibrium is in the MP training set - graded the student on memorized homework. Halide softness lives off-equilibrium (rattled forces, alpha/delta ordering, barriers, finite-T), not in a 0-K volume relax.
REFILED bet: rattled-force RMSE ranks CsPbI3 worst of three. Test: force check (next session); full version: P4 Phase 2.
Table thesis: student-vs-professor (-0.38%, -0.03%, +0.005%) vs professor-vs-reality (+0.83%, +1.00%, +1.59%) - the student agrees best where the professor is most wrong. Fidelity to oracle != fidelity to nature, now measured.
Catch #12 (mentor, refinement): symmetric start -> symmetry-breaking forces zero by construction; this run could not reveal the instability. Angles-90 checked setup, not stability.
Note: absolute totals never compare across codes (MACE -14.179 vs GPAW -14.19 = coincidence of zeros).
Cross-check oracle (600 eV, 4x4x4): a0 = [fill from tail]

CORRECTION (catch #13, mentor - verdict logged before pending cross-check was read): cross-check oracle a0(600 eV, 4x4x4) = 6.3768 - does NOT confirm Jul-7 6.390. Spread 0.21% = ~40x the celebrated MACE delta. "BEST leg / +0.005%" SUSPENDED pending adjudication. Confounds between runs: k (6^3 vs 4^3), cutoff (Jul-7 refit cutoff unknown; 400 eV was ~80 meV unconverged per my own sweep), possibly method (refit may be E-V fit, not stress relax). Isolating run queued: identical to tonight's 600 eV run except kpts -> 6x6x6. NEW RULE: no verdict enters the ledger while a decisive run is pending. The "[fill from tail]" above = 6.3768.
Stakes: converged ~6.377 -> MACE delta ~+0.21%, ranking flips, halide bet partially revives. Converged ~6.390 -> tonight's 4^3 under-converged (k-point silent lie catches the cross-check itself).
Mentor bet: 600/6^3 lands within 0.05% of 6.3768 (k-density 25 A*k already adequate for a 1.7 eV insulator; suspicion falls on the Jul-7 refit's cutoff/method).
Pre-run, force check (refiled halide bet, both signatures): rattled-force RMSE ranks CsPbI3 WORST of three; quantitative: RMSE_CsPbI3 >= 2x RMSE_STO.
Catch #14 (mentor, pre-named): night shift launched from (mace) -> gpaw import failed, chain exited at step 1 in seconds. && chain worked as designed: zero partial state, zero compute lost. New habit: verify a launch actually started before walking away.
Si settings archaeology: converged = PW(400), k 6^3 (lattice) / 8^3 (gap). Force check uses PW(500)/8^3 - at or above converged; valid reference, provenance noted.

## ADJUDICATION scored (Jul 12 morning)
Oracle a0(600 eV, 6^3) = 6.39015. k=6^3 agrees across cutoffs to 0.002% (Jul-7 refit 6.390); k=4^3 off by 0.21% -> k-points were the lie, cutoff innocent. ORACLE CONFIRMED 6.390.
Mentor bet (within 0.05% of 6.3768): MISS by 4x. The Phase-0 k-point silent lie claimed the mentor's own cross-check; the Jul-7 solo oracle VINDICATED. Repo > everybody.
Leg 3 UN-SUSPENDED: MACE 6.39032 vs 6.39015 -> +0.003%. Best leg stands on a two-run oracle.
Softness measured: 0.05 A rattle -> max|F| Si 1.72 / STO 1.07 / CsPbI3 0.152 eV/A. ~10x weaker restoring force in the halide.
PRE-REGISTERED before compare: original absolute bet (RMSE_CsPbI3 >= 2x RMSE_STO) scored as written but flagged scale-confounded (soft -> small forces -> small abs errors; likely boring MISS). Meaningful metric registered blind: relative = RMSE/RMS(F_gpaw). Refined bet, both signatures: CsPbI3 WORST in relative error.

## FORCE VERDICT + Phase 2 ships (Jul 12)
Table: rel% = RMSE/RMS(F_gpaw): Si 40.1 (RMSE 0.315) | STO 7.4 (0.027) | CsPbI3 24.3 (0.0118).
Bet 1 (absolute, >=2x STO): MISS as pre-flagged - scale confound; CsPbI3 abs error 11.8 meV/A is SMALLEST, at/below published MACE-MP levels.
Bet 2 (relative, CsPbI3 worst, registered blind): MISS - Si worst at 40.1%. Session tally: 5 registered, 2 hit. Calibration gap on MLIP failure modes = the finding that justifies P4 Phase 2.
HEADLINE: CsPbI3 same crystal, same model: lattice +0.003% vs forces 24.3% rel - equilibrium fidelity != force fidelity, measured.
Si anomaly - design confound diagnosed: uniform 0.05 A rattle = non-uniform severity (Si shoved to 1.7 eV/A = OOD; CsPbI3 to 0.15 = in-distribution). Table ranks OOD distance, not chemistry. Hypothesis: error = noise floor (dominates CsPbI3's tiny forces) + OOD blowup (Si).
P4 PHASE 2 OPENER, pre-registered blind: matched-severity rattles (target RMS_F 0.3-0.4: Si ~0.02 A, STO 0.05, CsPbI3 ~0.2 A - also the 300K-relevant regime for the halide) + GPAW PW600 self-consistency point on Si. Prediction, both signatures: Si rel% < 15; CsPbI3 rel% > STO (halide bet, third filing, natural units).
Humility: N=1 snapshot/seed, 15-24 components; ordering robust, ratios +/-20%.

## FORCE VERDICT + Phase 2 ships (Jul 12)
Table: rel% = RMSE/RMS(F_gpaw): Si 40.1 (RMSE 0.315) | STO 7.4 (0.027) | CsPbI3 24.3 (0.0118).
Bet 1 (absolute, >=2x STO): MISS as pre-flagged - scale confound; CsPbI3 abs error 11.8 meV/A is SMALLEST, at/below published MACE-MP levels.
Bet 2 (relative, CsPbI3 worst, registered blind): MISS - Si worst at 40.1%. Session tally: 5 registered, 2 hit. Calibration gap on MLIP failure modes = the finding that justifies P4 Phase 2.
HEADLINE: CsPbI3 same crystal, same model: lattice +0.003% vs forces 24.3% rel - equilibrium fidelity != force fidelity, measured.
Si anomaly - design confound diagnosed: uniform 0.05 A rattle = non-uniform severity (Si shoved to 1.7 eV/A = OOD; CsPbI3 to 0.15 = in-distribution). Table ranks OOD distance, not chemistry. Hypothesis: error = noise floor (dominates CsPbI3's tiny forces) + OOD blowup (Si).
P4 PHASE 2 OPENER, pre-registered blind: matched-severity rattles (target RMS_F 0.3-0.4: Si ~0.02 A, STO 0.05, CsPbI3 ~0.2 A - also the 300K-relevant regime for the halide) + GPAW PW600 self-consistency point on Si. Prediction, both signatures: Si rel% < 15; CsPbI3 rel% > STO (halide bet, third filing, natural units).
Humility: N=1 snapshot/seed, 15-24 components; ordering robust, ratios +/-20%.
