from pathlib import Path

from lab.autosave import submission_root
from lab.completion import current_signature, mission_status
from lab.controls import prediction
from lab.evidence import artifact, load_json, runtime_map, validate_map_bundle
from lab.navigation import set_stage
from lab.session import complete_mission
from lab.submissions import save_mission
from lab.ui import render_check, show_map, text_response
from missions.mission_1 import evaluate

ROOT = Path(__file__).resolve().parents[1]


def render(st):
    st.header("Mission 1 — Build and inspect a map")
    st.write("Plan, observe, save, and interpret your first occupancy-grid map. A wrong prediction is useful if you explain what the run revealed.")

    st.subheader("1. Plan before driving")
    forecast = prediction(
        st, "mission_1.route", {"world": "turtlebot3_world", "run": 1},
        "Describe your route, a place you will revisit, and where you predict map coverage or alignment may be weak.",
        min_chars=40,
    )
    if forecast is None:
        st.info("Save the plan before running the robot. Your original prediction is kept separately from later analysis.")
        return

    st.subheader("2. Launch and inspect")
    st.write("Use separate terminals in the browser desktop. Keep the mapping launch running while you teleoperate and inspect. Stop the robot before changing terminal focus.")
    with st.expander("Terminal 1 — simulator and SLAM", expanded=True):
        st.code("export ROS_DOMAIN_ID=26\nbash scripts/launch_mapping.sh", language="bash")
        st.caption("Expected: TurtleBot3 World starts and /scan, /odom, TF, and /map become available. If no map appears, check those topics and the SLAM lifecycle state.")
    with st.expander("Terminal 2 — teleoperation"):
        st.code("source /opt/ros/jazzy/setup.bash\nexport ROS_DOMAIN_ID=26\nexport TURTLEBOT3_MODEL=burger\nros2 run turtlebot3_teleop teleop_keyboard", language="bash")
    with st.expander("Terminal 3 — RViz observations"):
        st.code("rviz2", language="bash")
        st.write("Add Map, LaserScan, RobotModel, TF, and Odometry. Identify the current scan, estimated pose, known cells, and unknown cells. On a revisit, look for a correction to existing structure.")
    st.warning("Avoid rapid rotation and do not edit the saved PGM or evidence JSON by hand.")

    st.subheader("3. Save and analyze")
    st.write("After approximately 6–8 minutes, save the map while SLAM is running. The guide reads files in runtime/maps/mission1 automatically; use uploads if Streamlit is on another machine.")
    st.code(
        "mkdir -p runtime/maps/mission1\n"
        "ros2 run nav2_map_server map_saver_cli -f runtime/maps/mission1/map\n"
        "python3 scripts/analyze_map.py --yaml runtime/maps/mission1/map.yaml "
        "--strategy perimeter_then_interior --duration-min 7 "
        "--output runtime/maps/mission1/evidence.json",
        language="bash",
    )
    st.caption("Replace the example strategy label and seven-minute duration with the route and actual timing you used. The analyzer cannot measure driving duration for you.")
    local_evidence, local_yaml, local_image = runtime_map("mission1")
    evidence_item = artifact(st.file_uploader("Map analysis JSON", type=["json"], key="m1.evidence")) or local_evidence
    yaml_item = artifact(st.file_uploader("Map YAML", type=["yaml", "yml"], key="m1.yaml")) or local_yaml
    image_item = artifact(st.file_uploader("Map PGM", type=["pgm"], key="m1.image")) or local_image
    screen_upload = st.file_uploader("RViz screenshot with map, scan, and robot", type=["png", "jpg", "jpeg"], key="m1.screen")
    saved_screens = sorted((submission_root() / "mission_1").glob("rviz_screenshot.*"))
    screenshot = (artifact(screen_upload, ROOT / "runtime/maps/mission1/rviz.png")
                  or (artifact(None, saved_screens[0]) if saved_screens else None))
    evidence = load_json(evidence_item)
    metrics, error = validate_map_bundle(evidence, yaml_item, image_item)
    if error:
        st.info(error)
    else:
        st.success("The map YAML, PGM, and analysis JSON agree.")
        st.dataframe([{"measure": key, "value": value} for key, value in metrics.items()], hide_index=True)
        show_map(st, image_item, "First mapping run")
        with st.expander("How to interpret these map measures"):
            st.write("Known fraction is the share labeled free or occupied; it is not proof that labels are correct. Speckle fraction counts small isolated occupied components. Border contact can suggest a clipped map. The quality score combines these measures for discussion, not as ground truth.")
    if screenshot is None:
        st.info("Save an RViz screenshot as runtime/maps/mission1/rviz.png or upload it here.")

    st.subheader("4. Explain what the evidence supports")
    text_response(st, "mission_1.system_observation", "Describe how /scan, odometry, TF, and /map changed. Identify which is a measurement, which is an estimate, and which is accumulated map evidence.")
    text_response(st, "mission_1.map_interpretation", "Use your known fraction, speckle fraction, border contact, and visible walls to identify a strength and a possible defect.")
    text_response(st, "mission_1.limitations", "Where did the robot collect little evidence? How did your route or sensor geometry cause that limitation?")
    text_response(st, "mission_1.drift_and_revisit", "Identify a revisit or potential loop closure. Could accumulated pose error explain any distortion? Explain what you observed and what you cannot conclude.")
    check = evaluate(evidence if metrics is not None else None, st.session_state["responses"], metrics is not None, metrics is not None)
    render_check(st, check)
    if st.button("Check and save Mission 1", type="primary", disabled=not check.passed or screenshot is None):
        prior = st.session_state["evidence"].get("mission_1")
        st.session_state["evidence"]["mission_1"] = evidence
        signature = current_signature(st, "mission_1")
        try:
            save_mission(
                "mission_1", {"analysis": evidence, "state_signature": signature},
                st.session_state["responses"],
                {
                    "analysis.json": evidence_item, "map.yaml": yaml_item, "map.pgm": image_item,
                    "rviz_screenshot" + Path(screenshot.name).suffix.lower(): screenshot,
                },
                state_signature=signature,
            )
        except (OSError, ValueError) as failure:
            if prior is None: st.session_state["evidence"].pop("mission_1", None)
            else: st.session_state["evidence"]["mission_1"] = prior
            st.error(f"Mission files were not saved: {failure}")
        else:
            complete_mission(st, "mission_1", signature)
            st.success("Mission 1 evidence and explanations saved.")
    if mission_status(st)["mission_1"] and st.button("Continue to Mission 2"):
        set_stage(st, "mission_2")
