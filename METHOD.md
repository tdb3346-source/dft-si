# METHOD — verification doctrine
Rule + receipt. Never a rule without the failure that earned it.
Distinct from LOG.md (what happened) and the TOOLKIT spec (what the tools are).
This is how to JUDGE. Append only when a failure earns an entry.

## M1. Match the protocol between fast model and oracle
Relax in each code's OWN minimum, then apply IDENTICAL strains and the same fit.
Comparing MACE-at-MACE-minimum to GPAW-at-GPAW-minimum with different strain
ladders confounds model error with reference-state error.
RECEIPT: Jul 24 2026 EOS run. Strain ladder (0.94,0.97,1.00,1.03,1.06) and the
eV/A^3->GPa factor were verified identical across pipeline.py and oracle_bulk.py
BEFORE the batch. Commit 39b69d7.

## M2. Run the control that could kill the finding first, and cheapest
Order the oracle batch so the system that would INVALIDATE your claim runs first.
RECEIPT: Jul 24. C (diamond) was MACE's best case (+1% vs expt). If GPAW had
disagreed on C, the protocol was broken and Si/Fe were meaningless. GPAW gave
433.5 vs MACE 446.2 (+2.9%) -> protocol validated, so Si and Fe MEAN something.
Cost of learning this on C instead of after Fe: ~2 hours.

## M3. Pre-register the readings before the number lands
Write what each possible outcome WOULD mean, timestamped, before seeing it.
Prevents hindsight-fitting whichever story the number flatters.
RECEIPT: Jul 24 00:35. Readings A/B/C logged while Fe was still running
(A: 170-200 = finding survives; B: 70-90 = weakens to oracle caveat;
C: anything else = ambiguous, do NOT force). Fe landed 193.3 -> Reading A,
no argument needed. Commit 433af71 (pre-reg) precedes 39b69d7 (result).

## M4. A verdict is scoped or it is not a verdict
State: which decision, which domain, which conditions. "Descriptor X is valid"
is not a claim. Descriptor validity is a property of the tuple
(descriptor + target outcome + candidate domain + conditions + oracle protocol).
RECEIPT: the Jul 24 bulk-modulus result is an INSTRUMENT AUDIT (does the fast
model reproduce the oracle), NOT a screen. It certifies nothing about ranking
candidates for any target outcome. n=3, one MLIP, one functional, one property.

## M5. KNOWN INSTRUMENT LIMITATION — Check 3 passes vacuously cross-material
Check 3 (discriminates vs noise floor) was designed for CANDIDATE COMPOSITIONS
OF ONE MATERIAL. On a grid of chemically unrelated materials it passes trivially
(12 different elements obviously differ in size: spread 3.76 A vs floor 0.02).
Its noise-floor semantics do NOT transfer from composition-screening to
cross-material auditing. Do not read a cross-material Check 3 PASS as evidence.
RECEIPT: Jul 24 on-ramp, flagged BEFORE the run, confirmed after.

## M6. The instrument's own bugs are caught by the instrument — if you let them be
RECEIPT: Jul 24. bulk_modulus_descriptor had a unit conversion off by ~1e-11
(divided by 1.602e-19 then multiplied by 1e-30 instead of multiplying by
160.2176634). All 12 systems returned 0.000. Check 3 returned FAIL
("spread 0.000 vs noise floor 2.000, within noise, can't rank") WITHOUT being
told anything was wrong. The checker refused to certify its author's garbage.

## THE HEADLINE RESULT THIS FILE WAS WRITTEN AROUND (Jul 24 2026)
MACE-MP positional accuracy does NOT transfer to curvature.
Same model, same materials, same run, oracle-verified vs GPAW/PBE:
  lattice constant:  C +0.1%   Si +0.4%   Fe -0.4%    (all 12 systems <2%)
  bulk modulus:      C +2.9%   Si -15.9%  Fe -62.9%
MACE knows where the atoms sit; it does not know how hard it is to squeeze them.
Error magnitude is unpredictable across ordinary elements (Fe worst - magnetism
is the hardest case, and MACE-MP trains on relaxed geometries where curvature is
barely constrained). Scope: n=3 oracle-verified, instrument audit, not a trust map.
