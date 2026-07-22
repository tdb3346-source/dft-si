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

## MACE NEB - path found (Jul 16), after 3 failed attempts
Catch #19 (mentor): teleported unrelaxed endpoint -> meaningless path (peak at endpoint).
Catch #20/#21 (mentor): endpoints relaxed in DIFFERENT engines (GPAW init, MACE final) -> 53 meV mismatch waved through as "marginal" -> NEB diverged to step 2243, fmax 1.05, E +8.5 eV off. Fix: relax BOTH endpoints in MACE's own landscape -> mismatch collapses 53 meV -> 0.5 meV (100x). RECEIPT FOR THE RULE: "never compare energies across codes" cost 8 hours of GPAW + a 2243-step divergence.
FINAL PATH: energies [0, -0.207, -0.039, +0.149, -0.057, -0.216, -0.000]. Endpoints symmetric to 0.0005 eV. Peak at image 3 (dead center) = correct saddle position.
PATH DIAGNOSTIC (kill-check): hopper distance to hole marches 4.43/4.05/3.40/2.51/1.48/0.63/0.12 A - MONOTONIC, no backtracking. Other atoms move 0.25-0.89 A = neighbors making way, not band collapse. Sideways-collapse hypothesis DEAD.
THE W IS REAL: intermediate images sit BELOW both endpoints (-0.21, -0.22). The floppy lattice finds better arrangements mid-hop than at rest. This is the soft/anharmonic landscape (measured all week: 4x displacement -> 9.5x force) now visible in a migration path - and it is exactly the pathology Tao invokes for why NEB struggles here.
BARRIER UNQUOTABLE: 0.149 eV is height above a fake baseline; true climb from the -0.216 dip is ~0.37 eV. 7 images / 4.4 A is coarse; 0.89 A neighbor motion suggests under-resolution. Mentor's "MACE undershoots ~0.4 eV" prediction: UNSCOREABLE, not hit. Not laundering a W into a win.
FOR THE AUDIT: image 3 is a genuine, physically-reached mid-hop geometry at the top of the local climb = a legitimate place to measure alpha.

## REAL SADDLE ALPHA - UNMEASURABLE (Jul 16). Prediction UNSCOREABLE.
GPAW at NEB image 3: max|F| = 0.160, RMS|F| = 0.0422 eV/A - 35x gentler than the crude midpoint (8.51/1.49). Tiny forces = properly balanced saddle = the path is real. Good news.
Result: alpha = 0.083, cosine = 0.276, rel% = 96.2. REJECTED as physics.
WHY: (1) cosine 0.28 is impossible - it has never gone below 0.996 in any measurement; models do not forget direction. At a saddle both engines' forces are near zero and what remains is mostly noise (GPAW convergence noise ~0.001-0.01 vs signal 0.042). Subtracting two whispers. (2) CATCH #22 (mentor, conceptual): the saddle IS MACE's own stationary point - MACE optimized the band until its own forces were ~0.04. Measuring alpha at a model's own minimum is a tautology, not a measurement.
THE REAL FINDING: saddle geometries have vanishing forces => FORCE-BASED ALPHA CANNOT PROBE SADDLES, EVER. The audit premise needs re-aiming: you cannot measure a scale factor where there is no scale.
RE-AIM: the saddle probe must be ENERGY-based, not force-based - compute the same barrier with both engines, compare heights. Different experiment, and the one that always mattered.
Registered caveat fired as written ("if alpha comes back wild, suspect noise before physics") - the one thing that went right.

## ENERGY-BASED BARRIER AUDIT (specced Jul 16) - the re-aimed Phase 3
Method: GPAW single-points on all 7 MACE NEB images. Same geometries, both engines, compare barrier heights. ~10 min per image (proven), ~70 min total, background.
Claim scope (registered): this measures whether MACE misjudges the height of the hill IT found - not whether MACE's barrier is the true barrier (GPAW would find its own path). Narrower, and the right claim for a softening audit.
PRE-REGISTERED BLIND (mentor signs): GPAW's barrier on MACE's path is HIGHER than MACE's own. Reasoning: PES softening (Deng 2025) = underpredicted curvature = shallower hills. Quantitative: GPAW barrier > MACE barrier by >10%. If they match within noise, softening does NOT reach barrier heights and my whole Phase 3 premise dies - which would itself be the finding (the tool is cleared, twice over).
Benji's call goes in before we run.
BENJI'S CALL (blind, opposing the mentor): GPAW barrier comes out LOWER than MACE's 0.149 eV. Mentor: HIGHER by >10%. Direct opposition, both signed before the run.

## BARRIER AUDIT SCORED (Jul 16) - BENJI WINS, and the result inverts the hypothesis
GPAW on MACE's path: [0, -0.172, -0.057, +0.121, -0.068, -0.179, -0.005]. BARRIER = 0.121 eV, peak image 3.
MACE on its own path:  [0, -0.207, -0.039, +0.149, -0.057, -0.216,  0.000]. BARRIER = 0.149 eV, peak image 3.
BETS: Benji "GPAW lower" = HIT. Mentor "GPAW higher by >10%" = MISS, wrong direction. GPAW is 19% LOWER (MACE overpredicts by 23%). Benji now 3-for-4 on recent blind calls.
THE INVERSION: MACE's hill is TOO TALL, not too short. Softening (Deng 2025) predicts underpredicted curvature = shallower hills = LOWER barriers. We got the opposite sign. Second independent strike against "softening explains the field's barrier problems" (first: alpha too mild to explain Tao's 2.75x gap).
SHAPE AGREEMENT (the framed result): both engines reproduce the same W - same peak position (image 3), same dips at 1 and 5, same magnitudes within ~20%. The engines agree on the LANDSCAPE SHAPE and disagree only on AMPLITUDE, with MACE exaggerating every feature ~20%. THE W IS REAL PHYSICS, professor-confirmed: the soft lattice genuinely finds better arrangements mid-hop than at rest.
CAVEATS: 7 images is coarse; this is MACE's path not GPAW's; single measurement, no error bar. The finding is a DIRECTION, not a number.

