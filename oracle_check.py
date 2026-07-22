import numpy as np

def select_spotchecks(mace_scores):
    """Pick which compositions to DFT-verify: extremes + most-suspicious.
    mace_scores: dict tag -> (score, distortion_metric)"""
    tags = list(mace_scores)
    by_score = sorted(tags, key=lambda t: mace_scores[t][0])
    best, worst = by_score[0], by_score[-1]
    suspicious = max(tags, key=lambda t: mace_scores[t][1])  # most distorted
    picks = list(dict.fromkeys([best, worst, suspicious]))    # dedup, keep order
    return picks

def oracle_verdict(mace_scores, dft_scores):
    """Compare MACE ranking to DFT ranking on the spot-checked subset."""
    picks = select_spotchecks(mace_scores)
    checked = [t for t in picks if t in dft_scores]
    mace_order = sorted(checked, key=lambda t: mace_scores[t][0])
    dft_order  = sorted(checked, key=lambda t: dft_scores[t])
    agree = mace_order == dft_order
    coverage = f"{len(checked)} of {len(mace_scores)}"
    return {"spotchecks": picks, "checked": checked,
            "mace_order": mace_order, "dft_order": dft_order,
            "ranking_agrees": agree, "coverage": coverage,
            "verdict": "PASS" if agree else "FAIL"}

# TEST on the halide barrier series (real DFT + MACE numbers we already have)
# tag -> (mace_barrier, distortion_proxy)   distortion: I=0,Br=1,Cl=2 (heavier swap)
mace = {"I": (0.152, 0), "Br": (0.139, 1), "Cl": (0.108, 2)}
dft  = {"I": 0.108, "Br": 0.126, "Cl": 0.188}
r = oracle_verdict(mace, dft)
for k, v in r.items(): print(f"{k}: {v}")
