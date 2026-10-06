from pathlib import Path
from lab.evidence import load_json
from lab.navigation import set_stage
def render(st):
    st.header("ROS 2 preflight")
    st.write("Use the shared course container configured in Week 1. The course launcher has already selected `ROS_DOMAIN_ID=26`, sourced ROS 2 Jazzy, and opened this lab directory.")
    st.code("bash scripts/course_preflight.sh", language="bash")
    runtime = Path(__file__).resolve().parents[1] / "runtime" / "evidence" / "preflight.json"
    evidence = st.session_state["evidence"].get("preflight")
    if runtime.exists():
        import json
        try: evidence = json.loads(runtime.read_text(encoding="utf-8"))
        except json.JSONDecodeError: pass
    upload = st.file_uploader("If Streamlit runs on another machine, upload preflight.json", type=["json"])
    if upload: evidence = load_json(upload)
    if evidence:
        st.session_state["evidence"] = {**st.session_state["evidence"], "preflight": evidence}
        st.caption("Preflight captured: " + str(evidence.get("captured_at", "time unavailable")) +
                   ". This checks the installed environment; confirm live /scan, /odom, TF, and /map after launching Mission 1.")
        st.dataframe(evidence.get("checks", []), hide_index=True, width="stretch")
        (st.success if evidence.get("ready") else st.error)("Environment ready" if evidence.get("ready") else "Resolve every failed check before continuing.")
    else: st.warning("No preflight evidence found yet.")
    if st.button("Continue to RViz tutorial", type="primary", disabled=not bool(evidence and evidence.get("ready"))): set_stage(st, "tutorial_3")
