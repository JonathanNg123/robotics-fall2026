import os
import unittest

from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        self.assertEqual(len(segments), 8)

        expected_distances = [0.40, 0.25, 0.40, 0.25]

        for index, expected_distance in zip([0, 2, 4, 6], expected_distances):
            segment = segments[index]
            self.assertAlmostEqual(
                segment.linear_x * segment.duration,
                expected_distance,
                places=5,
            )
            self.assertAlmostEqual(segment.angular_z, 0.0, places=5)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        for index in [0, 2, 4, 6]:
            self.assertGreater(segments[index].linear_x, 0.0)
            self.assertAlmostEqual(segments[index].angular_z, 0.0, places=5)

        for index in [1, 3, 5, 7]:
            self.assertGreater(segments[index].linear_x, 0.0)
            self.assertGreater(segments[index].angular_z, 0.0)


if __name__ == "__main__":
    unittest.main()