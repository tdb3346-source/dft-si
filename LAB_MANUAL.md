# FIELD MANUAL — How to Rebuild the Lab on Any Problem

**Status:** Master reference. Written July 12, 2026, the day Project 3 shipped.
**How to use:** Cold restart → read §0, §8, §10. Everything else is lookup. The repos are the proofs; this file is the map.
**Prime directive:** The repo is the source of truth. This manual included — where they disagree, the repo wins.

---

## §0. The soul, one paragraph

AI made generating candidates, hypotheses, and papers nearly free. The bottleneck of science moved to **verification** — and calibrated trust is the scarce, non-clonable asset. The lab's product is not materials or papers; it is **numbers a stranger should believe**, produced by a loop: trusted oracle → verified surrogate → calibrated uncertainty → chosen next measurement → falsifiable claim. Edison's edge was never ideas — it was the test rig, the notebooks, and ownership of the survivors. Kelly's was naming the system's bottleneck and building the most productive environment per square foot around it. You are building both: the rig is the verifier, the notebooks are the repos, the survivors get provisionals. The tools are public and everyone has them. **The moat is the verification and decision architecture around the tools, plus the public track record of catching lies — including your own.** North-star metric: **time-to-trust** — days from entering a new problem to the first result a stranger should believe.

---

## §1. State of the lab (what exists, where)

| Project | Repo (tdb3346-source/) | What it proved | Flagship results |
|---|---|---|---|
| P1 — SQ calculator + audit | `Perovskite-sq-audit1` | The verification reflex; reproduce-then-audit | 33.68% @ 1.34 eV reproduced; 2 papers flagged (MASnI₃ 33.46%, KSnI₃ 30.21%) |
| P2 — TMM inverse modeling | `tmm-jax` | Fit quality ≠ trustworthy inference | Coverage certification 0.915/0.920; three-mode degeneracy ~67/150/365 nm; surrogate MAE 0.0014 with coverage 0.65 (the bust) |
| P3 — DFT/MLIP layer | `dft-si` | Oracle calibration + surrogate graded on both report cards | Tables in §5; adjudicated oracle; force-vs-lattice headline |

**Environments** (WSL Ubuntu, Miniconda):
- `dft` — GPAW 25.7.0, ASE 3.29.0. The oracle. Never install experiments into it.
- `mace` — mace-torch 0.3.16, CPU torch, ASE 3.29. The surrogate.
- `tmmjax` — Python 3.11, JAX 0.10.1. Project 2's stack (Equinox/Diffrax/emcee).
- Paths: work at `/mnt/c/Users/Buyer/dft-si`; **git push from Windows Anaconda Prompt** (credentials live there).

