import unittest
from missions import mission_1, mission_2, mission_3

class MissionTests(unittest.TestCase):
    def setUp(self):
        self.metrics = {"known_fraction": .55, "resolution": .05, "speckle_fraction": .02, "border_contact_fraction": .01}
    def test_map_missions(self):
        first = {"strategy": "perimeter", "duration_minutes": 7, "metrics": self.metrics, "quality_score": 70}
        second = {"strategy": "frontier", "duration_minutes": 7.5, "metrics": {**self.metrics, "known_fraction": .6}, "quality_score": 75}
        responses = {**{f"mission_1.{key}": "Evidence-based interpretation of ROS observations, map quality, limitations, and causes. " * 2 for key in mission_1.REFLECTIONS}, **{f"mission_2.{key}": "Controlled numerical and visual comparison with a careful claim about loop closure evidence. " * 2 for key in mission_2.REFLECTIONS}}
        responses["mission_1.route.original_prediction"] = "I will follow the perimeter, revisit a wall, and inspect the weakly observed center."
        responses["mission_2.strategy.original_prediction"] = "The second route may improve coverage but delay revisits."
        responses["mission_2.controls"] = "Both runs start from the same robot pose, use the same world and map resolution, and run for about seven minutes. Route choice is the principal change; steering differences remain a possible confound."
        self.assertTrue(mission_1.evaluate(first, responses, True, True).passed); self.assertTrue(mission_2.evaluate(first, second, responses).passed)
    def test_localization_mission(self):
        base = {"sample_count": 40, "duration": 20, "convergence_time": 2, "final_covariance": .1, "settled_position_spread": .03, "pose_jump": .02, "scan_retention": 1.0}
        trials = {"good_initial_pose": {"metrics": base}, "incorrect_initial_pose": {"metrics": {**base, "pose_jump": .5}}, "ambiguous_location": {"metrics": {**base, "final_covariance": .2}}, "degraded_sensor": {"metrics": {**base, "final_covariance": .3, "scan_retention": .5}}}
        responses = {f"mission_3.{key}": "Evidence-based interpretation of uncertainty, recovery, sensing, failure, stakeholders, and fallback behavior. " * 2 for key in mission_3.REFLECTIONS}
        for condition in mission_3.CONDITIONS:
            responses[f"mission_3.{condition}.original_prediction"] = "I expect this initial pose to change the particle distribution and convergence."
            responses[f"mission_3.{condition}.observation"] = "The particle cloud changed during the run; I compared the estimated pose with independent visual evidence before judging correctness."
            responses[f"mission_3.{condition}.correctness"] = "Uncertain"
        responses["mission_3.policy_reasoning"] = "A low covariance is only a concentrated belief. I would slow, stop, or ask for help when scan evidence or convergence is weak, and also check for a confidently wrong pose near people."
        self.assertTrue(mission_3.evaluate(trials, responses).passed); self.assertFalse(mission_3.evaluate({}, {}).passed)

if __name__ == "__main__": unittest.main()
