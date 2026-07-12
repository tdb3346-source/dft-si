# Real vs. Fooled-Yourself: The Three Disciplines of Trustworthy Inference

**Status:** Methods section of the lab constitution. Applies to every fit, every surrogate, every claim, in every domain, forever.
**Rule zero:** A good fit is not evidence. In inverse problems, a beautiful fit to insufficient data is the *default failure mode*, not a success.
**Origin:** Expanded from the device-diagnostician conversation (archived). Disciplines 1 and 2 are already field-proven in Project 2; Discipline 3 is scheduled (P5/P7/Era 3).

---

## The One Machine

The three disciplines are not a menu — they are stages of a single loop, and the loop *is* the verifier's inner engine:

> **Prove the engine on planted truth (D1) → fit real data → report intervals, not points (D2) → issue one of three verdicts: supports / rejects / can't tell → if "can't tell," compute which measurement would tell (D3) → measure → refit → tighter → claim.**

Time-to-trust is this loop's cycle time. Every project on the roadmap either runs this loop or builds a part of it.

---

## Discipline 1 — The Synthetic Recovery Test

**One sentence:** Never point an inference engine at real data before proving it can recover truths you planted yourself.

**The intuition.** You calibrate a scale with known weights before weighing unknowns. If a detective method fingers the wrong suspect on a case where you *already know who did it*, it has no business working real cases. Same logic: generate fake data from parameters you chose, then check whether your engine finds them.

### The protocol

1. **Draw ground truths θ\* from your priors** — not one point but a set spanning the space, deliberately including regions near suspected degeneracies. A method can succeed at one spot in parameter space and fail two decades away.
2. **Generate synthetic data with the same forward model you will fit with.** This is deliberate: it isolates the *inference machinery* from *model error*. Know which test you're running — same-model generation (the "inverse crime") cannot detect a wrong physics model. Model adequacy is a separate, later test: generate with a higher-fidelity model, fit with yours, and watch what breaks.
3. **Add honest noise.** Match your instrument's amplitude and structure (heteroscedastic if reality is). The classic self-deception is adding whisper-level Gaussian noise and declaring victory.
4. **Fit from multiple random starts.** Multi-modal landscapes have wrong valleys, and one start can land in one. (Receipt: the TMM problem had three thickness modes at ~67, ~150, and ~365 nm producing near-identical spectra. Gradient descent from one start found one mode and *hid the ambiguity*; the posterior revealed all three.)
5. **Score calibration, not closeness.** The question is not "is θ̂ near θ\*" — it is "does the claimed interval contain θ\* at the claimed rate?" Over ≥100 repeats (fresh θ\* and noise seeds), 90% intervals must catch the truth ~90% of the time. This is the **coverage test**.
6. **Run the progression.** One measurement type first — watch the recovery stay ambiguous. Add measurement types — watch the recovered parameters tighten. That tightening curve *is* the identifiability story, and it is a publishable figure on its own.
7. **Freeze it as a harness.** Pytest-style, rerun on every engine change. Regression insurance: the day you "improve" the fitter is the day it silently breaks, and only the harness will notice.

### Receipts (this discipline has already earned its keep)

- **Project 2 Phase 0:** emcee on the toy line fit — m-coverage 0.915, b-coverage 0.920 at N=200, both within ±2·SE of the 0.90 nominal. The engine was certified *before* it touched the TMM problem.
- **Project 2 Phase 4:** a surrogate with MAE 0.0014 — a beautiful fit by any pointwise standard — produced coverage of 0.65 against a nominal 0.90. The fit looked perfect; the coverage test caught the lie and isolated the surrogate (not the inference method) as the cause. This single result is the strongest argument for the discipline: **without the coverage test, that surrogate ships confident garbage and nobody ever knows.**

### Traps

- Misreading the inverse crime: same-model recovery validates inference, not physics. Don't claim more than the test shows.
- Testing one θ\*, one seed, one noise level. That's an anecdote, not a certification.
- Fitting order-of-magnitude parameters (rates, densities, mobilities) in linear space — optimizers choke; always log-space them.
- Scoring point-estimate closeness while ignoring interval calibration. A close point with a false interval is still a liar.
- Optimistic noise.

### Speed-ups

Start with 1–2 free parameters and freeze the rest; `jax.vmap` over seeds makes 100 repeats nearly free; cache forward solves; make the harness a permanent repo fixture (the `audit_cell` pattern from Project 1, pointed inward).

**Artifact shipped:** recovery scatter (θ̂ vs θ\*), coverage table, and the tightening-with-more-data figure.

---

