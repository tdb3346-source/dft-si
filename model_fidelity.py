import numpy as np
from itertools import combinations

def kendall_tau(a, b):
    """Rank agreement, -1 (inverted) to +1 (identical)."""
    n = len(a); c = d = 0
    for i,j in combinations(range(n),2):
        s = np.sign(a[i]-a[j]) * np.sign(b[i]-b[j])
        if s>0: c+=1
        elif s<0: d+=1
    return (c-d)/(c+d) if (c+d) else 0.0

def fidelity_audit(name, fast, oracle):
    """fast, oracle: dict tag->value. Reports the fidelity card."""
    tags = list(fast)
    f = np.array([fast[t] for t in tags]); o = np.array([oracle[t] for t in tags])
    # absolute error
    mae = np.mean(np.abs(f-o))
    # ranking agreement
    tau = kendall_tau(f, o)
    rank_verdict = "PASS" if tau > 0.5 else ("INVERTED-FAIL" if tau < 0 else "WEAK-FAIL")
    # scale vs direction: fit f ~ alpha*o (scale error) and residual
    alpha = float(np.dot(f,o)/np.dot(o,o))
    resid = f - alpha*o
    scale_err = abs(alpha-1)*100
    direction_err = float(np.linalg.norm(resid)/np.linalg.norm(o))*100
    print(f"=== MODEL-FIDELITY AUDIT: {name} ===")
    print(f"  MAE: {mae:.4f}")
    print(f"  Ranking (Kendall tau): {tau:+.2f} -> {rank_verdict}")
    print(f"  Scale error (alpha={alpha:.3f}): {scale_err:.1f}% off unity")
    print(f"  Direction error (residual): {direction_err:.1f}%")
    # overall
    if rank_verdict != "PASS":
        v = "FAIL - ranking not preserved, cannot screen"
    elif scale_err < 50 and direction_err < 20:
        v = "PASS - correctable (mostly scale error, ranking holds)"
    else:
        v = "MARGINAL - ranking holds but large/complex error"
    print(f"  VERDICT: {v}\n")
    return {"tau":tau, "alpha":alpha, "verdict":v}

# TEST 1: halide barriers (known to invert -> must FAIL)
fidelity_audit("halide barriers",
    fast={"I":0.152,"Br":0.139,"Cl":0.108},
    oracle={"I":0.108,"Br":0.126,"Cl":0.188})

# TEST 2: group-IV lattice constants (known correct -> must PASS)
fidelity_audit("group-IV lattice",
    fast={"C":3.57,"Si":5.455,"Ge":5.773,"Sn":6.612},
    oracle={"C":3.567,"Si":5.431,"Ge":5.658,"Sn":6.489})