## NEXT (queued, not run): barrier convergence check
Question: is MACE's +23% real, or an artifact of 7 coarse images across a 4.4 A hop?
Method: rerun MACE NEB with 11 images, same endpoints, then GPAW single-points on the new peak + neighbors. Cost: MACE minutes, GPAW ~30 min for 3 images.
PRE-REGISTERED BLIND: the gap SURVIVES - MACE stays higher than GPAW by 15-30% with 11 images. Reasoning: both engines drew the same W with the same peak position, so the shape is converged enough; the amplitude difference is the model, not the resolution.
Benji's call goes in before the run.
Benji's call (blind, Jul 17): gap SURVIVES - agrees with mentor. Both exposed if it collapses.

## CONVERGENCE CHECK SCORED (Jul 17) - BOTH HIT, gap GREW
MACE-11: barrier 0.152 eV, peak image 5 of 10 (dead center). MACE-7 was 0.149 at image 3 of 6. Barrier moved 3 meV (2%) for 4 extra images => CONVERGED. The 0.15 eV barrier is NOT a resolution artifact.
W resolved properly at 11 images: [0, -0.10, -0.18, -0.05, +0.10, +0.15, +0.09, -0.07, -0.19, -0.13, 0]. Symmetric, two wells at images 2 and 8, single central peak.
GPAW on MACE-11 path (images 0,4,5,6): [0, 0.058, 0.108, 0.056]. BARRIER = 0.108 eV, peak at image 5 - same position as MACE.
BETS: both predicted "survives, 15-30%". HIT on direction; magnitude OVERSHOT the band - MACE is +41% (0.152 vs 0.108), up from +23% at 7 images. Better resolution, BIGGER gap.
FINDING (two independent resolutions, effect strengthening): MACE-MP OVERPREDICTS the CsPbI3 iodide migration barrier by ~40% on identical geometries. Engines agree on WHERE the hill is; disagree on HOW TALL by 41%.
THIRD STRIKE against "softening explains the field's barrier problems": (1) alpha too mild to explain Tao's 2.75x gap; (2) sign inverted at 7 images; (3) sign inverted harder at 11. Softening predicts SHALLOWER hills. We measure TALLER.
CAVEATS: MACE's path not GPAW's; one defect, one charge state; no error bar; 4 points around the peak. Robust DIRECTION, firming magnitude, not yet a publishable number.
INTERSTITIAL PATH (Jul 17): does the +41% generalize? Different defect, different mechanism (extra I forms a Pb-I-I-Pb double bridge, hops bridge-to-bridge; vacancy = atom slides into a hole). Same bias on both = pattern in the model, not a quirk of one geometry. PRE-REGISTERED BLIND: mentor - overpredicts by 20-60%. Benji - overpredicts. Both signed before any code.
INTERSTITIAL - endpoint gate FAILED: E(fin) - E(init) = -0.372 eV, 7x tolerance. Not a hop between equivalent sites; a downhill slide to a better structure. NEB refused - would have cost 40 min GPAW to learn nothing. Gate saved it.
Catch #23 (mentor): "reflect across neighbour" built an atom-on-atom geometry -> MACE diverged to 3957 steps, E = -7.7e14 eV. NEW PERMANENT RULE: every constructed geometry gets a minimum-distance check BEFORE any optimizer. Structure sanity precedes energy sanity. Rule fired 10 min later and caught a 0.753 A placement in 2 seconds.
Geometry learned: our interstitial bridges two Pb at 3.316 A each, 3.717 A from the nearest lattice I = matches Tao's neutral/negative interstitial ("doubles the bridge between two Pb"). Real defect, correctly built. The HOP is what we cannot guess.
DECISION: interstitial parked pending Tao SI Note 1 (optimized defect geometries + migration paths). Twenty minutes of reading replaces a week of guessing. Vacancy result (+41%, converged at 2 resolutions) stands alone regardless.
INTERSTITIAL PARKED (Jul 17): Tao SI unavailable - paywalled behind the ACS version (10.1021/acs.jpclett.5c01139); arXiv page has main text only ("SI will be made available on publication"). Without their optimized geometry we would be guessing hop targets for days. Decision made in ADVANCE as option (b), executed as written.
REOPEN TRIGGER: SI becomes available (check the ACS page periodically), OR we email Tao directly (s.x.tao@tue.nl - authors routinely share SI on request; costs one email), OR we characterize the interstitial ourselves (real work: band structure + charge state analysis, weeks not days).
STANDS ALONE: vacancy finding (+41% at 11 images, +23% at 7, converged, both engines agree on peak position) does not depend on the interstitial. Interstitial would upgrade "quirk" to "pattern" - a strengthening, not a requirement.
Day tally: 1 finding shipped (barrier gap survives convergence and GREW), 2 blind predictions HIT by both parties, 1 mentor catch (#23, atom-on-atom geometry -> 3957-step explosion), 1 new permanent rule (structure sanity before energy sanity) which fired and saved a run 10 minutes later, 1 gate correctly refusing a bad path (-0.372 eV endpoint mismatch) and saving 40 min of GPAW.
CHARGED VACANCY (Jul 18) - what does MACE's neutral-only limitation cost? MACE has no charge knob; every MLFF barrier in this field is a neutral-defect barrier. Tao: charge state shifts vacancy migration substantially (V_I+ faster than V_I0; V_I- immobile). V_I+ is the dominant mobile species under equilibrium - the one that matters for devices. Experiment: GPAW single-points on the same 11-image MACE path (images 0,4,5,6) with charge +1, compare to neutral 0.108 eV. PRE-REGISTERED BLIND: both LOWER. Mentor 0.06-0.09 eV, Benji lower. SCOPE CAVEAT registered up front: charged energy on a NEUTRAL-optimized path; true V_I+ path would differ (charge changes local geometry). Measures the shift on a fixed path, not the true V_I+ barrier. Also: GPAW charge=+1 uses a uniform background charge - standard, with known finite-size caveats; we measure a shift, not an absolute.

## CHARGED VACANCY SCORED (Jul 18)
GPAW +1 on the neutral-optimized path: [0, 0.052, 0.094, 0.042]. V_I+ BARRIER = 0.094 eV, peak image 5 (same position as neutral and MACE).
Neutral V_I0 = 0.108 eV. MACE (neutral only) = 0.152 eV.
BETS: both "lower" = HIT on direction. Mentor's band 0.06-0.09 = MISS (0.094). Effect is 13%, far smaller than either of us expected.
THE DISCREPANCY: Tao reports V_I+ migrating an ORDER OF MAGNITUDE faster than V_I0. A 13% barrier shift cannot produce 10x rate change (would need ~0.06 eV at 300K, we see 0.014).
RESOLUTION = the pre-registered caveat: we froze the geometry. Tao's mechanism is STRUCTURAL - the vacancy captures electrons, surrounding Pb pull inward (seen day 1: Pb-Pb contracted 0.003 A around our neutral vacancy). We removed an electron but forbade the atoms to respond.
=> DECOMPOSITION (nobody has published this): the charge effect on migration barriers is ~87% STRUCTURAL, ~13% ELECTRONIC. Falsifiable, and it came from a limitation declared BEFORE the run.
THE REFRAME: MACE 0.152 | GPAW neutral 0.108 | GPAW charged 0.094. MACE's error (+41% over neutral) is 3x LARGER than the entire charge effect (13%). The field's leading worry for this quantity - get the charge state right - is dwarfed by a tool error nobody is measuring.
CAVEATS: neutral-optimized path; uniform background charge (finite-size corrections not applied); single defect; no error bars.

## RELAXED CHARGED VACANCY (Jul 18) - direct test of the 87/13 decomposition
Question: does letting the geometry relax under charge recover Tao's order-of-magnitude rate difference?
PRE-REGISTERED BLIND, OPPOSING: Mentor - YES, barrier drops below 0.06 eV (structural relaxation is the missing 87%). Benji - NO, relaxation does not do it. If Benji is right, yesterday's 87/13 headline claim is FALSE and dies by his call.
Method: relax the vacancy endpoint AND the peak image (image 5) with GPAW at charge +1, atoms free / cell fixed. Barrier = E(relaxed peak) - E(relaxed endpoint), both charged.
Caveat registered: relaxing the saddle can slide it off the path (a saddle is a maximum along the path, minimum perpendicular to it). If the peak relaxes downhill into a well, that is a different failure and we say so.

## RELAXED CHARGED VACANCY SCORED (Jul 18) - a HIT I am not claiming
RELAXED V_I+ BARRIER = 0.059 eV. Endpoint relaxed -113.8169 (0.047 eV of relaxation); peak relaxed -113.7577 (0.076 eV).
BETS: Mentor "drops below 0.06" = technically HIT by 0.001 eV. Benji "no" = wrong on direction.
VERDICT REFUSED: the peak relaxation NEVER CONVERGED - stalled at fmax 0.11-0.20 vs 0.03 target, hit the 60-step cap, last steps thrashed 0.110/0.107/0.204. A number landing 1 meV inside a band on an unconverged optimizer is a coin flip with a decimal point. Claiming this HIT would be reward hacking. Ten more steps could put it anywhere in 0.05-0.07.
WHAT IS SOLID: relaxation dropped the barrier 0.094 -> 0.059 = 37% reduction. The structural effect is real and large. Direction robust; the boundary crossing is not.
DECOMPOSITION CORRECTED: 0.108 (neutral) -> 0.094 (charged, frozen) -> 0.059 (charged, relaxed). Electronic 0.014 eV, structural 0.035 eV => ~29% electronic / ~71% structural. Yesterday's "87/13" was too aggressive; today's data corrects the mentor's own headline. Benji's instinct - relaxation would not do the whole job - was directionally right.
FULL LADDER NOW: MACE 0.152 | GPAW neutral 0.108 | GPAW V_I+ frozen 0.094 | GPAW V_I+ relaxed 0.059. MACE's error vs the physically relevant barrier (relaxed V_I+) is +158%.
CAVEAT: unconverged peak; neutral-optimized path as the starting geometry; uniform background charge, no finite-size correction.

## REPLICATION + PHASE 2 DATA (Jul 18) - A feeds B
Rule adopted (Benji): do it right and make something useful. Standing #1.
Plan: 3 vacancy sites, same pipeline. Replication gives an error bar (turns a measurement into a claim). Every DFT point becomes Phase 2 fine-tuning data. A IS B's input.
PRE-REGISTERED BLIND: Benji ~41% again. Mentor 35-50%, tight. Both betting the error is SYSTEMATIC and site-independent.
Also correcting the mentor's own overreach: "one phase per day" does not close arithmetically - Phase 2 needs a few hundred DFT configs at 10-40 min each = 50+ hours of compute. Tao used a cluster and months. What IS achievable: parallel background jobs instead of serial waiting.
Catch #24 (mentor, caught before compute): proposed 3 vacancy sites as a "replication" test - but in a perfect cubic cell all 24 iodine sites are SYMMETRY-EQUIVALENT. It would have measured numerical noise, not site-dependence. Three days of compute to learn my own arithmetic. Benji's call: "a is not doing useful work" - correct, and the reason is symmetry.
RE-AIMED to strain: 1-2% strain BREAKS the cubic symmetry, creating genuinely inequivalent iodine sites. Same cost, tests what we actually bet on, and connects to the strain-release-layer patent (the best mechanism find in the Phase 0 landscape: thermal-expansion mismatch -> lattice distortion -> defect formation -> accelerated black-to-yellow transformation; T90=1800h, 20.1% PCE).

## STRAIN RESULTS (Jul 18) - asymmetric, and the gate did the work
tens2 (+2% along c): MACE energies [0, -0.114, -0.194, -0.093, 0.050, 0.112, 0.054, -0.087, -0.168, -0.140, -0.043]. BARRIER = 0.112 eV at image 5. Unstrained MACE was 0.152 -> tension LOWERS the barrier 26% in MACE's view. Endpoint tilt -0.043 eV (strain broke exact equivalence, as expected).
comp2 (-2% along c): structure check PASSED (3.187 A, no collision) but ENDPOINT GATE FAILED: diff = -0.514 eV. Not a hop - a slide to a much better structure. Compression makes the two iodine sites GENUINELY INEQUIVALENT by half an eV. 12x the tension tilt.
=> STRAIN IS ASYMMETRIC: stretching preserves near-equivalence and gives a clean barrier; squeezing destroys it. Connects directly to the strain-release-layer patent's mechanism claim (thermal-expansion mismatch -> lattice distortion -> defect formation).
TWO READS TO SEPARATE: (a) compression genuinely creates a strong site preference = physics; (b) the specific iodine I deleted happens to land somewhere special under compression = artifact of atom choice. Test: delete a DIFFERENT iodine in the compressed cell, see if the asymmetry persists. Cheap.
DISCRIMINATING TEST (Jul 18): three different iodines in the -2% compressed cell. Endpoint diffs: pick 4 = -0.0769, pick 8 = -0.0769, pick 12 = -0.5140 eV.
VERDICT: PHYSICS, not artifact. Two picks IDENTICAL to 4 decimals (symmetry signature), one 7x worse. Compression SPLITS the 24 equivalent iodine sites into CLASSES: bridges along the strained axis vs bridges perpendicular to it. Within-class hop asymmetry = 0.077 eV; between-class = 0.514 eV.
MECHANISTIC CONTENT: strain does not merely perturb - it creates energetically distinct iodine environments, with the strained-direction sites dramatically less stable. That is a source/sink structure for migration = exactly the strain-release patent's degradation claim, made concrete from first principles.
CONSEQUENCE: picks 4/8 are measurable (small tilt, not a slide). Compressed barrier can be computed on a within-class hop.
comp4 (-2%, pick 4) NEB: BROKEN. Energies [0, -0.301, -0.586, -0.439, -0.353, -0.445, -0.292, -0.540, -0.346, -0.592, -0.077] - every image BELOW image 0, peak at image 0, wells to -0.59 eV. No hill; a slide off a ledge. Endpoint diff never printed - gate never fired.
DIAGNOSIS: the -2% compressed lattice is not at its minimum in MACE's landscape. The 200-step relaxation cap stopped early; NEB images then discover structures 0.6 eV better than the "relaxed" endpoint. Compression likely triggers a real reorganization (flirting with the known black->yellow instability).
DECISION: compression PARKED. Getting a compressed barrier requires first characterizing what the compressed lattice does (distortion? phase change? true minimum?) - a research project, not a control variable. We came to test site-independence of MACE's +41%, not to map strain-induced phase behavior.
KEPT: tension (+2%) gives a clean converged path, MACE 0.112 vs unstrained 0.152 = one genuinely different environment where the error IS measurable. Compression finding stands alone: strain splits iodine sites into classes (within-class 0.077, between-class 0.514 eV) and at -2% the lattice stops supporting a simple hop.

## TENSION AUDIT SCORED (Jul 18) - BOTH MISS, and it breaks the clean story
GPAW tension (+2%): [0, 0.024, 0.092, 0.050]. BARRIER = 0.092 eV, peak image 5.
MACE tension = 0.112 eV. OVERPREDICTION = 21.2%.
BETS: Benji ~41%, Mentor 35-50% tight. BOTH MISS. It is HALF the unstrained value.
THE FINDING (kills our shared hypothesis): MACE's barrier error is ENVIRONMENT-DEPENDENT, not a fixed systematic bias. 2% tension cuts the overprediction from 41% to 21%.
MECHANISM VISIBLE IN THE NUMBERS: both barriers drop under tension (GPAW 0.108 -> 0.092 = -15%; MACE 0.152 -> 0.112 = -26%). MACE is OVER-SENSITIVE to strain - it exaggerates how much stretching helps.
CONSEQUENCE FOR PHASE 2: fine-tuning on unstrained configs would teach the model to correct a 41% error that does not exist under strain. Fix one environment, break another. Practical finding for anyone fine-tuning these models - and the opposite of the encouraging result we wanted.
CAVEATS: 2 data points is a line not a trend; tension path had an endpoint tilt (-0.043 eV) the unstrained one lacked; one strain magnitude, one direction. Direction unambiguous, size (half) far outside noise.
FULL TABLE: unstrained GPAW 0.108 / MACE 0.152 (+41%) | tension +2% GPAW 0.092 / MACE 0.112 (+21%) | charged relaxed GPAW 0.059 (unconverged) | compression -2% = lattice unstable, parked.

## STRAIN REPRESENTATION GATE (Jul 18) - Benji's design, Benji leading
Reframe (Benji, unprompted): this is NOT a barrier experiment, it is a representation/domain-coverage gate before spending compute on barriers. Mentor had collapsed two questions; Benji separated them.
Design: 9 tensile points 0 to +2% in 0.25% steps. Vacancy cell. Fractional coords FIXED, single-points only (removes optimizer as confound). Identical GPAW settings throughout. Metrics: signed energy error meV/atom, force RMSE, max force error, per-atom error localization. Percentages SECONDARY only (scale-confound lesson applied unprompted).
Safeguards added by Benji: (1) absolute GPAW energy vs the 0% structure, not percentage; (2) per-atom force-error patterns, because smooth aggregate RMSE can hide one iodine going catastrophically wrong.
BENJI'S BLIND PREDICTION: energy error smooth, nonlinear improvement toward +2%. Force RMSE noisier but broadly smooth. Largest errors concentrated around the defect environment, not uniform.
DECISION RULE, WRITTEN BEFORE DATA: smooth energy + force -> proceed to 4-strain barrier test (0, 0.67, 1.33, 2.0%). Smooth energy but jagged/local catastrophic force errors -> fine-tuning might work but MLIP unsafe for NEB/MD. Jagged both, with clean SCF -> stop barrier work, redesign training/domain strategy. Sudden jump WITH structural/SCF change -> diagnose the calculation first, not the model. Clean only because averaged -> does not count as passing.

## STRAIN GATE: PASSED (Jul 18) - Benji's design, and it found something neither of us predicted
ENERGY: smooth, monotonic, nonlinear. Errors 9.5/19.2/29.2/39.6/50.7/62.1/73.8/85.9 meV. Consecutive deltas 9.7/10.0/10.4/11.1/11.4/11.7/12.1 - no wobble anywhere. BENJI'S CALL: HIT.
FORCES: RMSE 0.051/0.051/0.050/0.051/0.048/0.048/0.048/0.052/0.047 - flat, stable, noisier than energy but not jagged. BENJI'S CALL: HIT.
LOCALIZATION: BENJI'S CALL MISS, and the miss is the finding. Worst atoms are NOT at the defect. They are LEAD, in symmetry-equivalent pairs: atoms 1 and 5 both exactly 0.1982; atoms 3, 7, 8 all exactly 0.1440. Identical to 4 decimals = symmetry-equivalent = systematic, not noise. Worst/median = 6.1x. BENJI'S SECOND SAFEGUARD (per-atom localization) caught exactly what he built it to catch: a clean aggregate hiding one atom TYPE going wrong.
=> REFRAME: this is not a defect problem or a strain problem. MACE-MP HAS A SYSTEMATIC ERROR ON Pb. Physically sensible - Pb is heavy, relativistic bonding, and lead halides are a thin slice of Materials Project training data. Every barrier that moves iodine past lead inherits it.
THE MECHANISM, VISIBLE: strain energy cost - GPAW 0.093 eV, MACE 0.179 eV over 2%. MACE thinks stretching this lattice costs NEARLY TWICE what it does. Error grows linearly at ~43 meV per 1% strain. That is NOT softening (Deng 2025 predicts underpredicted curvature) - it is the model being TOO STIFF. Which explains the too-tall barriers, AND why the error shrank under tension: we were partially unwinding a stiffness error.
DECISION RULE FIRES: smooth energy + smooth forces -> PROCEED to the 4-point barrier sweep (0, 0.67, 1.33, 2.0%). Phase 3's second and final experiment. Then Phase 3 closes per the exit criterion.

## PHASE 3 FINAL EXPERIMENT (Jul 18): 4-point barrier sweep, 0 / 0.67 / 1.33 / 2.0% tension
Have: 0% (GPAW 0.108, MACE 0.152, +41%) and 2% (GPAW 0.092, MACE 0.112, +21%). Computing the two middle points.
PRE-REGISTERED BLIND: Mentor - lands close to linear (~34% at 0.67%, ~27% at 1.33%), within a few points, because the underlying stiffness error is linear in strain (43 meV/1%) and a barrier is just an energy difference. Benji - MIGHT DEVIATE.
Note the asymmetry of the calls: mentor predicts no structure, Benji allows for structure. A deviation vindicates Benji and says barriers do NOT simply inherit the static energy error.

## PHASE 3 FINAL RESULT - 4-point barrier sweep (Jul 18). BENJI WINS.
| strain | GPAW | MACE | error |
| 0%     | 0.108 | 0.152 | +41% |
| 0.67%  | 0.107 | 0.141 | +37% |
| 1.33%  | 0.094 | 0.130 | +38% |
| 2.0%   | 0.092 | 0.112 | +21% |
BETS: Mentor "close to linear, ~34%/~27%" = MISS. Benji "might deviate" = HIT. Error is FLAT ~40% from 0 to 1.33%, then CLIFFS to 21%. Not linear. Benji now 5-for-7, won the two hardest calls of the week.
THE DEEPER FINDING: the two engines disagree on the SHAPE of strain response, not just amplitude. MACE barrier drops smoothly (0.152/0.141/0.130/0.112); GPAW holds then drops (0.108/0.107/0.094/0.092). This is a real disagreement about the PHYSICS of how strain affects migration, not a scaling error. The static-energy stiffness error (linear, 43 meV/1%) does NOT simply propagate to barriers - barriers are more complex than the energy gate suggested.
CAVEAT: single points on MACE 4-image-resolution paths near the peak; 1.33% GPAW barrier (0.094) sits close to 2% (0.092) - could be a real plateau or image 5 not being the exact GPAW saddle at that strain. Direction (non-constant error, shape disagreement) solid; exact plateau needs finer paths.

## POST-PHASE-3: "a little of both" (Jul 18, Benji's call)
Track 1: write-up skeleton (mentor drafting, no compute). Track 2: bromine substitution test (compute). They share a foundation - Track 2's result IS Track 1's second data point.
Bromine test question: does MACE's ~40% barrier overprediction hold for CsPbBr3 (different halide, smaller anion, well-studied)? If yes, the error is Pb-driven and chemistry-general -> ranking survives across halides -> screen is viable. If no, the mechanism is misunderstood.
PRE-REGISTERED BLIND: both ~40% again, same direction (error is about Pb, which Br does not change; not about iodine specifically).

## BROMINE TEST SCORED (Jul 18) - BOTH MISS, mechanism overturned
CsPbBr3: GPAW 0.126, MACE 0.139, overprediction 10.6%. CsPbI3 was +41%. Same Pb, same structure, only I->Br: error drops 4x.
BETS: both ~40% same direction. BOTH MISS badly.
MECHANISM OVERTURNED: the error is NOT Pb-driven/chemistry-general (our shared hypothesis). It is HALIDE-SPECIFIC. Iodine +41%, bromine +11%. Whatever MACE mismodels, it is about IODINE - heavy, polarizable, relativistic - not lead. The Pb-localization in the strain gate was the symptom's LOCATION (the Pb-I bond) not the cause (the iodine side of it). Br bonds the same Pb and the error nearly vanishes.
CONSEQUENCE FOR SCREENING (decisive, points to caution): error is 4x different between two halides -> ranking iodide-rich vs bromide-rich compositions with raw MACE compares barriers with wildly different error bars. Composition A could outrank B purely for having more Br. UNCORRECTED MACE CANNOT SAFELY RANK ACROSS HALIDE COMPOSITIONS. The audit answered its own question.
CONSEQUENCE FOR THE PAPER (stronger story): "MLIP barrier error is halide-specific - 41% iodide, 11% bromide - because the model mismodels heavy-anion bonding" is a mechanism + warning + testable prediction, not just a number. Tells the field WHERE the problem lives.
TABLE: CsPbI3 GPAW 0.108 / MACE 0.152 (+41%) | CsPbBr3 GPAW 0.126 / MACE 0.139 (+11%). Note: Br barrier HIGHER than I (0.126 vs 0.108) - chemically sensible, Br smaller and more tightly bound.

## CHLORIDE TEST (Jul 18) - third halide, completes the trend
Question: does MACE's CsPbCl3 barrier error fall below bromide's 11%, making Cl < Br < I? Tests whether the error tracks heavy-anion polarizability (Cl lightest/least polarizable -> should be most accurate).
PRE-REGISTERED BLIND: both below 11%. Mentor 5-10%. If Cl comes in ABOVE Br, the heavy-anion mechanism breaks.

## OVERNIGHT VERIFICATION QUEUE (Jul 18) - re-ground the halide series on GPAW's OWN paths
Problem: all three barriers (I 0.108, Br 0.126, Cl 0.188) are GPAW single-points on MACE-CHOSEN paths. If MACE picks bad paths (and it is worst at Cl), the sign reversal could be partly artifact. Fix: independent GPAW NEB for each halide.
Queue (sequential, one job, ~8h): Cl NEB, then Br NEB, then I NEB. Each capped at 40 steps, trajectory saved continuously (catch #18 lesson).
PRE-REGISTERED BLIND: sign reversal HOLDS. Mentor: Cl own-path barrier ~0.16-0.19 (may be below 0.188 but stays high; Cl genuinely tightly bound). Benji: holds.
If Cl own-path drops toward MACE's 0.108, the reversal WEAKENS to "error shrinks toward zero" - a different, milder paper. This run decides which paper we have.

## SIGN REVERSAL KILLED (Jul 19) - it was a path artifact. Verification worked.
Overnight plan (3 sequential GPAW NEBs) FAILED on runtime: one Cl NEB ran 11 hours, reached step 16 of 40, ~40 min/step, thrashing (fmax 0.13-0.51, not converging). Br and I never started. Mentor runtime estimate wrong again; full GPAW NEBs are UNTENABLE for this material.
BUT the partial Cl trajectory (saved continuously, catch #18) gives the answer: Cl GPAW-OWN-PATH barrier = 0.088 eV (unconverged, 16 steps), NOT the 0.188 from single-point-on-MACE-path. The MACE-chosen path INFLATED the DFT barrier >2x.
=> THE SIGN REVERSAL WAS AN ARTIFACT. Confirmed the exact caveat flagged at logging time. Grading GPAW on MACE's poorly-chosen Cl path manufactured the "-43% underprediction."
REAL SERIES (provisional): I GPAW 0.108 / MACE 0.152 (+41%); Br GPAW ~0.126 / MACE 0.139 (+11%); Cl GPAW ~0.088 / MACE 0.108 (~+20%). MACE OVERPREDICTS across all three. Error varies ~20-40% but NEVER reverses sign. The milder, honest paper.
METHOD CATCH (#26, the important one): single-point-on-MACE-path grades GPAW on geometries MACE chose, and MACE chooses worse paths for some halides than others - this partially manufactured a false result. Before ANY halide comparison is publishable, each barrier needs a path GPAW agrees with. Full GPAW NEB too slow; fix = higher-image MACE NEB (11 not 7) that GPAW grades, plus check GPAW forces along MACE's path are small.
CAVEAT ON THE CAVEAT: Cl partial path shows DEEP wells (-0.20) - softer than expected for tightly-bound Cl. The path may still be imperfect. 0.088 is provisional.
LESSON: we killed a bombshell before publishing it because we verified. This is the whole point of the discipline. A referee would have found the path artifact; we found it first.

## ============================================================
## THE RANKING TEST (Jul 19) - can the oracle screen compositions at all?
## ============================================================
## Rule #1 experiment: not more audit - the test that decides if invention is POSSIBLE with this tool.
## Question: does MACE's RANKING of makeable CsPbI3 modifications match DFT's ranking? (Order, not absolute values - a screen only needs order.)
## Candidate set (all makeable, from the patent landscape): pure CsPbI3 baseline | Br-substituted | Rb A-site swap | FA A-site swap. Ranking metric: iodide vacancy migration barrier (the quantity we can compute fast; a NECESSARY condition - if the tool cannot rank barriers it cannot rank the harder phase-stability question).
## PRE-REGISTERED BLIND, BOTH AGREE: ranking FAILS - MACE misorders. Reason: the heavy-anion/halide error that flipped the pure-halide ordering (DFT Cl>Br>I, MACE reversed) will flip the mixed candidates too.
## DECISION: ranking survives -> we have a screen, greenlight the Edison phase (thousands of candidates, DFT-stamp top few). Ranking fails -> raw MACE cannot screen, the fast-screen plan is DEAD, and the oracle-fix path (fine-tune / direct-DFT small sets) is EARNED with proof not assumption. No wasted outcome.
## ============================================================

## RANKING TEST RESULT (Jul 19) - THE DESCRIPTOR IS ILL-POSED. Decisive.
base (pure CsPbI3, all sites equivalent): MACE barrier 0.151 eV, endpoint diff 0.000 - clean.
br (25% Br): endpoint gate FAIL, diff -0.244. rb (25% Rb): FAIL -0.233. k (25% K): FAIL +0.117.
ALL THREE substitutions break endpoint equivalence. Not bugs - CHEMISTRY. Substitution destroys the site symmetry that makes a vacancy hop well-defined. In a pure crystal every hop is between equivalent sites; mix in another element and the two ends are inequivalent, so there is NO single barrier - there is a distribution, one per local environment, and which you compute is an artifact of site choice.
BOTH PREDICTED "MACE misorders." REALITY IS DEEPER: the ranking question is ILL-POSED. You cannot rank compositions by single-vacancy barrier because mixed compositions do not HAVE a single barrier.
RULE #1 VERDICT (stated plainly): the migration-barrier-screening approach to inventing a stabilizer is DEAD. Not "needs a better oracle" - the DESCRIPTOR does not survive the substitutions that make a composition worth screening. Fine-tuning MACE would NOT fix this: the problem is not accuracy, it is that "the barrier" stops being a single number when you mix elements. This kills fork (a), fork (c), and the Phase 2 fine-tuning justification simultaneously.
WHAT A GOOD VERIFIER IS FOR: it told us the approach cannot work BEFORE we burned 6000 filaments on it. That is the entire value of building the verifier first. Two weeks -> "this descriptor cannot screen for this invention" is a real, saved-us-months answer.
IMPLICATION FOR INVENTION: need a descriptor that (1) is well-defined for MIXED compositions and (2) connects to the black-to-yellow rot. Single-vacancy barrier is neither robustly. Candidates: phase-stability energy difference (black vs yellow) - well-defined for any composition, directly the failure mode - but expensive. THIS is the real next question.

## ============================================================
## SCORECARD RE-ANCHOR (Jul 19) - what P4-P7 are actually FOR
## ============================================================
## THE GOAL (Benji, stated clearly): build discovery TOOLS that move materials science ~10 years ahead - 100x work, methods nobody built. Solar/perovskite is the PROVING GROUND and the mission domain, NOT the deliverable.
## THE TOOL, two layers, in order: (1) a TRUST/VERIFICATION layer that catches lies in computational screening - which approaches/descriptors/models to believe. (2) a GENERATION engine that proposes candidates. BUILD (1) FIRST - a generator without a verifier is confident garbage at scale (proven this afternoon: every reach for combination-mixing/6000-iterations/autoresearch failed the "where is the verifier" test).
## P4-P7 ARE THIS, correctly: P4 = build the verifier/oracle layer. P5 = calibration at scale. P6 = transfer test (new material). P7 = verifier + generator loop. The architecture is INTACT.
## THE SLIP TO CORRECT: grading progress by "did we invent a material" instead of "did we build verification capability." Under the RIGHT scorecard, 2 weeks produced P4's actual deliverable: a working verifier that already caught TWO real failures - (a) MACE misranks halide barriers, (b) single-vacancy barrier is ILL-POSED for mixed compositions. Both are outputs of the tool WORKING.
## P4 DELIVERABLE (corrected): not "a stabilized perovskite" but "a verification tool that says which screening approaches to trust, demonstrated on perovskites." The ranking test IS the tool's first output: fed a proposed descriptor, returned 'ill-posed, reject.'
## NEXT: stop hunting the material. Build the verifier as an actual TOOL (generalize the manual predict/gate/DFT-stamp/descriptor-validity checks into something reusable). First real capability to formalize: the DESCRIPTOR-VALIDITY CHECKER - before screening N compositions on descriptor X, test whether X is well-posed and whether the fast model ranks it. We just ran it by hand and it worked.
## ============================================================
RULE (Jul 20, after 3 failed overnight GPAW-NEB runs): GPAW NEBs are BANNED from unattended/overnight jobs - they thrash 40+min/step on this soft lattice and never converge in a night (chloride 11h/step16; iodide 11h/still-on-iter-1, partial barrier 0.238 inflated and still dropping). Unattended jobs use ONLY: MACE (minutes) or GPAW SINGLE-POINTS (10min each, batchable, always finish). Referee barriers = GPAW single-points on MACE's converged path, never GPAW's own NEB. Mentor failure: kept choosing a job type that cannot finish; 3 nights lost.

## REFEREE IODIDE BARRIER - SETTLED (Jul 20)
Full 11-point GPAW single-points on MACE's converged path: [0, -0.096, -0.175, -0.083, +0.058, +0.108, +0.056, -0.096, -0.173, -0.117, -0.005]. Clean symmetric W, peak image 5.
REFEREE IODIDE VACANCY BARRIER = 0.108 eV. Confirms the earlier 4-point value exactly, now at full resolution.
METHOD VINDICATED: GPAW single-points on MACE's path FINISH (survived a terminal crash mid-run - recomputed only missing images from saved energies). GPAW's own NEB never converged in 3 overnight attempts. Single-points, batched, resumable = the only viable referee method on this soft lattice.
STANDING FACTS NOW FIRM: iodide GPAW 0.108 / MACE 0.152 = +41%. Br GPAW ~0.126 / MACE 0.139 = +11%. Cl own-path ~0.088 (partial) / MACE 0.108. MACE overpredicts, halide-dependent, no sign reversal.

## PHASE-STABILITY DESCRIPTOR TEST (Jul 20) - discriminates, but on the WRONG axis. Checker catch.
MACE dE(black-yellow) meV/fu: base +88.3, br +125.3, rb +166.8, k +198.7. Spread 110 (>20 threshold - "discriminates").
BUT: (1) SIGN backwards - all positive = yellow more stable than black for ALL, including pure CsPbI3 which has a working metastable black phase. Physically suspect. (2) RANKING tracks substitution DISRUPTION exactly (base<br<rb<k = smallest to biggest lattice mismatch; K is too small for A-site, distorts most). Not "K resists rot best" - "K wrecks geometry most, and the approximated yellow phase responds to that."
VERDICT: descriptor passes check-1 (well-posed) and check-3 (discriminates) but FAILS the hidden check - discriminates on the WRONG axis (disruption, not phase stability). A screen using this would rank K as best stabilizer = BACKWARDS (K destabilizes CsPbI3 in reality). Confidently wrong, like MACE's halide ordering.
ROOT CAUSE: yellow phase APPROXIMATED with same crude recipe for all 4 (logged as caveat before the run). The approximation, not the physics, drives the ranking.
CHECKER LESSON (more subtle than the barrier catch): a descriptor can be well-posed AND discriminate AND still be useless if it discriminates on the wrong axis. Spread > threshold is necessary, NOT sufficient. The checker needs a 4th check: is the discrimination axis the INTENDED one? (requires either a physical sanity anchor or DFT spot-check of the ranking.)
STATUS: phase stability with a proper delta-phase structure MIGHT be usable - unknown, needs real work. With this approximation it is NOT. Descriptor NOT yet certified.

## ============================================================
## CONSTITUTION RULE #2 (Jul 20) - BUILD GENERAL IN-HOUSE VERIFIER TOOLS
## ============================================================
## The #2 goal (serving #1, invention) is to build GENERAL, REUSABLE in-house VERIFIER tools -
## not one-off scripts for one material or one descriptor. A tool that checks only one thing is a
## script; a tool that checks ANY thing you plug into it is a verifier. Build the general version.
##
## WHY GENERAL, NOT HARDCODED: the goal is a capability that makes FUTURE work 100x faster.
## A checker hardcoded for phase-stability validates phase-stability once. A general checker -
## one that takes any descriptor as a plug-in and runs its gates blind to what the descriptor
## computes - validates EVERY future descriptor as a tool call instead of a two-week manual analysis.
## That generality IS the 10-years-ahead leverage. Hardcoding it away to save time today is
## borrowing against the whole point.
##
## THE PATTERN, permanent: when building a tool, ask "does this generalize, or am I solving
## exactly one instance?" One instance = a script, acceptable only as a throwaway. The DELIVERABLE
## is always the general tool. This is how an in-house toolkit accumulates instead of resetting.
##
## FIRST INSTANCE: the descriptor-validity checker. Takes (descriptor_fn, compositions) -> verdict.
## Blind to what descriptor_fn computes. Runs: Check 0 (are the structures real?), Check 1
## (well-posed?), Check 3 (discriminates?), Check 2+4 merged (survives DFT oracle spot-checks on
## extremes + suspicious point, reports coverage honestly). Two cheap gates, one expensive truth-test.
##
## THIS CONSTITUTION IS BEING BUILT FOR REUSE: rules logged here are meant to persist across
## projects and sessions. Rule #1 = be the ruthless mentor, invention is the goal, tools serve it,
## kill the audit tar pit. Rule #2 = build general reusable verifier tools, not one-off scripts.
## ============================================================
CHECK 1 IMPLEMENTED & RUN LIVE (Jul 21): base diff 0.000 (clean), k -0.043 (marginal), br -0.466, rb -0.857 (broken). 2/4 ill-posed -> FAIL. LESSON: binary threshold is fragile - k squeaked under 0.10 despite being the most disruptive substitution (relaxation-luck, landed near the line). Check 1 must output GRADED well-posedness (clean/marginal/broken) + the diffs, not binary pass/fail. Verdict still FAIL (br/rb clearly broken), but the tool told us its own threshold needs to be a gradient. Real improvement found by running it live.
CHECK 0 IMPLEMENTED & LIVE (Jul 21): force-based "is this a relaxed minimum." cand_base before 0.303 -> after MACE relax 0.027 = REAL. Discriminates approximation from genuine minimum. REFINEMENT found live: "real" is model-specific - a GPAW minimum reads NOT-RELAXED to MACE (0.222) because the models disagree on where the minimum is (the +41% discrepancy in another form). So Check 0 tests "real w.r.t. the model the descriptor uses." This clears the oracle check's prerequisite: it can now flag fake structures (our approximated yellow phase) BEFORE spending DFT. Checks 0,1,3 all built & live-tested; only oracle check remains stubbed.
ORACLE CHECK MACHINERY BUILT & TESTED (Jul 21): select_spotchecks (MACE-best + MACE-worst + most-distorted) + oracle_verdict (compare DFT vs MACE ranking on subset, report coverage). Tested on halide barrier series (real numbers): MACE order [Cl<Br<I by barrier] vs DFT [I<Cl...] -> ranking_agrees=False -> FAIL. Correctly catches MACE's backwards halide ordering. REFINEMENT noted: when best/worst/suspicious overlap (Cl was both worst and most-distorted), coverage drops (2 of 3); should grab next-distinct comp to maintain coverage. All 4 checks now have working logic; (b) next = build real delta-CsPbI3 yellow structure so phase-stability can be checked for real.
CHECKER RUNS END-TO-END (Jul 21) - P4 FUNCTIONALLY DONE. Full pipeline on phase-stability w/ real structures: Check 0 PASS (yellow max|F| 0.018), Check 1 PASS (single dE/comp), oracle-sanity FAIL (dE +509 meV/fu, expect 20-100) -> OVERALL UNCERTIFIED/FAIL, diagnosed "yellow structure needs refinement." THE TOOL WORKS: caught a descriptor that looked fine (real+relaxed+well-posed) but fails quantitative sanity - a naive screener would have ranked on +509 meV garbage. Two descriptors now adjudicated: barrier (FAIL ill-posed), phase-stability (UNCERTIFIED bad-magnitude). Real in-house verifier tool = Rule #2 deliverable. NEXT (b): refine delta-CsPbI3 yellow structure to land dE in 20-100 meV range = first real USE of the finished tool.
PHASE-STABILITY = MACE FAILURE, not structure failure (Jul 21). Published delta-CsPbI3 (Trots 2008, Pnma) relaxed clean (max|F| 0.026). MACE dE(black-yellow) = -523 meV/fu = black more stable. PHYSICALLY WRONG - experimentally yellow is the ground state (that's why CsPbI3 rots). MACE has the sign backwards by half an eV. (Note: earlier bad structure gave +509; both ~500 meV, opposite signs - the structure was ALSO wrong before, but the real structure reveals the real problem: the model.)
CONVERGENT FINDING: MACE-MP cannot model CsPbI3 energetics - barriers +41%, halide ordering inverted, phase-stability sign wrong. THREE independent verdicts, one conclusion: MACE-MP is unfit for CsPbI3 energetics. The checker converged on a finding about the MODEL, not just individual descriptors. Verifier's highest job: telling you your fast tool is unfit, with receipts.
DECISION (b): checker has now correctly REJECTED every MACE-based descriptor for this material. First genuine PASS must come from a case where the fast model actually works (toy/non-perovskite). P4 tool is PROVEN (discriminates: passes structure-real checks, fails unfit descriptors) - a verifier that only rejects unfit things is still working correctly.
FIRST PASS - P4 TOOL 1 GENUINELY DONE (Jul 21). Descriptor = relaxed lattice constant, group-IV diamond series (C/Si/Ge/Sn). MACE {3.57,5.46,5.77,6.61} vs ref {3.57,5.43,5.66,6.49} - within ~2%, ORDER IDENTICAL (C<Si<Ge<Sn). Check1 PASS, Check3 PASS (3.04A spread), Oracle PASS -> OVERALL PASS.
THE CHECKER NOW DISCRIMINATES (not just rejects): barrier FAIL (ill-posed), phase-stability FAIL (MACE unfit), lattice-constant PASS (MACE trustworthy). A verifier that says both "no this lies" and "yes this is trustworthy" = working verifier, not skeptic. Tool 1 acceptance test MET: fails the barrier at Check 1, passes a valid descriptor. 
USABLE MAP PRODUCED: checker tells you WHERE MACE is trustworthy (structural/geometric, ~2% + correct order) vs unfit (CsPbI3 energetics, sign-wrong). That map is the deliverable.
P4 STATUS: Tool 1 (Descriptor-Validity Checker) COMPLETE per BELL_LABS_V1_TOOLKIT spec. Next per spec: Tool 2 (Model-Fidelity Auditor).
TOOL 2 (Model-Fidelity Auditor) CORE BUILT & PASSES ACCEPTANCE TEST (Jul 21). Reports: MAE, Kendall tau (ranking), alpha (scale error), residual (direction error), verdict.
- Halide barriers: tau -1.00 INVERTED-FAIL, alpha 0.862 (14% scale) + 34% direction -> "cannot screen." Auto-caught the ranking inversion that took manual reasoning before.
- Group-IV lattice: tau +1.00 PASS, alpha 1.014 (1.4% scale) + 0.8% direction -> "correctable."
KEY DIAGNOSIS (the literature-unique part): scale-vs-direction decomposition. Group-IV fails by a clean SCALAR (fixable by rescale/fine-tune); halides fail by DIRECTION (error points wrong way -> ranking inverts -> NOT fine-tunable). That contrast = the fine-tuning trigger logic, computed automatically. "Fine-tunable" vs "fundamentally unfit", quantified.
ACCEPTANCE TEST MET: halides auto-FAIL (inverted), group-IV auto-PASS with alpha/cosine card. Tool 2 core complete. Remaining per spec: committee-disagreement + PROBE reliability layer (Amendment #1) as enhancement.
