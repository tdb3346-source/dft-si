import numpy as np, re

def parse_bfgs(logfile):
    steps=[]
    for line in open(logfile):
        m = re.search(r'BFGS:\s+(\d+).*?\s([\d.]+)\s*$', line.strip())
        if m: steps.append((int(m.group(1)), float(m.group(2))))
    return steps

def audit_run(logfile, fmax_target=0.05, min_per_step=40, budget_hours=8):
    steps = parse_bfgs(logfile)
    if len(steps) < 3:
        print(f"{logfile}: too few steps"); return
    f = np.array([s[1] for s in steps]); n=len(f)
    converged = f[-1] < fmax_target
    tail = f[max(0,n-min(10,n//2)):]
    slope = np.polyfit(range(len(tail)), tail, 1)[0]
    # estimate steps-to-target at current rate
    if slope < -1e-5:
        steps_left = (f[-1]-fmax_target)/(-slope)
        hours_left = steps_left*min_per_step/60
    else:
        steps_left, hours_left = np.inf, np.inf
    if converged:
        v = "HEALTHY - converged"
    elif hours_left <= budget_hours:
        v = f"IN PROGRESS - ~{hours_left:.1f}h to target, within budget"
    elif np.isfinite(hours_left):
        v = f"KILL - descending but ~{hours_left:.0f}h to target (>{budget_hours}h budget). Take partial, result UNCONVERGED"
    else:
        v = "KILL - stalled/rising. Result UNCONVERGED"
    print(f"=== RUN AUDIT: {logfile} ===")
    print(f"  steps {n}, fmax {f[0]:.2f}->{f[-1]:.3f}, rate {slope:+.4f}/step")
    print(f"  est. {steps_left:.0f} steps / {hours_left:.1f}h to target")
    print(f"  VERDICT: {v}\n")

for lg in ["cl_gpawneb_bfgs.log", "ob_bfgs.log"]:
    try: audit_run(lg)
    except Exception as e: print(f"{lg}: {e}")
