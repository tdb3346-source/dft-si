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

## P4 OPENER SCORED (Jul 14) - matched-severity force check v2
Design goal met: RMS_F one band (Si 0.326 / STO 0.368 / CsPbI3 0.461 eV/A; v1 spread was 16x).
Bet 1 (Si rel% < 15 at matched severity): MISS - 45.9%. Error is severity-INDEPENDENT (40.1% @ 0.05A, 45.9% @ 0.02A; RMS_F scaled 0.42x for 0.4x amplitude = harmonic regime). OOD hypothesis for Si: DEAD by its own pre-registered test.
Bet 2 (CsPbI3 > STO, third filing): HIT - 12.5% vs 7.4%. Halide worse than oxide off-equilibrium, factor 1.7, now measured.
Sleeper: GPAW cutoff self-noise = 0.2% of RMS_F. Reference clean; Si error belongs to the student, not the worksheets.
CsPbI3 v1 24.3% resolved: small-denominator artifact - forces up 9.5x, rel error halves to 12.5%. Absolute 0.057 eV/A at 0.2A (anharmonic regime) is respectable.
Anharmonicity in the oracle: 4x displacement -> 9.5x RMS force (harmonic = 4x). Superlinear stiffening, measured.
NEW HYPOTHESIS (Si): systematic force-constant softening - scale-type error, not OOD.
PRE-REGISTERED blind (mentor signs): scale/direction decomposition next. Prediction: Si alpha in [0.55,0.85], cosine > 0.9, rel% after rescale < 15; STO/CsPbI3 alpha in [0.9,1.05]. Si cosine < 0.8 kills the softening story too.
Phase 0 reading list add: universal-MLIP phonon softening literature.

## SCALE/DIRECTION DECOMPOSITION SCORED (Jul 14)
Table: alpha/cosine/raw/rescaled: Si 0.543/0.997/45.9/7.5 | STO 0.951/0.998/7.4/5.8 | CsPbI3 0.882/0.999/12.5/4.4.
Bets: Si alpha MISS by 0.007 (more softening than predicted); Si cosine HIT; Si rescaled HIT; STO alpha HIT; CsPbI3 alpha MISS by 0.018 (softening side). Hypothesis structure CONFIRMED: Si error is scale, not direction - one scalar removes 84% of the error norm.
UNIVERSAL SOFTENING measured: alpha < 1 all three (Si 0.54 << CsPbI3 0.88 < STO 0.95). Cosines >= 0.997 everywhere.
INVERSION: rescaled, CsPbI3 is BEST (4.4%) - halide has the best-shaped forces in its anharmonic regime; Si carries the largest calibration error.
LITERATURE MATCH (verified): Deng et al., npj Comput Mater 11, 9 (2025) / arXiv:2405.07105 - PES softening in M3GNet/CHGNet/MACE-MP-0 from near-equilibrium training bias; affected quantities include ION MIGRATION BARRIERS; fix = fine-tuning. We reproduced it blind on our own oracle + added a halide-perovskite anharmonic-regime alpha they don't report.
CONSEQUENCES: P4 Phase 3 raw barriers biased LOW (quantified reason for fine-tune-first + DFT stamps). Phase 2 success metric born: post-fine-tune alpha = 1.00 +/- 0.05 per material.
CAVEATS: alpha bundles MACE softening + GPAW<->VASP training-target delta (Si too big to be code gap; STO's 5% could be). Harmonic implication: Si phonons ~26% soft (sqrt 0.543) - larger than typical published MACE-MP-0 phonon errors; tension flagged, probe next.
PRE-REGISTERED blind (mentor signs): alpha at OLD 0.05 A Si rattle (files exist, zero GPAW). Prediction: alpha(0.05) in [0.55, 0.70], cosine > 0.99. Amplitude-dependent alpha = structure in the softening worth reporting.
ALPHA-AMPLITUDE PROBE SCORED: alpha(0.05A) = 0.602, cosine 0.996 - HIT both clauses. Softening has structure: worst near equilibrium (0.543 @ 0.02A -> 0.602 @ 0.05A), relaxing with amplitude; direction near-perfect throughout. Harmonic limit implies alpha <= 0.54 -> Si phonons ~26%+ soft; tension with published MACE-MP-0 phonon benchmarks flagged. Caveats: 2 amplitudes = trend not curve; different seeds (42/43) add few-% noise to slope, not to direction of drift. Phase 0 task sharpened: check Deng et al. + MACE-MP-0 paper for diamond-Si phonon numbers specifically.
Day tally: 4 predictions scored (2 HIT incl. the halide bet's first-ever hit on filing #3, 2 informative near-MISS), one literature-verified reproduction of a 2025 npj finding + one additive halide data point, Phase 2 success metric minted (post-fine-tune alpha = 1.00 +/- 0.05).
