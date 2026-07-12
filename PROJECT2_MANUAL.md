# PROJECT 2 FIELD MANUAL — tmm-jax: The One-Year Brush-Off

**Status:** Project-scoped refresher. Written July 12, 2026 (P2 shipped earlier this year; Phase 5 parked with trigger).
**How to use:** Cold return → §0, §4, then whichever of §2/§5 the trigger demands. The repo wins every disagreement with this file.
**Companion:** `LAB_MANUAL.md` (the lab-wide constitution). This file assumes you've skimmed its §0 and §3.

---

## §0. What this project was, one paragraph

Project 2 built the lab's **inference engine** on the simplest honest physics available: a differentiable transfer-matrix optics model (thickness → reflectance R(λ), 400–700 nm) in JAX, with a Bayesian statistical layer on top. The stated goal from the original roadmap: *recover a device's internal parameters from measurements — and, just as important, learn to detect when parameters CANNOT be recovered.* It delivered both, and in doing so produced the lab's two founding empirical lessons: a beautiful fit can hide real non-uniqueness (the three-mode degeneracy), and a surrogate can be pointwise-excellent while statistically dishonest (the coverage bust). Everything in the three-disciplines doc was earned here first. TMM was the barbell, not the trophy — the inference machinery is the asset, and it is domain-agnostic by construction.

---

## §1. State

- **Repo:** `tdb3346-source/tmm-jax`
- **Env:** `tmmjax` — Python 3.11, JAX 0.10.1, emcee for MCMC (Equinox in the stack). **The env is a time capsule: it still works exactly as frozen unless you touch it. Never `pip install -U` inside it.**
- **Phases shipped** (historical order, which was deliberately out of numerical order):
  - **Phase 1** — differentiable TMM forward model; `jax.grad` inversion; the 5-starting-guess identifiability experiment. Kill-checks: R+T+A=1 (any stack, any λ) · bare glass (n≈1.5) → R≈0.04 · d→0 recovers the no-film case.
  - **Phase 0** (done after 1, on purpose) — statistical foundations: likelihood → posterior → **coverage certification** on a toy line fit (m=2, b=5): coverage 0.915 / 0.920 at N=200 vs 0.90 nominal. The engine was certified before it touched TMM. The motivation was Phase 1's own unresolved question — bad minima or real degeneracy? — which is why the statistics stuck.
  - **Phase 2** — surrogate emulator over the forward model.
  - **Phase 3** — Sobol sensitivity analysis.
  - **Phase 4** — Bayesian inversion + identifiability mapping; the central finding (§2.4).
  - **Phase 5** — drift-diffusion capstone: **PARKED** (§5), trigger written, decision logged in dft-si LOG.md and LAB_MANUAL §9.
- **Ship line, scored honestly:** (a) ground-truth recovery from noisy synthetic data with calibrated intervals — ✓ (coverage cert + Phase 4). (b) non-uniqueness made concrete — ✓ at the *parameter* level (three modes, one mechanism). The original ambition of *mechanism-level* comparison (competing physical stories, Bayesian model comparison) was not abandoned — it migrated into the parked device-diagnostician concept and P2 Phase 5's design, where it belongs, because mechanism menus need device physics.

---

## §2. Findings with receipts (carry these)

1. **Coverage certification, 0.915 / 0.920 @ 0.90 nominal (N=200).** The engine can recover planted truth with honest intervals. This is Discipline 1's origin and the precondition for trusting anything downstream.
2. **The three-mode degeneracy, ~67 / 150 / 365 nm.** Different thicknesses produce near-identical reflectance spectra (interference orders). Gradient descent from one start found one mode and *hid the ambiguity*; the posterior exposed all three. The "bad local minima" hypothesis was wrong — it was real optical non-uniqueness. **Parable attached:** this flagship finding began life as a "20-minute loss-value check" deferred through an entire session of roadmap-admiring. The postponed tiny check *was* the discovery. Remember that shape.
3. **Sobol:** n₁ dominates reflectance magnitude; d acts primarily through interaction — and the *mean-reflectance observable hides d* via oscillatory cancellation. The observable is a design decision (Discipline 3's seed).
4. **The surrogate bust — the project's crown jewel.** A surrogate with **MAE 0.0014** (pointwise superb) produced credible-interval **coverage 0.65 vs 0.90 nominal**. The isolating experiment: real-TMM inference stayed calibrated under identical conditions → the surrogate, not the inference machinery, was the liar. Doctrine minted: **quantified ≠ calibrated**; a good fit is not evidence; and the *isolating-experiment pattern* (swap one component, hold the rest) is how you assign blame in a pipeline.
5. **The kill-check trio** (energy conservation, known-value anchor, limiting case) remains the project's regression suite — cheapest bug-catchers in the codebase.

---

## §3. Code map (layers, not filenames)

Conceptual architecture, top to bottom: **forward model** (TMM, complex-valued, differentiable) → **gradient inversion** (`jax.grad` path; the Phase 1 artifact) → **statistical layer** (likelihood, priors, emcee posterior, coverage harness) → **surrogate layer** (emulator + the calibration comparison machinery) → **sensitivity layer** (Sobol) → **kill-check suite**.

**Honesty note (constitutional):** this manual was written without a live listing of the repo's tree, and per catch #7 the lab does not fabricate file names. **Completion task at commit time (2 minutes):** paste `ls -R` (or the README's structure section) below this line, so future-you maps layers → files without archaeology.

