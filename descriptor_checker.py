"""
DESCRIPTOR-VALIDITY CHECKER  -  v1 skeleton
============================================
Constitution Rule #2: a GENERAL, reusable verifier tool. It is blind to what a
descriptor computes. You hand it a scoring function and a set of compositions;
it interrogates that function for the ways descriptors lie and returns a verdict.

This is a SKELETON: the architecture is real, the check internals are TODO stubs
that currently return a placeholder verdict. The point is to lock the SHAPE first.

Acceptance test (when internals are filled in): fed the two descriptors below,
whose answers we already know, it must return:
    barrier          -> FAIL at Check 1 (ill-posed for mixed compositions)
    phase_stability  -> FAIL at the oracle check (discriminates on the wrong axis)
...without being told those answers.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Any
import numpy as np


# ---------------------------------------------------------------------------
# The plug-in contract: what a "descriptor" IS to this tool.
# ---------------------------------------------------------------------------
# A descriptor is ANY function that scores one composition and returns either:
#   - a float (the descriptor value), or
#   - None  (meaning "this descriptor is not well-defined for this composition")
# The checker never looks inside it. It only calls it and interrogates the results.
#
#   descriptor_fn(composition) -> float | None
#
# A "composition" is an opaque object the descriptor knows how to score
# (e.g. a dict of substitutions, a structure, a formula). The checker treats it
# as a black box too - it only passes compositions to the descriptor.
# ---------------------------------------------------------------------------

DescriptorFn = Callable[[Any], float | None]


class Verdict(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIPPED = "SKIPPED"          # gate upstream failed, so this check wasn't run
    UNCERTIFIED = "UNCERTIFIED"  # ran, but coverage too low to trust (honest lite mode)


@dataclass
class CheckResult:
    name: str
    verdict: Verdict
    detail: str                  # plain-English why
    numbers: dict = field(default_factory=dict)   # the evidence


@dataclass
class ValidityReport:
    descriptor_name: str
    checks: list = field(default_factory=list)
    overall: Verdict = Verdict.SKIPPED

    def card(self) -> str:
        lines = [f"DESCRIPTOR-VALIDITY REPORT: {self.descriptor_name}",
                 "=" * 52]
        for c in self.checks:
            lines.append(f"  [{c.verdict.value:11s}] {c.name}")
            lines.append(f"               {c.detail}")
            if c.numbers:
                nums = "  ".join(f"{k}={v}" for k, v in c.numbers.items())
                lines.append(f"               {nums}")
        lines.append("-" * 52)
        lines.append(f"  OVERALL: {self.overall.value}")
        return "\n".join(lines)


# ===========================================================================
# THE CHECKS  -  each takes (descriptor_fn, compositions, oracle_fn, config)
# and returns a CheckResult. Internals are TODO stubs for now.
# ===========================================================================

def check0_structures_real(descriptor_fn, compositions, oracle_fn, cfg) -> CheckResult:
    """
    CHECK 0 - Are the structures the descriptor is computed on REAL?
    Forced into existence by the phase-stability failure: a descriptor computed on
    a fake/approximated structure gives a precise number for the wrong geometry.
    TODO: how does a GENERAL tool know if a structure is real? Candidate tests:
      - is it at a relaxed local minimum (forces near zero)?  <- automatable
      - was it flagged 'approximated' by the descriptor's own metadata?
      - does it match a known reference (space group / density) if one exists?
    For now: STUB. Returns PASS with a warning that Check 0 is not implemented.
    """
    return CheckResult(
        name="Check 0: structures real",
        verdict=Verdict.PASS,
        detail="STUB - not yet implemented. Real version must verify structures are "
               "relaxed minima, not approximations.",
        numbers={},
    )


def check1_well_posed(descriptor_fn, compositions, oracle_fn, cfg) -> CheckResult:
    """
    CHECK 1 - Is the descriptor a single well-defined number per composition?
    The barrier FAILED this: mixed compositions broke site-equivalence, so the
    descriptor returned None (or an inconsistent value) for 3 of 4.
    TEST (real version): call descriptor_fn on each composition. Count how many
    return None or fail an internal self-consistency flag. If a meaningful
    fraction are ill-defined, FAIL.
    TODO: fill in. For now, STUB using the None-count logic sketched.
    """
    # sketch of the real logic (safe to run, but treat as provisional):
    values = []
    n_illposed = 0
    for comp in compositions:
        try:
            v = descriptor_fn(comp)
        except Exception:
            v = None
        if v is None:
            n_illposed += 1
        else:
            values.append(v)
    frac = n_illposed / max(len(compositions), 1)
    # graded: CLEAN (<0.02) / MARGINAL (<0.10) / BROKEN (>=0.10) done upstream by descriptor
    verdict = Verdict.FAIL if frac > cfg.get("illposed_tolerance", 0.25) else Verdict.PASS
    return CheckResult(
        name="Check 1: well-posed (graded)",
        verdict=verdict,
        detail=f"{n_illposed}/{len(compositions)} broken. "
               + ("FAIL - not well-defined for enough compositions." if verdict == Verdict.FAIL
                  else "PASS."),
        numbers={"n_broken": n_illposed, "n_total": len(compositions), "frac": round(frac, 2)},
    )


def check3_discriminates(descriptor_fn, compositions, oracle_fn, cfg) -> CheckResult:
    """
    CHECK 3 - Do compositions differ by more than noise?
    Phase-stability PASSED this (spread 110 meV vs ~10 meV noise floor).
    TEST (real version): compute spread of well-defined values, compare to a
    noise floor. Spread < floor -> FAIL (can't rank if everything scores alike).
    TODO: fill in noise-floor estimation. For now, STUB using raw spread.
    """
    values = []
    for comp in compositions:
        try:
            v = descriptor_fn(comp)
        except Exception:
            v = None
        if v is not None:
            values.append(v)
    if len(values) < 2:
        return CheckResult("Check 3: discriminates", Verdict.SKIPPED,
                           "Fewer than 2 well-defined values; can't assess spread.", {})
    spread = max(values) - min(values)
    floor = cfg.get("noise_floor", 0.010)
    verdict = Verdict.PASS if spread > 2 * floor else Verdict.FAIL
    return CheckResult(
        name="Check 3: discriminates",
        verdict=verdict,
        detail=f"spread {spread:.3f} vs noise floor {floor:.3f}. "
               + ("PASS - separates compositions." if verdict == Verdict.PASS
                  else "FAIL - within noise, can't rank."),
        numbers={"spread": round(spread, 4), "noise_floor": floor},
    )


def check_oracle(descriptor_fn, compositions, oracle_fn, cfg) -> CheckResult:
    """
    THE MERGED CHECK (old Check 2 + Check 4) - the expensive truth-test.
    Does the fast descriptor's RANKING survive the oracle (DFT) on spot-checks?
    This catches BOTH failure modes at once:
      - fidelity failure (fast model disagrees with DFT on order) - the halide barrier
      - wrong-axis failure (descriptor ranks on a confound) - phase-stability
    ...because the oracle IS the correct axis. If DFT disagrees with the fast
    ranking on the spot-checked subset, the descriptor is not trustworthy.

    SPOT-CHECK STRATEGY (decided): the EXTREMES + the SUSPICIOUS point.
      - fast-model best and fast-model worst (if DFT flips them, ranking is dead)
      - plus any composition flagged physically suspicious (e.g. largest lattice
        mismatch), which is where a confound hides.
    HONEST COVERAGE: report N-checked-of-M. Low coverage -> UNCERTIFIED, not PASS.

    TODO: this needs oracle_fn (DFT) wired to real structures. Until Check 0 is
    real (structures real), this check cannot run truthfully. For now: STUB.
    """
    if oracle_fn is None:
        return CheckResult(
            name="Check 2+4: survives oracle (fidelity + correct axis)",
            verdict=Verdict.UNCERTIFIED,
            detail="STUB - no oracle provided. This is the expensive DFT spot-check. "
                   "Strategy: extremes + suspicious point, report coverage honestly. "
                   "Cannot certify a descriptor without it.",
            numbers={"coverage": "0 of N"},
        )
    # real logic will go here
    return CheckResult("Check 2+4: survives oracle", Verdict.UNCERTIFIED,
                       "oracle wired but logic not implemented", {})


# ===========================================================================
# THE ENGINE  -  runs checks in order, short-circuits on gate failures.
# ===========================================================================

def validate_descriptor(descriptor_fn, compositions, descriptor_name="unnamed",
                        oracle_fn=None, config=None) -> ValidityReport:
    """
    General entry point. Blind to what descriptor_fn computes.
    Runs: Check 0 -> Check 1 -> Check 3 -> oracle check.
    Cheap gates (0,1,3) first; expensive oracle check last, only if gates pass.
    A gate FAIL short-circuits: downstream checks are SKIPPED (don't waste DFT).
    """
    cfg = config or {}
    report = ValidityReport(descriptor_name=descriptor_name)

    gate_order = [check0_structures_real, check1_well_posed, check3_discriminates]
    gates_passed = True
    for check in gate_order:
        result = check(descriptor_fn, compositions, oracle_fn, cfg)
        report.checks.append(result)
        if result.verdict == Verdict.FAIL:
            gates_passed = False
            break   # short-circuit: don't run the expensive oracle on a dead descriptor

    if gates_passed:
        report.checks.append(check_oracle(descriptor_fn, compositions, oracle_fn, cfg))
    else:
        report.checks.append(CheckResult(
            "Check 2+4: survives oracle", Verdict.SKIPPED,
            "Skipped - a cheap gate already failed. No point spending DFT.", {}))

    # overall verdict
    verdicts = [c.verdict for c in report.checks]
    if Verdict.FAIL in verdicts:
        report.overall = Verdict.FAIL
    elif Verdict.UNCERTIFIED in verdicts:
        report.overall = Verdict.UNCERTIFIED
    else:
        report.overall = Verdict.PASS
    return report


# ===========================================================================
# TWO TEST DESCRIPTORS  -  answers known, used to prove the engine works.
# These are STUBS returning canned behaviour matching what we measured, so you
# can run the skeleton end-to-end today. Real versions call MACE/GPAW.
# ===========================================================================

def barrier_descriptor(composition):
    """
    Migration-barrier descriptor. KNOWN TO FAIL Check 1 (ill-posed for mixed comps).
    Stub reflects the measured result: well-defined only for the pure base comp;
    None for any substituted composition (endpoint gate failed 3 of 4).
    """
    if composition.get("subs"):        # any substitution present
        return None                    # ill-posed - endpoint equivalence broke
    return 0.151                        # base: the one clean MACE barrier


def phase_stability_descriptor(composition):
    """
    Phase-stability descriptor (black-yellow). Well-posed & discriminates, but the
    APPROXIMATED yellow phase makes it rank on lattice-disruption, not stability.
    Stub reflects measured meV/fu values.
    """
    table = {"base": 88.3, "br": 125.3, "rb": 166.8, "k": 198.7}
    return table.get(composition.get("tag"), None)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    comps = [
        {"tag": "base", "subs": None},
        {"tag": "br",   "subs": [("I", "Br", 6)]},
        {"tag": "rb",   "subs": [("Cs", "Rb", 2)]},
        {"tag": "k",    "subs": [("Cs", "K", 2)]},
    ]

    print(validate_descriptor(barrier_descriptor, comps,
                              descriptor_name="migration_barrier").card())
    print()
    print(validate_descriptor(phase_stability_descriptor, comps,
                              descriptor_name="phase_stability (approx yellow)").card())
