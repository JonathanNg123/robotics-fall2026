from pathlib import Path

from lab.autosave import submission_root
from lab.completion import current_signature, mission_status
from lab.controls import prediction
from lab.evidence import artifact, evidence_id, load_json, runtime_map, validate_map_bundle
from lab.navigation import set_stage
from lab.session import complete_mission
from lab.submissions import save_mission
from lab.ui import render_check, show_map, text_response
from missions.mission_2 import evaluate

ROOT = Path(__file__).resolve().parents[1]


def render(st):
    st.header("Mission 2 — Compare mapping strategies")
    first = st.session_state["evidence"].get("mission_1")
    st.write("Map the same world again with a meaningfully different route. Keep the world, robot, map settings, and approximate duration fixed; reset Gazebo and SLAM between runs.")
    st.subheader("1. Predict before run two")
    forecast = prediction(
        st, "mission_2.strategy", {"first_evidence_id": evidence_id(first), "world": "turtlebot3_world"},
        "Name both routes. Predict which will improve coverage, continuity, and loop closure, and why.",
        min_chars=40,
    )
    if forecast is None:
        return
    text_response(st, "mission_2.controls", "Record both start poses, route differences, approximate speed, actual durations, and what else you kept the same. What could still confound the comparison?")

    st.subheader("2. Run and save the comparison map")
    st.write("Stop the first launch, restart a clean world and SLAM, then follow the second route. Do not run two mapping systems in the same ROS domain.")
    st.code(
        "bash scripts/launch_mapping.sh\n"
        "# In a second sourced terminal, after mapping:\n"
        "mkdir -p runtime/maps/mission2\n"
        "ros2 run nav2_map_server map_saver_cli -f runtime/maps/mission2/map\n"
        "python3 scripts/analyze_map.py --yaml runtime/maps/mission2/map.yaml "
        "--strategy room_by_room --duration-min 7 "
        "--output runtime/maps/mission2/evidence.json",
        language="bash",
    )
    st.caption("Replace the strategy name and duration with what you actually used. The map analyzer records those labels; it does not measure your driving duration automatically.")
    local_evidence, local_yaml, local_image = runtime_map("mission2")
    evidence_item = artifact(st.file_uploader("Strategy 2 analysis JSON", type=["json"], key="m2.evidence")) or local_evidence
    yaml_item = artifact(st.file_uploader("Strategy 2 map YAML", type=["yaml", "yml"], key="m2.yaml")) or local_yaml
    image_item = artifact(st.file_uploader("Strategy 2 map PGM", type=["pgm"], key="m2.image")) or local_image
    screen_upload = st.file_uploader("Strategy 2 RViz screenshot", type=["png", "jpg", "jpeg"], key="m2.screen")
    saved_screens = sorted((submission_root() / "mission_2").glob("rviz_screenshot.*"))
    screenshot = (artifact(screen_upload, ROOT / "runtime/maps/mission2/rviz.png")
                  or (artifact(None, saved_screens[0]) if saved_screens else None))
    second = load_json(evidence_item)
    metrics, error = validate_map_bundle(second, yaml_item, image_item)
    if error: st.info(error)
    if first and second and metrics is not None:
        st.subheader("3. Inspect both maps")
        a, b = st.columns(2)
        with a:
            first_pgm = artifact(None, submission_root() / "mission_1" / "map.pgm")
            show_map(st, first_pgm, "First strategy")
        with b: show_map(st, image_item, "Second strategy")
        first_metrics, second_metrics = first.get("metrics", {}), second.get("metrics", {})
        rows = []
        for key, label in (
            ("known_fraction", "Known fraction"), ("speckle_fraction", "Speckle fraction"),
            ("border_contact_fraction", "Border contact fraction"),
            ("occupied_components", "Occupied components"),
        ):
            left, right = first_metrics.get(key), second_metrics.get(key)
            rows.append({"Measure": label, "Run 1": left, "Run 2": right,
                         "Run 2 − Run 1": round(right - left, 4) if isinstance(left, (int, float)) and isinstance(right, (int, float)) else "n/a"})
        rows.append({"Measure": "Quality score (discussion aid)", "Run 1": first.get("quality_score"),
                     "Run 2": second.get("quality_score"), "Run 2 − Run 1": "compare with image"})
        st.dataframe(rows, hide_index=True, width="stretch")
        st.caption("A higher score is not proof of a more correct map. Inspect wall alignment, duplicates, and areas never observed.")

    st.subheader("4. Explain differences and limits")
    text_response(st, "mission_2.comparison", "Compare both maps using at least three numeric measures and visible features. Was your original prediction supported?")
    text_response(st, "mission_2.loop_closure", "Describe evidence of a revisit or loop closure—or explain why the evidence is insufficient. What would distinguish correction of old structure from ordinary map growth?")
    check = evaluate(first, second if metrics is not None else None, st.session_state["responses"])
    render_check(st, check)
    if st.button("Check and save Mission 2", type="primary", disabled=not check.passed or screenshot is None):
        prior = st.session_state["evidence"].get("mission_2")
        st.session_state["evidence"]["mission_2"] = second
        signature = current_signature(st, "mission_2")
        try:
            save_mission(
                "mission_2", {"strategy_1": first, "strategy_2": second, "state_signature": signature},
                st.session_state["responses"],
                {"analysis.json": evidence_item, "map.yaml": yaml_item, "map.pgm": image_item,
                 "rviz_screenshot" + Path(screenshot.name).suffix.lower(): screenshot},
                state_signature=signature,
            )
        except (OSError, ValueError) as failure:
            if prior is None: st.session_state["evidence"].pop("mission_2", None)
            else: st.session_state["evidence"]["mission_2"] = prior
            st.error(f"Mission files were not saved: {failure}")
        else:
            complete_mission(st, "mission_2", signature)
            st.success("Both strategy records are saved for comparison.")
    if mission_status(st)["mission_2"] and st.button("Continue to localization tutorial"):
        set_stage(st, "tutorial_4")
