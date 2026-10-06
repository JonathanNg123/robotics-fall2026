import tempfile, unittest
from pathlib import Path
from analysis.localization import localization_decision, summarize, trial_passes
from analysis.map_metrics import analyze_pixels, quality_score, read_pgm, read_pgm_bytes
from scripts.analyze_map import parse_map_metadata

class AnalysisTests(unittest.TestCase):
    def test_ascii_pgm_and_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.pgm"; path.write_bytes(b"P2\n# test\n4 2\n255\n0 0 254 205 254 254 205 0\n")
            width, height, maximum, pixels = read_pgm(path); metrics = analyze_pixels(width, height, maximum, pixels, .05)
            self.assertEqual((width, height, maximum), (4, 2, 255)); self.assertAlmostEqual(metrics["known_fraction"], .75); self.assertGreaterEqual(quality_score(metrics), 0)
    def test_localization_summary(self):
        rows = [{"time": i, "x": 1 + .001 * i, "y": 2, "yaw": 0, "covariance_trace": .8 if i < 2 else .2} for i in range(21)]
        metrics = summarize(rows); self.assertEqual(metrics["sample_count"], 21); self.assertEqual(metrics["convergence_time"], 2)
        self.assertTrue(trial_passes("good_initial_pose", metrics))
    def test_map_yaml_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.yaml"; path.write_text("image: map.pgm\nresolution: 0.05\norigin: [0, 0, 0]\n", encoding="utf-8")
            self.assertEqual(parse_map_metadata(path)["image"], "map.pgm")
    def test_empty_summary(self): self.assertEqual(summarize([])["sample_count"], 0)

    def test_binary_pgm_preserves_whitespace_valued_first_pixel(self):
        width, height, maximum, pixels = read_pgm_bytes(b"P5\n2 1\n255\n\x0a\xfe")
        self.assertEqual((width, height, maximum, pixels), (2, 1, 255, [10, 254]))

    def test_binary_pgm_crlf_header(self):
        self.assertEqual(read_pgm_bytes(b"P5\r\n2 1\r\n255\r\n\x0a\xfe"), (2, 1, 255, [10, 254]))

    def test_reference_error_is_distinct_from_covariance(self):
        rows = [{"time": i, "x": 1.0, "y": 0., "yaw": 0., "covariance_trace": .1,
                 "reference_x": 0., "reference_y": 0., "reference_yaw": 0.} for i in range(25)]
        metrics = summarize(rows)
        self.assertEqual(metrics["final_position_error"], 1.)
        self.assertEqual(metrics["false_confident_samples"], 25)
        self.assertIsNone(metrics["correct_convergence_time"])
        self.assertIn("SLOW", localization_decision({**metrics, "scan_retention": 1.}, .5, 10.))

    def test_confidently_wrong_trial_is_still_valid_evidence(self):
        metrics = {"sample_count": 40, "duration": 20, "final_covariance": .1,
                   "settled_position_spread": .02, "pose_jump": .01, "scan_retention": 1.0}
        self.assertTrue(trial_passes("incorrect_initial_pose", metrics))

if __name__ == "__main__": unittest.main()
