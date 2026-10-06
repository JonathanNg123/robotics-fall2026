import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


@unittest.skipUnless(importlib.util.find_spec("streamlit"), "Streamlit is not installed")
class StudentGuideUI(unittest.TestCase):
    def test_pgm_preview_renders(self):
        from streamlit.testing.v1 import AppTest

        app = AppTest.from_string(
            "import streamlit as st\n"
            "from lab.ui import show_map\n"
            "class Image:\n"
            "    def getvalue(self): return b'P5\\n2 1\\n255\\n\\x0a\\xfe'\n"
            "show_map(st, Image(), 'Test map')\n"
        ).run()
        self.assertFalse(app.exception, str(app.exception))

    def test_intro_tutorial_navigation_and_restart(self):
        from streamlit.testing.v1 import AppTest

        source = Path(__file__).resolve().parents[1] / "app.py"
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {"WEEK06_SUBMISSION_DIR": directory}), patch.object(sys, "argv", [str(source)]):
            app = AppTest.from_file(str(source), default_timeout=30).run()
            self.assertFalse(app.exception)
            for key, value in (
                ("student.name", "Test Student"),
                ("student.email", "student@example.edu"),
                ("student.course_id", "12345"),
            ):
                app.text_input(key=key).set_value(value).run()
            next(button for button in app.button if button.label == "Begin").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["stage"], "tutorial_1")
            app.text_area(key="field.tutorial_1.check").set_value(
                "A good range scan can be misplaced when dead-reckoned robot pose is wrong."
            ).run()
            next(button for button in app.button if button.label == "Mark tutorial reviewed and continue").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["stage"], "tutorial_2")
            app.text_area(key="field.tutorial_2.check").set_value(
                "The robot pose determines which metric grid cells receive each LiDAR ray."
            ).run()
            next(button for button in app.button if button.label == "Mark tutorial reviewed and continue").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["stage"], "preflight")
            restarted = AppTest.from_file(str(source), default_timeout=30).run()
            self.assertFalse(restarted.exception)
            self.assertEqual(restarted.session_state["stage"], "preflight")
            self.assertEqual(restarted.session_state["student"]["name"], "Test Student")
            self.assertTrue(restarted.session_state["tutorial_complete"]["tutorial_2"])

    def test_previous_final_page_remains_revisitable_when_evidence_stales(self):
        from streamlit.testing.v1 import AppTest
        from lab.autosave import save
        from lab.session import initialize

        source = Path(__file__).resolve().parents[1] / "app.py"
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ, {"WEEK06_SUBMISSION_DIR": directory}
        ), patch.object(sys, "argv", [str(source)]):
            st = SimpleNamespace(session_state={})
            initialize(st)
            st.session_state["stage"] = "mission_1"
            st.session_state["visited_stages"] = ["intro", "mission_1", "final"]
            save(st)
            app = AppTest.from_file(str(source), default_timeout=30).run()
            self.assertFalse(app.exception)
            self.assertFalse(app.button(key="nav.final").disabled)
            app.button(key="nav.final").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state["stage"], "final")

    def test_each_mission_and_final_page_render_without_ros(self):
        from streamlit.testing.v1 import AppTest
        from lab.autosave import save
        from lab.evidence import evidence_id
        from lab.session import initialize

        source = Path(__file__).resolve().parents[1] / "app.py"
        first = {"strategy": "perimeter_then_interior", "duration_minutes": 7,
                 "metrics": {"known_fraction": .5, "resolution": .05}, "quality_score": 65}
        second = {"strategy": "room_by_room", "duration_minutes": 7,
                  "metrics": {"known_fraction": .6, "resolution": .05}, "quality_score": 70}
        for stage in ("mission_1", "mission_2", "mission_3", "final"):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as directory, patch.dict(
                os.environ, {"WEEK06_SUBMISSION_DIR": directory}
            ), patch.object(sys, "argv", [str(source)]):
                st = SimpleNamespace(session_state={})
                initialize(st)
                st.session_state["stage"] = stage
                st.session_state["student"] = {"name": "Test", "email": "test@example.edu", "course_id": "123"}
                st.session_state["evidence"].update(preflight={"ready": True}, mission_1=first, mission_2=second)
                st.session_state["tutorial_complete"] = {
                    "tutorial_1": True, "tutorial_2": True, "tutorial_3": True,
                    "tutorial_4": True, "tutorial_5": True,
                }
                st.session_state["responses"].update({
                    "tutorial_4.selected_map": "Mission 1",
                    "tutorial_4.map_choice": "Mission 1 has stronger wall alignment and adequate coverage.",
                })
                for activity, context in (
                    ("mission_1.route", {"world": "turtlebot3_world", "run": 1}),
                    ("mission_2.strategy", {"first_evidence_id": evidence_id(first), "world": "turtlebot3_world"}),
                ):
                    st.session_state["prediction_locks"][activity] = {
                        "context_signature": evidence_id(context), "text": "A saved prediction before the trial."
                    }
                selected_map_id = evidence_id("Mission 1", first, st.session_state["responses"]["tutorial_4.map_choice"])
                for condition in ("good_initial_pose", "incorrect_initial_pose", "ambiguous_location", "degraded_sensor"):
                    st.session_state["prediction_locks"]["mission_3." + condition] = {
                        "context_signature": evidence_id({"condition": condition, "selected_map": selected_map_id}),
                        "text": "The particles may spread or converge after scans.",
                    }
                save(st)
                app = AppTest.from_file(str(source), default_timeout=30).run()
                self.assertFalse(app.exception, str(app.exception))


if __name__ == "__main__":
    unittest.main()