## Discipline 2 — Uncertainty Is the Result

**One sentence:** The interval is the finding; a point estimate without a width is an opinion.

**The intuition.** "The treasure is 5 km north" and "the treasure is somewhere in this 500 km circle" can share the same central value. Only the width tells you whether to start digging. When your engine outputs "interface recombination = 5×10⁻⁴," the scientific content is almost entirely in the range of values *also* consistent with the data.

### The ladder of methods (cheap → expensive; climb only as far as needed)

1. **Laplace approximation.** At the best fit, compute the Hessian of the loss (`jax.hessian` — nearly free), invert it for the covariance, read σ off the diagonal. Valid when the posterior is a single roughly-Gaussian mode. **The bonus that makes it indispensable:** eigen-decompose the Hessian. Small eigenvalues = flat directions = non-identifiable *combinations*, and the eigenvectors literally name them ("only the product n₁·d is constrained"). This is the sloppy-directions analysis, and it is the cheapest identifiability probe you own. Always work in log-parameter space; track the condition number as a health metric.
2. **Profile likelihood.** Fix one parameter along a grid, re-optimize all others at each point, plot the loss profile. Flat profile = practically non-identifiable from this data. More honest than Laplace when things are non-Gaussian; the standard tool in systems biology for exactly this job.
3. **Full posterior (emcee / NumPyro).** The truth machine, and the *only* rung that finds multiple modes. Price: thousands of forward solves. Use for final claims, model comparison, and any time multi-modality is plausible — which, per your own history, is "check at least once, always."
4. **Ensembles + conformal (for ML surrogates).** Deep ensembles give raw uncertainty; conformal prediction recalibrates it when coverage fails. This is the planned P5 machinery.

### Calibration closes the loop

An interval only means something if Discipline 1 says its coverage holds. **Quantified ≠ calibrated** — the Phase 4 surrogate *reported* uncertainty and the uncertainty was *wrong*. Every uncertainty method on the ladder gets a coverage stamp before its intervals are quoted in a claim.

### The reporting contract

Every number ships as [low, high] at a stated level, plus a verdict: **supports / rejects / can't tell.** If the interval spans the decision-relevant range, the verdict is "can't tell" — a valid, respected, *complete* scientific answer — and control passes to Discipline 3.

### Traps

- Laplace on a multi-modal posterior silently reports one mode as if it were the whole story (the gradient-descent-hid-the-modes lesson, at the uncertainty level).
- Hessian computed in linear space for log-scale parameters — garbage curvature.
- Reporting marginals without correlations. Two parameters can each look "identified" while being jointly degenerate. Corner plot or it didn't happen.
- Confusing residual size (fit quality) with parameter uncertainty (inference quality). They are different quantities and the whole point is that they diverge.

### Speed-ups

Eigen-decompose the Hessian *before* running expensive MCMC — it tells you where the trouble is for the cost of linear algebra. `corner.py` is the standard visualization. Log-space everywhere, always.

**Artifact shipped:** corner plot, Hessian eigenvalue spectrum, coverage stamp.

---

## Discipline 3 — Measurements Chosen to Kill Ambiguity (Optimal Experimental Design)

**One sentence:** Once uncertainty is quantified, the next experiment stops being a guess — you compute which measurement shrinks the decision-relevant uncertainty most per dollar or hour.

**The intuition.** Twenty questions. You don't ask random questions; you ask the one that best splits the remaining possibilities. Given only "the two numbers multiply to 12," the OED question is: which second fact — their sum, their difference, their ratio — pins the answer fastest? Different measurements constrain different directions; the skill is choosing the direction your flat spot points along.

### The mechanics

1. **Enumerate candidate experiments** — measurement types × conditions. In device terms: J–V across light intensities, scan rates, impedance at bias, EQE. In P4 terms: which composition gets the next DFT stamp, which NEB path, which MD temperature. In P5 terms: which literature device to "query" next.
2. **Predict the payoff before paying.** The cheap version: Fisher information is additive across independent experiments. Compute each candidate's Jacobian at the current best fit and ask whether its rows add constraint *along your flat directions* — no real experiment required. Formal criteria: **D-optimality** maximizes the determinant of the information matrix (shrinks the volume of the uncertainty ellipsoid); **A-optimality** minimizes the trace (average variance). The full version: simulate data under the current posterior and compute expected information gain (expected posterior shrinkage).
3. **Choose argmax(information ÷ cost).** Costs are real and asymmetric — an impedance sweep is not priced like a neutral-density filter.
4. **Measure, update, repeat.** Bayesian optimization (Ax/BoTorch) is this identical loop with "maximize the objective" swapped in for "shrink the uncertainty"; the acquisition function is just the shopping rule.

