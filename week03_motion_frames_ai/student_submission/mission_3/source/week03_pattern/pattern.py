"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")
    straight_speed = 0.2
    arc_linear_speed = 0.12
    arc_angular_speed = 0.80

    arc_duration = round((math.pi / 2) / arc_angular_speed, 6)
    distances = [0.40, 0.25, 0.40, 0.25]
    segments = []

    for distance in distances:
        straight_duration = distance / straight_speed

        segments.append(
            Segment(
                linear_x=straight_speed,
                angular_z=0.0,
                duration=straight_duration,
            )
        )

        segments.append(
            Segment(
                linear_x=arc_linear_speed,
                angular_z=arc_angular_speed,
                duration=arc_duration,
            )
        )

    return segments

