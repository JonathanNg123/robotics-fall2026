def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "rounded_rectangle":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    straight_speed = 0.20
    arc_speed = 0.12
    arc_radius = 0.15
    angular_speed = arc_speed / arc_radius
    arc_duration = (math.pi / 2.0) / angular_speed

    return [
        Segment(linear_x=straight_speed, angular_z=0.0, duration=0.40 / straight_speed),
        Segment(linear_x=arc_speed, angular_z=angular_speed, duration=arc_duration),
        Segment(linear_x=straight_speed, angular_z=0.0, duration=0.25 / straight_speed),
        Segment(linear_x=arc_speed, angular_z=angular_speed, duration=arc_duration),
        Segment(linear_x=straight_speed, angular_z=0.0, duration=0.40 / straight_speed),
        Segment(linear_x=arc_speed, angular_z=angular_speed, duration=arc_duration),
        Segment(linear_x=straight_speed, angular_z=0.0, duration=0.25 / straight_speed),
        Segment(linear_x=arc_speed, angular_z=angular_speed, duration=arc_duration),
    ]