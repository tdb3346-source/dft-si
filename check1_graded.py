diffs = {"base": 0.000, "k": -0.043, "br": -0.466, "rb": -0.857}
def grade(d):
    a = abs(d)
    if a < 0.02: return "CLEAN"
    if a < 0.10: return "MARGINAL"
    return "BROKEN"
print("CHECK 1 (graded well-posedness):")
for tag, d in diffs.items():
    print(f"  {tag:5s} diff={d:+.3f}  {grade(d)}")
broken = sum(1 for d in diffs.values() if abs(d) >= 0.10)
marg   = sum(1 for d in diffs.values() if 0.02 <= abs(d) < 0.10)
print(f"\n{broken} broken, {marg} marginal -> {'FAIL' if broken else 'PASS (with caveats)' if marg else 'PASS'}")
