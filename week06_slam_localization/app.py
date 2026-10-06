from __future__ import annotations
import argparse
from lab.autosave import load_state, save
from lab.completion import refresh_completion
from lab.navigation import LABELS, current_stage, render_progress, set_stage
from lab.session import initialize, sync_widgets
from lab_config import LAB
from pages import final, intro, mission_1, mission_2, mission_3, preflight, tutorials
PAGES = {
    "intro": intro.render, "tutorial_1": tutorials.render, "tutorial_2": tutorials.render,
    "preflight": preflight.render, "tutorial_3": tutorials.render,
    "mission_1": mission_1.render, "mission_2": mission_2.render,
    "tutorial_4": tutorials.render, "tutorial_5": tutorials.render,
    "mission_3": mission_3.render, "final": final.render,
}

def run_smoke_test():
    from analysis.map_metrics import analyze_pixels, quality_score
    from analysis.localization import trial_passes
    from missions import mission_1 as m1, mission_2 as m2, mission_3 as m3
    pixels = [205] * 100 + [254] * 750 + [0] * 150; metrics = analyze_pixels(40, 25, 255, pixels, .05); metrics["known_fraction"] = .6
    first = {"strategy": "perimeter_then_interior", "duration_minutes": 7, "metrics": metrics, "quality_score": max(50, quality_score(metrics))}; second = {"strategy": "room_by_room", "duration_minutes": 7.5, "metrics": {**metrics, "known_fraction": .65}, "quality_score": 70}
    responses = {**{f"mission_1.{key}": "A detailed evidence-based explanation of the ROS displays, map metrics, causes, and limitations. " * 2 for key in m1.REFLECTIONS}, **{f"mission_2.{key}": "A detailed comparison of strategies, numerical metrics, visible structure, and loop closure evidence. " * 2 for key in m2.REFLECTIONS}}
    responses.update({"mission_1.route.original_prediction": "I will map the perimeter, revisit the starting wall, and watch for unobserved interior space.",
                      "mission_2.strategy.original_prediction": "The second route may improve coverage while reducing early loop closure.",
                      "mission_2.controls": "I will use the same world, robot, map resolution, initial pose, and similar run duration. The path strategy changes, although steering speed may still confound the comparison."})
    assert m1.evaluate(first, responses, True, True).passed; assert m2.evaluate(first, second, responses).passed
    base = {"sample_count": 40, "duration": 20, "convergence_time": 2, "final_covariance": .1, "settled_position_spread": .03, "pose_jump": .02, "scan_retention": 1.0}
    trials = {"good_initial_pose": {"metrics": base}, "incorrect_initial_pose": {"metrics": {**base, "pose_jump": .8}}, "ambiguous_location": {"metrics": {**base, "final_covariance": .22}}, "degraded_sensor": {"metrics": {**base, "final_covariance": .3, "scan_retention": .5}}}
    responses.update({f"mission_3.{key}": "A detailed interpretation of localization evidence, uncertainty, failure, stakeholders, and safe fallbacks. " * 2 for key in m3.REFLECTIONS})
    for condition in m3.CONDITIONS:
        responses[f"mission_3.{condition}.original_prediction"] = "I predict this start will affect the particle cloud and convergence."
        responses[f"mission_3.{condition}.observation"] = "The trial changed the particle spread and I compared the displayed pose with the simulated robot before judging correctness."
        responses[f"mission_3.{condition}.correctness"] = "Uncertain"
    responses["mission_3.policy_reasoning"] = "The rule should slow for a concentrated belief, stop when scan evidence is degraded, and ask for help when convergence fails. A confidently wrong pose could still affect someone nearby."
    assert all(trial_passes(key, value["metrics"]) for key, value in trials.items()); assert m3.evaluate(trials, responses).passed
    print("Week 6 lab smoke test passed.")

def run_streamlit_app():
    import streamlit as st
    st.set_page_config(page_title=LAB.title, page_icon="🗺️", layout="wide"); initialize(st)
    if not st.session_state.get("loaded_autosave"):
        saved = load_state()
        if saved.get("recovery_blocked"):
            st.error(saved["recovery_note"]); st.stop()
        for key in ("stage", "student", "responses", "completed_missions", "checked_evidence_ids",
                    "evidence", "tutorial_complete", "prediction_locks", "visited_stages",
                    "recovered_from_backup"):
            if key in saved: st.session_state[key] = saved[key]
        if saved.get("recovery_note"): st.session_state["recovery_note"] = saved["recovery_note"]
        st.session_state["loaded_autosave"] = True
    if st.session_state.get("recovery_note"): st.warning(st.session_state["recovery_note"])
    status = refresh_completion(st)
    render_progress(st); identity = all(str(value).strip() for value in st.session_state["student"].values())
    preflight_ready = bool(st.session_state["evidence"].get("preflight", {}).get("ready"))
    reviewed = st.session_state["tutorial_complete"]
    access = {
        "intro": True, "tutorial_1": identity, "tutorial_2": reviewed.get("tutorial_1", False),
        "preflight": reviewed.get("tutorial_2", False), "tutorial_3": preflight_ready,
        "mission_1": reviewed.get("tutorial_3", False), "mission_2": status["mission_1"],
        "tutorial_4": status["mission_2"], "tutorial_5": reviewed.get("tutorial_4", False),
        "mission_3": reviewed.get("tutorial_5", False) and status["mission_2"],
        "final": status["mission_3"],
    }
    with st.sidebar.expander("Lab navigation", expanded=True):
        for stage in LAB.stages:
            revisiting = stage in st.session_state.get("visited_stages", [])
            if st.button(LABELS[stage], key=f"nav.{stage}", disabled=not (access[stage] or revisiting) or stage == current_stage(st), width="stretch"): set_stage(st, stage)
    PAGES[current_stage(st)](st)
    sync_widgets(st)
    try: save(st); st.sidebar.caption("Progress auto-saved locally")
    except OSError as error: st.sidebar.error(f"Autosave failed: {error}")

def main():
    parser = argparse.ArgumentParser(description=LAB.title); parser.add_argument("--smoke-test", action="store_true"); args = parser.parse_args(); run_smoke_test() if args.smoke_test else run_streamlit_app()
if __name__ == "__main__": main()
