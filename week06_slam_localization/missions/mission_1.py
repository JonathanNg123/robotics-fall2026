from lab.models import RequirementResult, make_check
import math
REFLECTIONS = ("system_observation", "map_interpretation", "limitations", "drift_and_revisit")


def _number(value, default=0):
    try:
        result = float(value)
        return result if math.isfinite(result) else default
    except (TypeError, ValueError):
        return default


def evaluate(evidence, responses, has_yaml, has_image):
    metrics = (evidence or {}).get("metrics", {})
    req = [
        RequirementResult("files", "Matching map YAML, PGM, and analysis supplied", has_yaml and has_image, f"YAML={has_yaml}, image={has_image}", "validated pair"),
        RequirementResult("coverage", "Known map coverage", _number(metrics.get("known_fraction")) >= .15, round(_number(metrics.get("known_fraction")), 3), "≥ 0.15"),
        RequirementResult("resolution", "Valid resolution", 0 < _number(metrics.get("resolution")) <= .10, metrics.get("resolution", "missing"), "0–0.10 m/cell"),
        RequirementResult("quality", "Map quality score", _number((evidence or {}).get("quality_score")) >= 45, (evidence or {}).get("quality_score", 0), "≥ 45"),
    ]
    for key in REFLECTIONS:
        text = str(responses.get(f"mission_1.{key}", "")).strip(); req.append(RequirementResult(key, key.replace("_", " ").title(), len(text) >= 100, len(text), "≥ 100 characters"))
    plan = str(responses.get("mission_1.route.original_prediction", "")).strip()
    req.append(RequirementResult("route", "Route plan saved before mapping", len(plan) >= 40, len(plan), "≥ 40 characters"))
    return make_check("Mission 1 includes a usable map and an evidence-based explanation.", req)
