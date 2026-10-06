"""Current-evidence checks shared by navigation and final submission."""
import hashlib

from lab.autosave import CONTENT_VERSION, read_json, submission_root
from lab.evidence import evidence_id
from lab_config import LAB


def current_signature(st, mission):
    responses = {key: value for key, value in st.session_state["responses"].items() if key.startswith(mission + ".")}
    predictions = {
        key: value for key, value in st.session_state.get("prediction_locks", {}).items()
        if key.startswith(mission + ".")
    }
    evidence = st.session_state["evidence"].get(mission)
    context = None
    if mission == "mission_2":
        context = st.session_state["evidence"].get("mission_1")
    elif mission == "mission_3":
        selected = st.session_state["responses"].get("tutorial_4.selected_map")
        selected_mission = "mission_1" if selected == "Mission 1" else "mission_2"
        context = {
            "selected_map": selected,
            "reason": st.session_state["responses"].get("tutorial_4.map_choice"),
            "selected_evidence": st.session_state["evidence"].get(selected_mission),
        }
    return evidence_id(CONTENT_VERSION, mission, st.session_state["student"].get("course_id"), context, evidence, responses, predictions)


def saved_matches(mission, signature):
    root = submission_root() / mission
    try:
        record = read_json(root / "submission.json")
        hashes = record["artifact_hashes"]
        if record.get("lab_id") != LAB.id or record.get("state_signature") != signature:
            return False
        if not isinstance(hashes, dict) or not {"explanation.md", "evidence.json"}.issubset(hashes):
            return False
        if mission in ("mission_1", "mission_2") and not {"map.yaml", "map.pgm"}.issubset(hashes):
            return False
        if mission in ("mission_1", "mission_2") and not any(name.startswith("rviz_screenshot.") for name in hashes):
            return False
        if mission == "mission_3" and not all(f"trial_{name}.json" in hashes for name in (
            "good_initial_pose", "incorrect_initial_pose", "ambiguous_location", "degraded_sensor"
        )):
            return False
        if mission == "mission_3" and len([name for name in hashes if name.startswith("rviz_")]) < 2:
            return False
        return all(
            (root / name).is_file() and hashlib.sha256((root / name).read_bytes()).hexdigest() == digest
            for name, digest in hashes.items()
        )
    except (OSError, ValueError, TypeError, KeyError):
        return False


def mission_status(st):
    return {
        mission: bool(
            st.session_state["checked_evidence_ids"].get(mission) == current_signature(st, mission)
            and saved_matches(mission, current_signature(st, mission))
        )
        for mission in LAB.missions
    }


def refresh_completion(st):
    status = mission_status(st)
    st.session_state["completed_missions"] = [mission for mission, valid in status.items() if valid]
    return status
