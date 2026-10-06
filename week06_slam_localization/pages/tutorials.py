"""Five short, revisitable concept-to-evidence tutorials."""
from lab.navigation import set_stage
from lab.session import response, set_response
from lab.ui import text_response

NEXT = {
    "tutorial_1": "tutorial_2", "tutorial_2": "preflight",
    "tutorial_3": "mission_1", "tutorial_4": "tutorial_5",
    "tutorial_5": "mission_3",
}


def _finish(st, stage, ready):
    if st.button("Mark tutorial reviewed and continue", type="primary", disabled=not ready, key="done." + stage):
        progress = dict(st.session_state["tutorial_complete"])
        progress[stage] = True
        st.session_state["tutorial_complete"] = progress
        set_stage(st, NEXT[stage])
    if st.session_state["tutorial_complete"].get(stage):
        st.caption("Reviewed. You can return from Lab navigation at any time.")


def motion(st):
    st.header("Guided Tutorial 1 — Motion estimates and dead reckoning")
    st.write("Recall Lab 4: wheel encoders count rotation. They do not directly measure how far the robot actually moved across the floor.")
    st.table([
        {"Wheel speeds": "vL = vR", "Predicted motion": "straight"},
        {"Wheel speeds": "vL ≠ vR", "Predicted motion": "curve"},
        {"Wheel speeds": "vL = −vR", "Predicted motion": "rotate"},
    ])
    st.latex(r"v_L=v_R\Rightarrow\text{straight},\quad v_L\ne v_R\Rightarrow\text{curve},\quad v_L=-v_R\Rightarrow\text{rotate}")
    st.info("Dead reckoning estimates a new pose from a previous pose and estimated motion. It is frequent, inexpensive, and available between sensor observations.")
    st.write("Wheel slip, calibration error, and uneven surfaces make the estimate imperfect. Because each new pose builds on the previous one, systematic error can accumulate.")
    steps = st.slider("Repeated moves with 2 cm distance bias each", 1, 20, 10)
    st.metric("Possible accumulated distance error", f"{steps * .02:.2f} m")
    st.caption("At ten moves, 10 × 0.02 m = 0.20 m. A small heading error can produce a much larger path error as the robot keeps moving.")
    st.code("pose error → LiDAR observation placed at a wrong pose → distorted map")
    answer = text_response(st, "tutorial_1.check", "Why can a scan be accurate while the map built from it is distorted? Use dead reckoning in your answer.")
    _finish(st, "tutorial_1", len(answer.strip()) >= 30)


def maps(st):
    st.header("Guided Tutorial 2 — Map representations")
    a, b = st.columns(2)
    with a:
        st.subheader("Topological map")
        st.write("Places and connections: Room A ↔ Hallway ↔ Room B. It need not encode exact wall geometry or distance.")
    with b:
        st.subheader("Metric map")
        st.write("Coordinates, geometry, and distance. Lab 6 saves a metric occupancy-grid map.")
    st.subheader("What does a LiDAR ray contribute?")
    st.table([
        {"Along the ray": "Free evidence", "Meaning": "The beam passed through these cells."},
        {"At the return": "Occupied evidence", "Meaning": "The beam encountered a surface."},
        {"Not observed": "Unknown", "Meaning": "There is not enough evidence to label the cell."},
    ])
    endpoint = st.slider("Move a toy LiDAR return along one row of cells", 2, 6, 4)
    st.code("Robot  " + "· " * (endpoint - 1) + "■ " + "? " * (6 - endpoint) +
            "\n       free along ray    occupied return    unknown beyond")
    st.caption("The toy row shows one beam only. Real occupancy grids combine many noisy observations from estimated robot poses.")
    st.info("The scan must be placed using an estimated robot pose. Wrong pose can put correct range readings into the wrong cells.")
    answer = text_response(st, "tutorial_2.check", "Why does accurate robot pose matter when adding a LiDAR scan to an occupancy grid?")
    _finish(st, "tutorial_2", len(answer.strip()) >= 30)


def rviz(st):
    st.header("Guided Tutorial 3 — Read SLAM in RViz")
    st.write("Before mapping, learn what each display is evidence of. Start the mapping launch in Mission 1 when prompted; use this checklist again once RViz is open.")
    st.table([
        {"Display": "LaserScan /scan", "Interpretation": "current LiDAR measurement"},
        {"Display": "Robot pose and TF", "Interpretation": "estimated relationships between frames"},
        {"Display": "Occupancy grid /map", "Interpretation": "accumulated map inference"},
        {"Display": "Unknown cells", "Interpretation": "areas not adequately observed"},
        {"Display": "Trajectory, if available", "Interpretation": "estimated path, not ground truth"},
    ])
    st.write("As the robot moves, compare scan returns with existing walls. On a revisit, look for a correction to earlier geometry—not merely newly filled cells.")
    answer = text_response(st, "tutorial_3.check", "Which RViz display is a direct sensor measurement, which is a current estimate, and which accumulates past evidence?")
    _finish(st, "tutorial_3", len(answer.strip()) >= 30)


def transition(st):
    st.header("Guided Tutorial 4 — From SLAM to localization")
    st.code("During SLAM: estimate pose + estimate map\nDuring AMCL: fixed saved map + estimate pose")
    st.write("The map is now treated as reference evidence rather than something the robot keeps building. A poor map can still mislead localization; fixed does not mean perfect.")
    st.write("Use one chosen Mission 1 or Mission 2 map in every localization trial. Record why you chose it, using visual structure and at least two measured properties.")
    widget = "field.tutorial_4.selected_map"
    if widget not in st.session_state:
        st.session_state[widget] = response(st, "tutorial_4.selected_map", "Choose…")
    selected = st.selectbox("Saved map for all AMCL trials", ("Choose…", "Mission 1", "Mission 2"), key=widget)
    set_response(st, "tutorial_4.selected_map", selected)
    answer = text_response(st, "tutorial_4.map_choice", "Which saved map will you use, and what evidence supports that choice?")
    _finish(st, "tutorial_4", selected != "Choose…" and len(answer.strip()) >= 40)


def amcl(st):
    st.header("Guided Tutorial 5 — Read AMCL")
    st.write("AMCL particles represent possible robot poses. Several clusters can express competing hypotheses; a concentrated cluster is not automatically in the right place.")
    st.table([
        {"RViz item": "Particle cloud", "Question": "One cluster or several? How spread out?"},
        {"RViz item": "Estimated pose", "Question": "Does the arrow agree with the simulated robot?"},
        {"RViz item": "Known map + LiDAR", "Question": "Do current scans align with mapped walls?"},
    ])
    support = st.slider("How strongly does the next scan support pose hypothesis A?", 0, 100, 50, 5)
    st.bar_chart({"Hypothesis A": [support], "Hypothesis B": [100 - support]})
    st.caption("Illustrative relative support only; AMCL uses many particles and sensor updates, not this two-choice calculation.")
    st.info("A decrease in covariance indicates a more concentrated modeled belief. To claim correct localization, compare the estimate with independent evidence such as simulation reference pose and scan alignment.")
    answer = text_response(st, "tutorial_5.check", "What evidence would distinguish a tight but wrong particle cluster from correct localization?")
    _finish(st, "tutorial_5", len(answer.strip()) >= 30)


RENDERERS = {
    "tutorial_1": motion, "tutorial_2": maps, "tutorial_3": rviz,
    "tutorial_4": transition, "tutorial_5": amcl,
}


def render(st):
    RENDERERS[st.session_state["stage"]](st)
