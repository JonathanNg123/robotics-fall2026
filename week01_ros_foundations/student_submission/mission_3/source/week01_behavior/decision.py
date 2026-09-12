"""Pure decision helpers for Mission 3.

Complete both functions. Keeping this logic independent of ROS makes it possible
to test safety decisions before running the simulated robot.
"""

from __future__ import annotations

from collections.abc import Sequence

import math

def front_distance(
    ranges: Sequence[float],
    angle_min: float,
    angle_increment: float,
    half_width_radians: float,
) -> float | None:
    """Return the nearest finite, positive reading in the front sector.

    Return ``None`` when the sector has no valid reading. Angles are measured in
    radians and the front direction is zero radians.
    """
    distances = []
    for index, distance in enumerate(ranges):
        angle = angle_min + index * angle_increment
        in_front = abs(angle) <= half_width_radians
        is_valid = math.isfinite(distance) and distance > 0 

        if in_front and is_valid:
            distances.append(distance)  # If both in front of the robot and there is a valid distance, add that distance to our list.

    if not distances: # If there is no valid distance in front of the robot, return None.
        return None

    return min(distances)


def decide_velocity(
    distance: float | None,
    stop_distance: float,
    forward_speed: float,
) -> float:
    """Return a bounded forward velocity; missing data must produce a stop."""
    if distance is None:
        return 0.0

    if distance <= stop_distance:
        return 0.0

    return max(0.0, min(float(forward_speed), 0.18))