> `[PASTE FILE TREE HERE]`

The repo's own README is the canonical entry point; if this section and the README disagree, the README wins.

---

## §4. Warm-up protocol (≈45 minutes, in order)

1. `conda activate tmmjax` — do **not** update anything. If the env is missing (new machine), rebuild from the exported `environment.yml` if one exists; if it doesn't, that's your first commit: export it *before* touching code. JAX's ecosystem moves fast; the pinned env is the compatibility guarantee.
2. Smoke test: `python -c "import jax; print(jax.__version__)"` and run the forward model on one known input.
3. **Run the kill-check trio.** They are the regression suite; green means the physics core survived storage.
4. **Re-run the coverage certification** (the Phase 0 harness / `synthetic_harness.py` pattern). If coverage still lands ~0.90, the inference engine is certified-after-storage and you may trust it again. If it doesn't — stop, that's the day's work, and it's Discipline 1 doing its job.
5. Read the repo's LOG end-to-end. Only then touch code.
6. Rhythm resumes per LAB_MANUAL §10: prediction → run → raw output → score → ship.

---

## §5. Phase 5 — the parked capstone (read only when the trigger fires)

**Trigger, verbatim from the ledger:** *a P4 atomistic claim needs device-level translation (barrier → JV/stability under bias), OR Era 3 device data exists.* Until one of those is true, this section is scheduled, not pending — do not re-litigate (the supersession of the old "PDE block" plan is logged).

**What it is:** a time-dependent drift-diffusion device model (Poisson + carrier continuity + **mobile ions** — mandatory for perovskite hysteresis; standard DD omits them) with the P2 inference machinery bolted on top, so that microscopic inputs (migration barriers → D(T)) become device observables (JV(t), PL(t)) with calibrated uncertainty, and competing mechanisms can be *compared*, not just fit.

**Design decisions already made — do not re-derive:**
- **deltapv** is the reference implementation (JAX, differentiable via implicit function theorem, MIT) but its repo is **archived**: at trigger time choose consciously between a disciplined fork (you adopt maintenance), a smaller purpose-built solver, or wrapping a maintained simulator and differentiating only the needed layer.
- **Stiffness discipline:** carrier densities go like exp(qV/kT). Scharfetter–Gummel discretization; differentiate through the *converged solve* (implicit diff / adjoints), never unroll the Newton loop; finite-difference-check gradients before any optimization campaign.
- **Kill-check tying P1 in:** as non-radiative losses → 0, efficiency approaches but never exceeds the Shockley–Queisser ceiling at that bandgap. Assert it.
- **The degeneracy-breaker is multi-modal fitting, designed in from the start, not bolted on:** one parameter set fit *simultaneously* to J–V at varied scan rates + intensity-dependent V_oc + impedance + transients collapses the bulk-vs-interface (and ion) ambiguities that any single curve leaves open. Published, validated; the citation lives in the mechanism menu file.
- **Synthetic recovery first, always** — generate device data with known parameters before fitting anything real (Discipline 1 at device scale).
- **Hypothesis-spec schema:** a hypothesis = a configuration over one model — mechanisms on/off, parameters fixed/free, priors — compared in slates, with the three-verdict output (supports / rejects / **can't tell**). This is the parked device-diagnostician's skeleton.
- **Inputs it consumes from P4:** computed barriers and D(T), the populated mechanism menu (v0 exists now, IonMonger-anchored priors inside), possibly powder-test aging data.

---

## §6. What P2 taught the lab (doctrine origins ledger)

- *A good fit is not evidence* — coverage is (finding 4).
- *Quantified ≠ calibrated* — the surrogate reported uncertainty and the uncertainty was wrong.
- *Gradient descent hides modes* — multi-start and posterior checks are law (finding 2).
- *The observable is a design decision* — mean reflectance hid d (finding 3).
- *The isolating experiment* — swap one component to assign blame; this pattern later adjudicated the P3 oracle dispute.
- *The deferred tiny check is often the discovery* — the loss-value parable. When avoidance and a 20-minute measurement compete, the measurement wins.
- Downstream flows: the coverage harness → Discipline 1 and `synthetic_harness.py`; the identifiability muscle → P5's real-data phase and the diagnostician; the calibration machinery → P4's barrier error bars.

---

## §7. Gotchas (P2-specific)

- **JAX version churn is the #1 storage risk.** The frozen env is the defense; migrating machines without an exported `environment.yml` is how you lose a day to API archaeology.
- Complex numbers in TMM are phase bookkeeping — JAX handles them; don't hand-manipulate.
- Order-of-magnitude parameters fit in **log space**; linear-space fitting was the classic early bug.
- One optimizer start is a vote, not a verdict — the three-mode lesson, permanently.
- Wavelength units: everything in nm, end to end; unit drift between the spectrum file and the model was the cheapest historical error class.
- The mean-reflectance trap generalizes: before trusting any scalar summary of a spectrum, ask what it averages away.

---

## §8. Restart protocol

Fresh conversation. Provide: this manual + LAB_MANUAL + the repo URL + LOG tail. The AI's first moves: `git log --oneline -10`, read the LOG, run the kill-checks — *then* advice. Any claim about this codebase not grounded in a file it has seen is a hypothesis and gets said so. The catch ledger is shared with the lab manual and continues from #15.

*One sentence, if the year erased everything else: this project proved that the fit can be perfect while the answer is not unique and the confidence is a lie — and built the machinery that tells you which is which. That machinery is the part you came back for.*
