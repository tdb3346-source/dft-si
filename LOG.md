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
Comprehension check (new rule: state the finding before the mentor explains it): alpha = 0.54 stated correctly in own words - MACE pushes ~54% as hard as GPAW. Correction absorbed: it is systematic (same error every time, right direction) not frequentist (right 54% of the time) - which is exactly why it is one curable dial and not noise.
Question logged (good one, wrong project number): "10 materials at once?" -> that is P6 (transfer test), and the answer is one target, then maybe two - each material needs its own convergence study + oracle discipline, the part that never transfers free. Ten uncalibrated oracles = confident garbage. Ten materials becomes right in Era 4, once P7's escalation rule automates the stamping - and then it is a map of alpha across chemistries, which is a paper.

## P4 PHASE 0 OPENED (Jul 14) - landscape scan
Pre-registered blind (both signatures, before reading anything):
- Patent density on CsPbI3 stabilization: I predict CROWDED on compositional fixes (A-site/cation mixing, halide alloying) and THINNER on process/strain/interface levers.
- I predict >=1 contradiction found between two papers on the same mechanism within the first 20 papers.
- I predict the mechanism menu grows from v0 by >=5 new entries with numbers attached.
- Abort trigger declared in advance: if every plausible lever is claimed AND the literature shows no open mechanism question, Phase 0 recommends re-targeting (a real, allowed outcome).
Deliverables: WHITESPACE.md (what's tried, what's crowded, what's thin) + mechanism menu v1.
Rule: a paper counts as read only if it yields (1) a menu entry with a number, (2) a benchmark number, (3) a contradiction, or (4) a one-line parking-lot note.
PHASE 0, day 1 scored: WHITESPACE.md created (1.4 KB). Patent landscape mapped: exact-phrase queries give 11/43/53/118 (fuzzy gave 4,900-15,000 = noise). HEADLINE: field is small and unfenced; 6 of 11 "iodide migration" patents build interface WALLS, 3 use additives, ~18% junk. Nobody targets the intrinsic lattice barrier - the field builds walls, our instrument measures hills.
Contradiction prediction: MISS - none found, and correctly so. The 11 patents AGREE (converging on wall-building). Catch #17 (mentor): predicted contradictions in the wrong genre - patents are written to claim, not argue. Contradictions live in PAPERS. Prediction re-filed for the literature pass, not the patent pass.
Density-by-lever prediction (crowded on composition, thin on process/interface): PARTIAL MISS on this sample - interface is the CROWDED lever, composition thinner. Opposite of my guess, on n=11.

## P4 PHASE 0 - PAPER HALF OPENED (Jul 15)
Target question: is the intrinsic-barrier hole an OPENING (nobody could compute it pre-MLIP) or the FIELD'S WISDOM (barrier can't be moved without breaking the absorber)?
Pre-registered blind (mentor signs):
- I predict CsPbI3 iodide-vacancy migration barriers HAVE been computed by DFT (several papers), in the 0.2-0.5 eV range, on the UNSTRAINED lattice.
- I predict barriers UNDER STRAIN are thin-to-absent - a handful of papers at most, and probably on MAPbI3 not CsPbI3.
- I predict NO paper has swept barrier vs composition at MLIP scale (hundreds of candidates) for CsPbI3.
- If all three hold, the hole is an OPENING and Phase 3 has its target. If barriers-under-strain is a crowded literature, the hole is partly the field's wisdom and we re-aim.
Benji's call goes in before we search.
PAPER HALF, day 1 - SCORED HARD:
Benji: "yes, 2-5 papers" -> HIT on yes, MISS on count (mature literature, many groups).
Mentor: "several papers, 0.2-0.5 eV, unstrained" -> HIT on range. Converged numbers: gamma-CsPbI3 0.42-0.43 eV (MD-Arrhenius + DFT-NEB + experiment agree); FAPbI3 vacancy 0.34-0.45 eV; MAPbI3 vacancy spread 0.08-0.58 eV (spread attributed to soft-lattice path-finding difficulty).
MENTOR PREDICTIONS DEAD (2 of 4): (a) "no MLIP-scale barrier work on CsPbI3" - FALSE. arXiv:2409.16051 (Tracing Ion Migration with MLFFs) does CsPbI3 iodide defects, charge states, MLFF-vs-DFT force validation, CI-NEB comparison, AND an SOC check (SOC affects defect geometry, not forces enough to train on). That is our Phase 1 SOC study + Phase 2 force validation + Phase 3 NEB, published, in our material. (b) "no composition sweep" - PARTIAL: Chem Mater 2025 (10.1021/acs.chemmater.5c00503) does gamma-CsPbI3 barriers + dopant effects (Sn 3%: 0.42->0.43 eV = no change) via DFT-NEB + 80 ns ML-MD.
ANSWER TO THE SHARP QUESTION: people ARE computing the intrinsic barrier. The patent hole is NOT ignorance - it is that a barrier is not a patentable ACTION. Reason (b) confirmed over (d).
ALSO: Science Advances "Multiple B-site doping suppresses ion migration" - the working lever is COMPOSITION (Eu-Yb-Ca in MAPbI3), i.e. the crowded room.
PHASE 0 JUST PAID FOR ITSELF: 3 days of reading vs 4 months reproducing a 2024 paper.
NEXT: read arXiv:2409.16051 in full - find what they did NOT do (strain? anharmonic regime? composition breadth?). Re-aim from there, honestly.
PAPER HALF - arXiv:2409.16051 read in full (Tyagi/Pols/Brocks/Tao, Eindhoven).
THEY DID OUR PHASES 1-3: MLFF for 6 charge states of I defects in CsPbI3, DFT force validation (R2>0.94, MAE<=55 meV/A), CI-NEB DFT-vs-MLFF, then 2ns x5 runs x5 temps on 216-unit supercells -> Arrhenius. Barriers 0.16-0.30 eV by charge state; V_I- immobile. SOC checked: affects defect geometry, not forces.
BENJI'S CALL "the target moved" - CORRECT.
THE CONTRADICTION FOUND (4 days after the prediction, in papers not patents): NEB vs MD disagree by 2-3x. Their V_I+: NEB 0.44 eV vs MD 0.16+/-0.03 eV. Field's TST/NEB spread for MAPbI3 vacancy: 0.08 / 0.26 / 0.32 / 0.58 eV = 7x, same defect. Their stated cause: NEB unsuitable for soft materials (path-sampling).
METHOD KILLED: our Phase 3 spec ("NEB barriers + DFT stamps") would have produced a number the field already knows is systematically wrong. Phase 3 must be MD-based, not NEB-based.
THE SURVIVING OPENING (re-aim): they validate forces with ABSOLUTE metrics (MAE). Nobody decomposes MLFF force error into SCALE vs DIRECTION on soft halides at migration-relevant displacements. Our alpha does exactly that. Systematic PES softening (Deng 2025) would bias barriers LOW - and their MD barriers ARE 2-3x lower than NEB. Is that soft-material physics or MLFF softening? UNANSWERED IN THE LITERATURE.
NEW P4 QUESTION: "How much of the computed barrier is the model's softening?" Cheap, ours, both answers publishable.
PATENT LESSON: patents need a demonstrable ACTION. A barrier is a property - computable by dozens, patentable by none. Any invention of ours must terminate in an action (powder test / recipe / treatment).
SKILL LOGGED (how to find the gold sentence): read for the APOLOGY, not the claim. Pattern = author admits their two instruments disagree, offers a plausible explanation, never tests it. Locations: Discussion section, the "however/note that/the exception is" sentences, the limitations paragraph. Tao paper's tell: "NEB values can easily be off by a factor of two... NEB might be less suitable for soft materials." Admitted disagreement + untested explanation = hole with a number attached.
THE 3 LEVERS (entire 41-patent landscape): (1) additives - extra molecule in the mix; (2) processing - solvent/anneal/growth route; (3) interface layers - buffer/coating/passivation next to the perovskite. All three are ACTIONS PERFORMED BY HANDS.
"Can I file 20 patents wholesale?" NO: patent needs novel AND non-obvious AND ENABLED. Additive #47 dies on obviousness, and we cannot enable it - no lab, and materials = "unpredictable art" requiring experimental data behind composition claims. Our only path: compute what they cannot see -> ONE prediction -> $5k physical confirmation -> patent the confirmed ACTION. One patent with a receipt > twenty without.
TODAY'S FIND IS PAPER MATERIAL, NOT PATENT MATERIAL: a 7x disagreement in the field's central number + an untested explanation. Nobody patents "your instrument is biased" - everybody cites it. Matches doctrine: open methods, owned matter.

