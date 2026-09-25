# Mission 3

## Ai Disclosure

I used ChatGPT to help interpret the assignment requirements, calculate the motion segments, write the initial Python implementation, and develop tests. I reviewed the code against the required rounded-rectangle specification. I revised the implementation in pattern.py, created two student tests, and ran the course evaluator. I verified that all 9 automated tests passed.

## Assigned Pattern

rounded_rectangle

## Assumptions

The AI assumed that the robot used meters for distance travled, meters per second for velocity, and radians per second for angular velocity. It also assumed that positive linear velocity moves the robot forward in the robot body frame and positive angular velocity turns the robot left. It also assumed the course-provided wrapper will stop the robot after the pattern finishes.

## Evidence Analysis

The evaluation ran 9 tests and all 9 passed. These tests show that the program has the structure, segment types and durations. It produces the intended rounded-rectangle geometry in the mathematical model. However, passing these tests does not prove that the real ROS simulation will follow the exact same path because actual robot motion can differ from the ideal calculations. My live ROS run completed, but the final stop and the observed rounded-rectangle shape were not successfully verified. 

## Live Issue

I ran the assigned rounded rectangle pattern using the ROS course runner. The program completed without being interrupted, but the live evaluator reported that the final stop was not verified and the observed path did not match the expected shape closely enough. 

## Live Pending

True

## Modifications

I looked at the AI implementation and kept the existing Segment class and revised only build_pattern(). I used straight segments with 0 angular velocity and calculated their durations using distance divided by linear speed. I also made sure all speeds and durations stay within the course limits and that an unknown pattern name raises ValueError.

## Original Output

For the rounded rectangle, I would use a constant forward speed of 0.20 m/s for the straight segments. That gives durations of 2.0 s for each 0.40 m leg and 1.25 s for each 0.25 m leg.
For each rounded corner, the robot needs to travel through a 90° (π/2 rad) left arc with radius 0.15 m. Using a linear speed of 0.12 m/s gives an angular speed of 0.12 / 0.15 = 0.80 rad/s. The duration of each 90° arc is (π/2) / 0.80 ≈ 1.9635 s. These values stay within the limits of 0.22 m/s linear speed and 0.80 rad/s angular speed.
I assume Segment can be constructed using linear_x, angular_z, and duration. I also assume the course-provided wrapper is responsible for publishing the segments and sending the final zero-velocity command, so build_pattern should only construct and return the eight motion segments. This requires import math if pattern.py does not already import it.
I would test that build_pattern("rounded_rectangle") returns exactly eight segments in the correct straight/arc order. For the straight segments, I would verify that linear_x * duration produces 0.40, 0.25, 0.40, and 0.25 m. For each arc, I would verify that angular_z * duration is π/2 radians and that linear_x / angular_z is 0.15 m. I would also test that all speed and duration limits are satisfied and that an unknown pattern name raises ValueError.

## Original Prompt

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for rounded_rectangle in the existing pattern.py. The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command. Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s). Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name. Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total. Do not replace the wrapper or course checks. Explain assumptions and propose tests.

## Original Source

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

## Problems

I identified whether the generated specs matched the assignment requirements. The straight speed of 0.20 m/s is below the 0.22 m/s limit. The arc uses 0.12 m/s and 0.80 rad/s, which gives the required 0.15 m radius. I also checked that each arc turns left by 90 degrees and that the straight distances occur in the required order.

## Saved Specification

I want the robot to follow a rounded rectangle using eight motion segments. The rounded rectangle will alternate between four straight forward sections of 0.40 m, 0.25 m, 0.40 m, and 0.25 m, with a 90-degree left arc with a radius of 0.15 m after each straight section. The speeds will stay within 0.22 m/s for linear velocity and 0.80 rad/s for angular velocity. 

## Specification

I want the robot to follow a rounded rectangle using eight motion segments. The rounded rectangle will alternate between four straight forward sections of 0.40 m, 0.25 m, 0.40 m, and 0.25 m, with a 90-degree left arc with a radius of 0.15 m after each straight section. The speeds will stay within 0.22 m/s for linear velocity and 0.80 rad/s for angular velocity. 

## Test Plan

For a pattern behavior test, we would check that the function returns eight segments alternating between a straight movement and a left 90-degree curve. The expected result is a rounded rectangle that finishes near its starting pose. For the velocity-limit test, I would make sure that every linear speed is at most 0.22 m/s and every angular speed is at most 0.80 rad/s. For the stop test, I would verify that the course-provided wrapper sends a 0 velocity after the final segment. 
