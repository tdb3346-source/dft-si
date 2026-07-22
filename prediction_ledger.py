import json, os, time
from datetime import datetime

LEDGER = "predictions.json"

def _load():
    if os.path.exists(LEDGER):
        return json.load(open(LEDGER))
    return []

def _save(d):
    json.dump(d, open(LEDGER,"w"), indent=2)

def predict(who, question, prediction, band=None):
    """Register a BLIND prediction before the result is known."""
    d = _load()
    entry = {"id": len(d)+1, "who": who, "question": question,
             "prediction": prediction, "band": band,
             "timestamp": datetime.now().isoformat(timespec="seconds"),
             "result": None, "outcome": None}
    d.append(entry); _save(d)
    print(f"#{entry['id']} [{who}] logged: {question} -> {prediction}" + (f" (band {band})" if band else ""))
    return entry["id"]

def resolve(pid, result, outcome):
    """Record the actual result. outcome: 'HIT' or 'MISS'."""
    d = _load()
    for e in d:
        if e["id"]==pid:
            e["result"]=result; e["outcome"]=outcome; _save(d)
            print(f"#{pid} resolved: {result} -> {outcome}")
            return
    print(f"#{pid} not found")

def scorecard():
    """Calibration record per person."""
    d = _load()
    resolved = [e for e in d if e["outcome"]]
    if not resolved:
        print("no resolved predictions yet"); return
    from collections import defaultdict
    by = defaultdict(lambda:[0,0])
    for e in resolved:
        by[e["who"]][0 if e["outcome"]=="HIT" else 1]+=1
    print("=== PREDICTION SCORECARD ===")
    for who,(h,m) in sorted(by.items()):
        print(f"  {who}: {h}/{h+m} HIT ({100*h/(h+m):.0f}%)")
    print(f"  ({len(resolved)}/{len(d)} predictions resolved)")

if __name__ == "__main__":
    # seed with this month's real head-to-head record from LOG.md
    if not os.path.exists(LEDGER):
        predict("Benji","barrier direction MACE vs GPAW","lower","")
        predict("Mentor","barrier direction","higher >10%","")
        predict("Benji","strain error shape","might deviate","")
        predict("Mentor","strain error shape","close to linear ~34/27%","")
        predict("Benji","chloride error","below 11%","")
        predict("Mentor","chloride error","5-10%","")
        # resolve them
        resolve(1,"GPAW 19% lower","HIT"); resolve(2,"GPAW lower","MISS")
        resolve(3,"flat-then-cliff, deviated","HIT"); resolve(4,"not linear","MISS")
        resolve(5,"sign reversed then killed","MISS"); resolve(6,"artifact","MISS")
    scorecard()