## P4 PHASE 3 RE-SPECCED (Jul 15) - the barrier-softening audit
OLD SPEC (dead): NEB barriers + DFT stamps. Killed by Phase 0 - Tao et al. show NEB is 2-3x off vs MD in soft halides; we'd have computed a number the field knows is wrong.
NEW QUESTION: how much of a computed migration barrier is PHYSICS and how much is MLFF softening (Deng 2025 / our alpha)?
THE GAP: Tao V_I+ = NEB 0.44 eV vs MD 0.16+/-0.03 eV (2.75x). They blame soft-material path-sampling. They never checked model softening. Nobody in this literature decomposes force error into scale vs direction. We do.
LEGS: (1) alpha along the migration path - measure alpha at saddle-point geometries, not just rattled crystals. (2) barrier-vs-barrier: our DFT vs MACE on the same path; does the gap match what alpha predicts? (3) verdict: real physics vs model bias.
PRE-REGISTERED BLIND (both signatures, before any code): alpha DECREASES at the saddle point vs equilibrium (saddle is furthest from near-equilibrium training data) -> barriers systematically underestimated by a computable amount. Quantitative: alpha(saddle) < alpha(rattled 0.2A) for CsPbI3, i.e. < 0.88.
COST: weeks not months. Handful of paths, few dozen DFT single-points. No 1000-trajectory MD, no composition sweep.
PHASE 1 SHRINKS: need defect structures + DFT forces on migration configs. Polymorph (black vs yellow) study drops off the critical path - PARKED.
HONEST RISK: this is an AUDIT -> paper + benchmark, NOT a patent. Patent path (one prediction -> $5k powder test) is downstream, if at all. Doctrine-consistent: the audit IS the moat.
READING LIST (Phase 3-serving, capped at 3): (1) Tao SI - migration path geometries + per-charge-state barrier tables = our Phase 3 input + comparison target. (2) Deng 2025 softening paper - what it claims about migration barriers; check diamond-Si phonon numbers (open tension in log). (3) Chem Mater gamma-CsPbI3 dopant paper - WHY did 3% Sn move the barrier only 0.42->0.43? That is the field answering "why not just raise the barrier."
PATENT REALITY LOGGED: the unit is ONE with a receipt, not "a few." Path unchanged: compute what they can't see -> one testable prediction -> ~$5k powder + XRD -> provisional on the ACTION. That is Phase 4, 4-6 months out, contingent on the audit being predictive. Faster = someone selling filing fees.
PAPER PATH IS THE LIVE ONE: alpha audit (scale-vs-direction decomposition of MLFF force error, 3 materials + saddle-point prediction) is months not years, and it is what makes a wet lab answer an email later.
"MEANWHILE" ANSWER: nothing for 3 weeks. Then P5 (database audit, laptop-grade) is the ONLY sanctioned parallel work. Everything else is the widening reflex - 14 ledger entries document where it goes.