**Live artifacts (promote, don't rebuild):**
- `three_disciplines_trustworthy_inference.md` — the methods constitution (§4 summarizes).
- **Mechanism menu v0** — perovskite loss mechanisms with IonMonger-anchored priors (SRVs ~7–9 & 23–40 m/s for TiO₂/MAPI/spiro; ion D ≈ 3.5×10⁻¹⁰ cm²/s, density ~5×10¹⁷ cm⁻³; citations inside the file). Feeds P4 Phase 0 and P2 Phase 4.
- `synthetic_harness.py` — executable seed of Discipline 1 (planted degeneracy, Hessian flat-direction catch).
- `LOG.md` in each repo — the ledgers. Predictions, catches, verdicts.
- Planning doc — P4–P7 specs, G-track, parking lot with triggers, Era map.

---

## §2. The transferable method (the ladder)

This is what "the method transfers" means. Ten rungs, in order, for any simulable domain:

1. **Pick the training material**: small/cheap to compute; contains the field's central problem in miniature; deeply studied (ground truth exists to calibrate against). You cannot validate an instrument on a material nobody has measured.
2. **Reproduce one known result from scratch.** Own the machinery. Ship it (repo + README + kill-checks). This is P1's pattern and the fastest cure for impostor doubt.
3. **Kill-checks before trust** — draw from the physics-gate menu (§4). A tool is guilty until it reproduces the known.
4. **Statistical layer before real data**: likelihood → posterior → **coverage certification** on synthetic truth (Discipline 1). The engine that can't recover a planted truth interprets nothing.
5. **Oracle calibration**: converge it (cutoff, k-grid — plateaus or the number is a lie), validate on known materials, then **map its lies** — sign and magnitude, per material. The map *is* the deliverable (§5).
6. **Surrogate on top**: fine-tune from a foundation model; grade it on **both report cards** — equilibrium (lattices) *and* off-equilibrium (forces at matched severity). Document where it breaks (OOD honesty). Publishing the breakage is the credibility artifact.
7. **Every fast number carries an oracle stamp.** Escalation rule: cheap surrogate first; uncertainty above threshold → oracle call. That one if-statement is the decision layer.
8. **Uncertainty is the result** (Discipline 2): Laplace → profile likelihood → full posterior, as needed; intervals mean nothing without a coverage stamp; flat Hessian directions *name* the degeneracies.
9. **Choose the next measurement** (Discipline 3): information gain per cost; the flat direction's eigenvector says what the probe must be sensitive to; the observable itself is a design choice.
10. **Claim → verdict → ownership**: three verdicts (supports / rejects / can't tell); freedom-to-operate scan; if it survives — provisional **before** the repo goes public, then a purchased physical test. Open methods, owned matter.

---

## §3. The constitution (rules, each earned)

### Epistemic
- **A good fit is not evidence.** A beautiful fit to insufficient data is the default failure mode. (P2 Phase 4: MAE 0.0014, coverage 0.65.)
- **Agreement with experiment is not validation.** CsPbI₃ gap lands ~1.79 vs 1.73 exp only because PBE's ~−1 eV and missing-SOC's ~+1 eV cancel. Convergence *restored the disguise*; the sloppy first run had exposed it.
- **Fidelity to oracle ≠ fidelity to nature.** The student agrees with the professor best exactly where the professor is most wrong about reality (§5 tables). MACE trained on PBE reproduces PBE, not the world.
- **Unconverged numbers lie confidently.** The k-point lie: 4³ vs 6³ moved a lattice constant 0.21% — 40× the effect being measured. Convergence is shown, never assumed.
- **Equilibrium fidelity ≠ force fidelity.** Same crystal, same model: a₀ agreement +0.003%, relative force error 24.3%. In-training-set equilibrium answers are memorized homework.
- **Absolute total energies never compare across codes.** Only differences within one method mean anything.
- **Watch scale confounds; register metrics blind; fix the misspecification, never the threshold.** Changing the metric after seeing data is reward hacking.
- **A second model can catch errors, never confirm truths.** Cross-model agreement is correlated error. Only physics gates verify.
- **Surprise is the product.** A lab that never surprises you is a printer.

### Operational
- **Predict before run** — Discipline 1 applied to the human. Timestamped band in LOG.md *first*, scored after, hit or miss. Misses recalibrate you; that's the point.
- **No verdict enters the ledger while a decisive run is pending.** (Catch #13.)
- **The repo is the source of truth** — over session labels, over memory, over the mentor. It beat everyone in this lab at least twice.
- **Outputs are never optional.** Raw terminal text, unedited, whole. "It ran" is not data.
- **Prose goes in files; commands go in shells.**
- **Background-job hygiene**: `nohup ... &` finishes *silently* — the log is the only messenger; run a launch check (~20 s later: tail the log + ls the worker's output file); never end a paste block with `tail -f`; expected-runtime note in the log; WSL window stays open or the VM parks the job.
- **One ship per day.** Ships stay honest when they're rationed.
- **Ledger every catch, both directions.** Mentor errors count double for morale and are logged the same.
- **Every phase ends with a shipped artifact + tool residue** (a reusable module or playbook page). Ten years of that is a factory; without it, a pile of repos.

### Strategic
- **Campaigns pull tools; tools never push campaigns.** The three-names rule before any infrastructure build: name (1) the blocked campaign, (2) the measurement showing the block, (3) the artifact the tool unblocks. No three names, no build.
- **Resolution decays with distance, on purpose.** Build-resolution for the next project only; phase-resolution one out; architecture beyond. Week-level detail for a project a year away is decoration.
- **Just-in-time depth.** The fake goal is always "deeply understand X." Depth is bought per artifact (emcee inside P2, GPAW inside P3).
- **Generators are cheap; gates are the invention.** Never grow a tree on an ungated root. Score ideas as novelty × verified value. Expect single-digit survival rates and celebrate them — unmeasured survival is Kosmos (79% by its own count) and GNoME's 380k.
- **Open methods, owned matter.** Verification tooling, benchmarks, calibration audits: public and loud. Compositions, additives, treatments: provisional filed before the repo goes public. Publishing starts clocks (US 1-yr grace; most of the world zero). Attorney drafts claims — never DIY.
- **Strategy documents post-convergence get three words: "parked pending [next number]."** Sixteen documents from five models converged on the same plan; a seventeenth will too. Numbers terminate; opinions recurse.
- **Tool rankings are frozen.** New tools: one line in the parking lot — name, one-sentence job, trigger. Ranking parked tools is shopping with numbers.

---

## §4. The three disciplines + gates (full text: `three_disciplines_trustworthy_inference.md`)

**D1 — Synthetic recovery:** plant truth, add honest noise, multi-start fit, score *coverage* (intervals contain truth at claimed rate, ≥100 repeats), then the tighten-with-more-data progression. Freeze as a pytest harness; rerun on every engine change.
**D2 — Uncertainty is the result:** ladder Laplace → profile likelihood → full posterior; eigen-decompose the Hessian (small eigenvalues = flat directions = *named* degeneracies); log-space always; corner plot or it didn't happen; every interval carries a coverage stamp. Quantified ≠ calibrated.
**D3 — Optimal next measurement:** Fisher information adds across experiments; candidate's Jacobian must add constraint *along the flat direction*; argmax(information ÷ cost); the observable is a design choice (Sobol receipt: mean reflectance hides d).

**Physics-gate menu** (draw kill-checks from here): dimensional analysis · limiting/asymptotic cases · known special cases · symmetry · sign & monotonicity · conservation laws · order-of-magnitude · independent derivation. Plus the cheap tricks earned this year: R+T+A=1; supercell **extensivity** (N× atoms → exactly N× energy); the √2 tell for primitive cells; zero-thickness limits.

**Companion rules** (for comparisons between runs): confound control ("dumbest explanation first") · matched cost · re-verified baseline, same session · variance before deltas · written self-critique before reporting.

**Output contract:** every claim ships as [low, high] at stated level + one of three verdicts — supports / rejects / **can't tell** — and "can't tell" plus D3's recommendation is a complete, respectable result.

---

## §5. Findings with receipts (carry these in your head)

**The oracle's lie map** (GPAW-PBE vs experiment; sign convention everywhere: (calc − ref)/ref):

| material | a₀ error | gap error | note |
|---|---|---|---|
| Si | +0.83% | ≈ −30% | baseline; converged PW(400), k 6³ (lattice) / 8³ (gap) |
| SrTiO₃ | +1.00% (3.9441 vs 3.905) | −34% (2.110 vs 3.20) | clean control; PW(900) — oxygen 2p needs it; k 6³ |
| CsPbI₃ | +1.59% (6.390 vs 6.290) | **+3.4%** (1.788 vs 1.73, no SOC) | the silent lie, quantified: PBE ↓~1 eV cancels missing-SOC ↑~1 eV; first run (400 eV) showed +22% — convergence restored the disguise |

- Lattice overshoot grows with soft/heavy lattices — systematic PBE family signature.
- **Ablation (Jul 7):** recomputing the gap at the relaxed lattice made the error *worse* (+8%) → lattice ruled out as cause; one variable at a time.
- **Adjudication (Jul 12):** two runs at k=6³ (different cutoffs) agree to 0.002%; k=4³ off by 0.21%. Oracle = **6.390**, defended.

**The surrogate's report cards** (MACE-MP medium, float64, vs my oracle):

| material | a₀ Δ vs oracle | rel. force error (0.05 Å rattle) | abs RMSE (eV/Å) |
|---|---|---|---|
| Si | −0.38% | **40.1%** | 0.315 |
| SrTiO₃ | −0.03% | 7.4% | 0.027 |
| CsPbI₃ | +0.005% | 24.3% | 0.0118 (smallest) |

- **Headline:** same crystal — +0.003% on the lattice, 24.3% on forces. Equilibrium answers for in-training-set crystals are memorized homework; honesty lives off-equilibrium.
- **Design confound (ours):** uniform rattle = non-uniform severity — Si shoved to 1.7 eV/Å (out-of-distribution), CsPbI₃ to 0.15 (in-distribution). The table ranks OOD distance as much as chemistry. Softness measured: ~10× weaker restoring force in the halide for the same shove.
- N=1 snapshot, one seed: ordering robust, ratios ±20%.

**P2 recap:** inference engine coverage-certified (0.915/0.920 @ nominal 0.90, N=200); three thickness modes (~67/150/365 nm) that gradient descent hid and the posterior exposed; a 0.0014-MAE surrogate that broke coverage to 0.65 — the isolating experiment pinned the surrogate, not the inference; Sobol: n₁ dominates reflectance magnitude, d acts through interaction and is hidden by the mean-reflectance observable.

---

## §6. The catch ledger + prediction record

Catches (mentor = C, Benji = B; the immune system's training data):
1–3 · B — mentor physics errors, P1/P2 era (details in those repos' logs)
4 · B — Move 37 artifact judged from its title page; review artifacts, not covers
5 · B — "generation is commodity" over-rotated; steered search made co-flagship with the verifier
6 · both — ASE primitive cell mislabeled as a₀ (the √2 tell)
7 · C, self-reported — **fabricated** an STO reference from memory; it was plausibly close, which is exactly why provenance, not plausibility, is the gate
8 · C — grep pattern skipped .ipynb
9 · C — `tail -f` at the end of a paste block took the terminal hostage
10 · C — narrated the *unconverged* 2.113 eV gap as physics
11 · C — misread the experimental 1.73 as a computed value (disambiguating grep caught it)
12 · C — symmetric starting positions have zero symmetry-breaking force *by construction*; angles-at-90 checked setup, not stability
13 · C — logged a verdict while a decisive cross-check was pending → new rule
14 · C, pre-named — night shift launched from the wrong conda env; `&&` chain failed clean in seconds
(+ mentor runtime calibration 0-for-2: "overnight" STO took minutes; the "quick" cross-check earned its hour)

Scored predictions, final session (write band first, score after — always):
- Si a₀ within ±0.3% → **MISS** (−0.38%) → band recalibrated to ±0.5%
- STO oracle in [3.93, 3.95] → **HIT** (3.9441)
- MACE vs STO oracle ±0.5% → **HIT** (−0.03%)
- CsPbI₃ direction (expands) → **HIT**; ±2% sanity → **HIT**
- "Worst leg" lattice bet (|Δ|>0.4%) → **MISS** (+0.005%, best leg — memorized homework)
- Mentor's 6.3768 adjudication bet → **MISS ×4** (k-point lie claimed the mentor's own cross-check)
- Force bet, absolute (≥2× STO) → **MISS**, pre-flagged scale confound
- Force bet, relative (CsPbI₃ worst) → **MISS** (Si worst, 40.1% — nobody bet on that)

Meta-finding: we are measurably miscalibrated about *where* MLIPs fail. That sentence is the empirical justification for P4 Phase 2.

**Standing pre-registered experiment (P4 opener, both signatures, blind):** matched-severity rattles targeting RMS force ≈ 0.3–0.4 eV/Å (Si ~0.02 Å, STO 0.05, CsPbI₃ ~0.2 Å — also the 300 K-relevant regime) + one GPAW PW(600) self-consistency point on Si to bound reference noise. Prediction: Si rel% collapses below 15; CsPbI₃ rises above STO.

---

## §7. Environment gotchas (the evening-eaters)

- **WSL parks when the last Ubuntu window closes** — takes nohup jobs with it. Window stays open for any background run.
- **WSL clock lies after host sleep.** Check `date` before trusting any file timestamp; fix: `sudo hwclock -s`.
- **Git pushes from Windows Anaconda Prompt** (credentials cached there); compute lives in WSL. Same folder, same .git.
- **ASE `bulk()` returns the primitive cell** — the √2 tell. Use `cubic=True` or convert. Extensivity (N× energy) confirms equivalence for free.
- **Jupyter is optional.** `.py` + terminal ships everything; the notebook server is where evenings historically died.
- MACE: `default_dtype="float64"` for geometry; first call downloads the model; the `weights_only`/`cuequivariance` warnings are benign noise.
- GPAW converged settings on file: Si PW400/k6³ (gap k8³) · STO PW900/k6³ · CsPbI₃ PW600/k6³. New material ⇒ new convergence study, always.
- Fit order-of-magnitude parameters in log space; multiple random starts; save results after every run, not at the end.
- `.gitignore` the `.ipynb_checkpoints` someday. Logs and `.npy` arrays are *provenance*, not mess — they stay.

---

## §8. Rebuild playbook — pointing the lab at a NEW problem

(This is Project 6's skeleton; it is also the generic restart.)

0. **Charter, one page, before anything**: the system's bottleneck this attacks · consequence test ("if answered, what changes?") · available observables · competing mechanisms (2–3, not ten) · success number **declared in advance** (predict-before-run at project scale) · abort criteria · what each task leaves as tool residue.
1. **Training material** by the three criteria: cheap to compute · field's central problem in miniature · deep ground truth exists.
2. **Reproduce one known result** end-to-end with the existing stack. Ship it small.
3. **Oracle discipline on the new chemistry** — new pseudopotentials, new convergence: this is the part that never transfers free.
4. **Fine-tune the surrogate; grade both report cards** (equilibrium + matched-severity forces); publish the breakage map.
5. **Calibrated inference** — reuse the D1–D3 machinery verbatim; it is domain-agnostic by construction.
6. **Hit or miss the pre-declared benchmark.** Either way, log it.
7. **The postmortem is the deliverable**: what transferred untouched, what broke, how much new oracle data was needed, and **time-to-trust measured** (target: ⅓ of the previous domain's). Honest expectation from prior analysis: 30–50% code reuse, 60–80% process/schema/verification-pattern reuse. The breakage list is the difference between "I have a pipeline" and "I have a method."

G-track rules ride along: generator conditioned on corpus/anomalies/contradictions, never vibes; every idea through the novelty + physics gates; append-only log of generation → verdict; hit-rate per gate is the only generator metric.

---

## §9. Roadmap state (as of ship day)

**Shipped:** P1, P2, P3.
**Next action:** P4 Phase 0 — 2–3 week patent + literature scan (Google Patents, Lens.org; white-space map + mechanism menu; menu v0 already exists — promote it). The **first experiment of P4 is already pre-registered** (§6) and runs before/alongside the scan.
**P4** (degradation physics, ~4–6 mo): Phase 0 scan → Phase 1 DFT polymorph ground truth (α/β/γ vs δ; PBE vs PBE+SOC vs hybrid — meet the cancellation deliberately) → Phase 2 fine-tuned MACE + public "where universal MLIPs lie on halide perovskites" benchmark → Phase 3 NEB barriers + finite-T MD with ensemble error bars → Phase 4 one falsifiable stabilization claim, FTO check, provisional if it survives, $5k powder test (contract synthesis + XRD aging). Compressed per the accepted re-scope: one claim, one physical signal, one provisional attempt, kill criteria, Edison metrics weekly.
**P5** (~3–4 mo, laptop-grade "cluster is busy" work): Perovskite Database autopsy → coverage audit (accurate-but-miscalibrated at field scale, conformal recalibration) → identifiability on real data (lab-vs-chemistry confound) → retrospective active-learning benchmark. Plus the upgrades filed: temporal splits, leave-one-lab-out, leakage detection, publication-bias analysis; database is literature-through-2020 + uploads, not a live census.
**P6** (~2–3 mo): the transfer test — Li transport in argyrodite/garnet, §8 executed verbatim, postmortem as product.
**P7** (~3–4 mo): the loop. Phase 0 constitution as an importable module (three-verdict contract; escalation rule; code-verification gates for agent-written solvers: manufactured solutions, conservation, convergence-order; earned autonomy — run duration bought by known-answer pass rate; interface requires `uncertainty_model()` and `falsification_tests()`). Phase 1 you run one full cycle by hand. Phase 2 agents operate inside the harness, bounded, budgeted, logged. Phase 3 campaign report: generated → killed → stamped → claim-grade; cost per trusted result.
**Money/IP gates:** $0 until a claim survives; then ~$3–5k powder test + $2–5k attorney provisional; provisional starts a 12-month convert-or-abandon clock ($15–30k); Era 3 sponsored lab access $20–100k/yr — access, not ownership; file before publish, always.
**Parking lot (triggers written in the planning doc):** device diagnostician (trigger: Era 3 data) · PySR/SINDy (post-P5 distillation; degradation rate laws) · LanceDB (G3 fleet) · C++ kernels (profiler shows an XLA-inexpressible hot loop AND no gradients needed) · continuum missing-term discovery (P4 time series exist) · deltapv fork decision (repo is archived — fork means adopting maintenance; decide fork/rewrite/wrap at trigger time) · InstaDeep `mlip` on the P4 Phase 2 eval list.
**Dashboard (controllable, weekly, replaces "paradigm shifts"):** prospective predictions made · fraction physically tested · calibration of those predictions · time-to-trust · cost per resolved hypothesis · provisionals filed or clean kills.
**Eras:** 1 instrument-maker (done) · 2 first products (P4–P7, now) · 3 matter interface + first hires (~month 18+) · 4 parallel campaigns · 5 the Kelly bet (~yr 8; do not spec early).

---

## §10. Restart protocol (cold start, any gap length)

1. **Open a fresh conversation.** Give it: this manual + the three repo URLs + the tail of each LOG.md. The only handoff in this lab's history that never scrambled is the one where the repo did the briefing.
2. **Demand verification before advice.** The AI's first moves must be `git log --oneline -10` per repo and reading the LOG.md ends. Any statement about your state not grounded in a file it has seen is a hypothesis, and you say so. Repo > labels > memory > vibes.
3. **Treat all AI numbers as hypotheses until sourced.** The catch ledger continues from #15. Mentors get audited; that is how this works — plausible fabrications survive review, only provenance catches them (catch #7 was 0.001 Å from correct).
4. **The tell of the old failure mode:** if the first hour of the restart produces a strategy discussion, a tool ranking, or a graded document instead of a command — stop, and run the smallest pre-registered experiment on the books (there is always one; right now it's the matched-severity force check). Sixteen documents once converged on a plan while zero numbers existed. The cure was five lines of Python.
5. **Rhythm:** prediction in the log → run → paste raw output → score → ship line → one ship per day → tool residue filed.

**If you remember one sentence:** *the lab exists wherever a prediction is written down before the run and scored after it — everything else is furniture.*

---

*Ledger closed July 12, 2026: three projects shipped, fourteen catches logged, one silent lie caught in the wild at 1 AM by the person who once couldn't parse "per m², per nm." The furnace stays warm.*
