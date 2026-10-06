from lab.models import RequirementResult, make_check
from missions.mission_1 import _number
REFLECTIONS = ("comparison", "loop_closure")
def evaluate(first, second, responses):
    m1 = (first or {}).get("metrics", {}); m2 = (second or {}).get("metrics", {})
    strategies = {(first or {}).get("strategy"), (second or {}).get("strategy")}
    req = [
        RequirementResult("runs", "Two valid analyzed maps", bool(m1) and bool(m2), len([x for x in (m1, m2) if x]), "2"),
        RequirementResult("strategies", "Different exploration strategies", len(strategies - {None, ""}) == 2, sorted(x for x in strategies if x), "2 different strategies"),
        RequirementResult("coverage", "Both maps have useful coverage", min(_number(m1.get("known_fraction")), _number(m2.get("known_fraction"))) >= .15, round(min(_number(m1.get("known_fraction")), _number(m2.get("known_fraction"))), 3), "≥ 0.15 each"),
    ]
    for key in REFLECTIONS:
        text = str(responses.get(f"mission_2.{key}", "")).strip(); req.append(RequirementResult(key, key.replace("_", " ").title(), len(text) >= 120, len(text), "≥ 120 characters"))
    prediction = str(responses.get("mission_2.strategy.original_prediction", "")).strip()
    controls = str(responses.get("mission_2.controls", "")).strip()
    req.append(RequirementResult("prediction", "Strategy prediction saved before run", len(prediction) >= 40, len(prediction), "≥ 40 characters"))
    req.append(RequirementResult("controls", "Experimental controls documented", len(controls) >= 100, len(controls), "≥ 100 characters"))
    duration_1 = _number((first or {}).get("duration_minutes"))
    duration_2 = _number((second or {}).get("duration_minutes"))
    comparable = min(duration_1, duration_2) > 0 and abs(duration_1 - duration_2) <= max(duration_1, duration_2) * .25
    req.append(RequirementResult("duration", "Mapping durations within 25%", comparable, (duration_1, duration_2), "similar durations"))
    return make_check("Mission 2 compares two mapping strategies using matched evidence.", req)