## P4 PHASE 1 OPENED (Jul 15) - shrunk spec: defect structures for the softening audit
Building: 2x2x2 cubic CsPbI3 supercell (40 atoms) with one iodide vacancy = the defect the field argues about.
Pre-registered blind (mentor signs, before any run): after relaxing the vacancy structure, the neighboring Pb atoms move APART (they lose the shared iodine bridge that held them). Prediction: nearest Pb-Pb distance INCREASES by >0.1 A vs the pristine lattice.
Note: Tao et al. used 2x2x2 for training, 6x6x6 for production MD. We start at 2x2x2 - if the DFT run is affordable we keep it, if the defect talks to its own periodic image we go bigger. That check comes later.

## P4 PHASE 1 - VACANCY RELAXATION (Jul 16)
Structure: 2x2x2 cubic CsPbI3 supercell, 40 atoms -> 39 with one iodide vacancy. Kill-check passed (Cs8Pb8I24 -> Cs8Pb8I23).
Run: GPAW PW(600), k 2x2x2 (equivalent density to 6x6x6 on the 1x cell), atoms relax / cell fixed. 25 BFGS steps, 1h44m, dE = -0.098 eV, final fmax 0.018 < 0.02 target.
PREDICTION (mentor signed): Pb-Pb around the vacancy moves APART by >0.1 A. RESULT: 6.3867 vs 6.390 pristine = moved TOGETHER by 0.003 A. MISS on DIRECTION and 30x on magnitude.
PHYSICS: matches Tao et al. - they report Pb-Pb SHORTENING around the vacancy (the two Pb2+ bond more tightly across the gap as the vacancy captures electrons), which is why V_I- is immobile. Our intuition ("remove the bridge, the ends fall apart") is exactly backwards. Counterintuitive result reproduced on our own machine.
CONFOUND CHECK (did it actually relax?): PASSED - 25 steps, real energy drop, not a stuck structure.
THE DIARY IS THE FINDING: fmax started 0.090, JUMPED to 0.331 at step 2 (4x worse), thrashed (0.14/0.19/0.24) for a dozen steps; energy rose at steps 2, 8, 11, 18. A smooth relaxation slides downhill. This one wandered a bumpy landscape.
=> SOFTNESS, FELT FROM THE INSIDE. Many near-degenerate positions for I around the vacancy = no strong opinion about where atoms sit. Same anharmonicity as the 4x-displacement/9.5x-force result. THIS IS EXACTLY WHY NEB STRUGGLES HERE (Tao's explanation, now observed in our own optimizer log).

## SADDLE ALPHA MEASURED (Jul 16) - first data on the new Phase 3 question
Crude midpoint saddle (I hops 4.42 A into the vacancy, straight-line midpoint). GPAW max|F| = 8.51 eV/A, RMS_F 1.49 - violent geometry, far outside MACE training distribution. Registered in advance as a directional probe, not the final measurement.
PREDICTION alpha(saddle) < 0.88: HIT - alpha = 0.832, cosine = 1.000, rel% = 17.0.
Alpha map now spans 2 orders of magnitude of force: Si 0.543 (0.02A) / 0.602 (0.05A) | STO 0.951 (0.05A) | CsPbI3 0.882 (0.2A rattle, RMS_F 0.46) -> 0.832 (saddle, RMS_F 1.49). Softening deepens with severity but GENTLY - no cliff.
ROBUSTNESS RESULT: cosine = 1.000 at a geometry the model has never seen. MACE points exactly right even when jammed. Interpretation A (catastrophic collapse at saddles) is DEAD.
THE SERVICE TO THE FIELD (mentor hypothesis MISS, and it matters): ~17% softening cannot explain Tao's 2.75x NEB-vs-MD gap (0.44 vs 0.16 eV). Model bias is largely CLEARED as the culprit; their soft-material path-sampling explanation gains support. We checked what nobody checked, and the answer exonerates the tool.
CAVEAT: crude midpoint, not a relaxed transition state. Real saddle = proper path optimization.
NEXT: does alpha hold at a RELAXED saddle (physically meaningful, forces near zero along the path)? That is the publishable version.