### The poor man's OED (use this first, always)

The flat direction's eigenvector from Discipline 2 tells you what the next measurement must be *sensitive to*. If the degenerate combination is bulk-vs-interface recombination, the winning probe is whichever measurement's Jacobian separates them — intensity-dependent V_oc, in that case. This is exactly why the field's multi-modal fitting result works (one parameter set fit simultaneously to J–V at varied scan rates + intensity-dependent V_oc + impedance + transients collapses the degeneracy): that published result is manual OED, arrived at by experts over years. The engine version computes it per-system, per-day.

### The observable is a design choice too

Receipt from Project 2 Phase 3: Sobol analysis showed mean reflectance *hides* the thickness parameter's influence through oscillatory cancellation. Choosing what to record is as much a design decision as choosing what to vary — pick observables that expose, not average away.

### Where it fires in the roadmap

- **P5 Phase 3** — the retrospective active-learning benchmark is Discipline 3 *measured*: experiments-to-discovery, calibrated vs. uncalibrated vs. random.
- **P7 escalation rule** — "spend the DFT stamp where uncertainty is high AND decision-relevant" is OED in one sentence.
- **Era 3** — the engine writes the sponsored lab's measurement list; the hypothesis ⟷ required-measurements link is the elegant core of the whole diagnostician concept.

### Traps

- Shrinking variance on parameters no claim depends on. Tie OED to the decision, not to global variance.
- Ignoring cost asymmetries.
- Computing expected information gain from an *uncalibrated* posterior — garbage in, confident garbage out. (Disciplines 1–2 are prerequisites, not siblings.)
- Greedy one-step myopia — usually fine, but know it's an approximation.
- Forgetting that a boring replicate can be the optimal experiment when noise, not degeneracy, is the bottleneck.

**Artifact shipped:** ranked next-measurement table with predicted uncertainty shrinkage per unit cost.

---

## Companion Rules (for any comparison between runs)

The three disciplines govern *inference from data*. These five govern *comparisons between experiments*, and every campaign report clears them:

1. **Confound control.** Ask: "what is the dumbest explanation for this result that has nothing to do with my hypothesis?" Rule it out first. A bigger basis set reaching lower energy is not a discovery.
2. **Matched cost.** Never report a win without the cost it was measured at (wall-clock, core-hours, oracle calls). An improvement bought with compute is a purchase, not a finding.
3. **Verified baseline.** Re-run the baseline in the same session, same conditions, same code state. A candidate that beats a baseline you never re-verified is not a result.
4. **Variance before deltas.** Know the seed-to-seed spread before believing an improvement. A delta smaller than the spread is noise, and you say so.
5. **Self-critique before reporting.** Attack the result as a hostile reviewer would, in writing, alongside the result. If it can't survive your own critique, it isn't ready.

---

## Roadmap Hooks

| Discipline | Already ran (receipt) | Fires next |
|---|---|---|
| 1 — Synthetic recovery | P2 Phase 0 coverage 0.915 / 0.920; Phase 4 surrogate bust caught by coverage | P4 Phase 2: MACE out-of-distribution honesty vs. held-out DFT; harness reruns on every engine change |
| 2 — Calibrated uncertainty | Three-mode TMM posterior; Sobol observable finding | P4 Phase 3: migration barriers with ensemble error bars; every claim's interval |
| 3 — Optimal design | Manual precedent: the multi-modal fitting literature; escalation rule specced in P7 | P5 Phase 3 AL benchmark; P7 escalation; Era 3 measurement menu |

---

## The Checklist (clear it before any claim leaves the lab)

- [ ] Engine passed synthetic recovery with coverage at the claimed level (≥100 repeats) before touching real data
- [ ] Multiple starts run / posterior checked for extra modes at least once
- [ ] Order-of-magnitude parameters fit in log space
- [ ] Every reported number carries an interval *and* that interval's calibration status
- [ ] Correlations inspected (corner plot / eigen-spectrum), not just marginals
- [ ] Verdict issued as supports / rejects / **can't tell** — and "can't tell" is a complete answer
- [ ] If "can't tell": next measurement chosen by information-per-cost, not habit
- [ ] Comparison rules cleared: confounds named, cost matched, baseline re-verified, variance known
- [ ] Run logged with code hash, config, seed — the claim is reproducible by a stranger

---

*Predict-before-run is Discipline 1 applied to the human operator. The lab's oldest habit and its newest machinery are the same idea at two scales.*
