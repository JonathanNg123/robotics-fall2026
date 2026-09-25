# Mission 2

## Frame Context

The rear-camera transform stays fixed because the rear camera is physically attached to the robot. This means the position and orientation of the robot is the same when the robot moves. The hallway camera does not move with the robot. This means that as the robot moves or turns, the base_link changes.

## Improved Changes

The improved prompt defines hall_camera as the required source frame and base_link as the target frame instead of leaving the ai guessing. It makes sure it is checking the PointStamped frame_id and raising a ValueError if the point is not from hall_camera. It also makes it so it is using the point’s original timestamp so the transform corresponds to when the observation was made. Finally, if the required transform is unavailable, the function should return None without commanding any robot motion.

## Initial Analysis

The initial AI response made several assumptions because the original prompt did not provide enough details. Firsty, it assumed that hall_camera was the source frame and base_link was the target frame. However, it did not verify the PointStamped frame_id. It also used the latest available transform instead of preserving the point’s timestamp. The ai assumed the transform would always be available and did not clearly define what the function should return if it was unavailable. The improved version should use the supplied TF buffer to perserve the point metadata and timestamp.

## Initial Output

A typical ROS 2 Python solution is to use tf2_ros to look up the transform from the hallway camera frame to base_link, then apply that transform to a PointStamped. This node assumes that the detected point is published as a geometry_msgs/msg/PointStamped on /hallway_camera/point and that its source coordinate frame is hall_camera. The TF buffer stores the available coordinate-frame relationships, while the TransformListener receives TF updates.
lookup_transform('base_link', 'hall_camera', ...) requests the transformation needed to express data from the hallway-camera frame in the robot's base_link frame. do_transform_point() then applies that transformation to the detected point.
This example also assumes that the necessary transform connecting hall_camera and base_link already exists in the robot's TF tree.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
from tf2_ros import Buffer, TransformListener
from tf2_geometry_msgs import do_transform_point


class HallwayCameraTransformer(Node):
    def __init__(self):
        super().__init__('hallway_camera_transformer')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

    def point_callback(self, point):
        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                'hall_camera',
                rclpy.time.Time()
            )

            transformed_point = do_transform_point(point, transform)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={transformed_point.point.x:.2f}, '
                f'y={transformed_point.point.y:.2f}, '
                f'z={transformed_point.point.z:.2f}'
            )

        except Exception as e:
            self.get_logger().warning(
                f'Could not transform point: {e}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = HallwayCameraTransformer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-25T02:17:01.025020+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'source': 'reference', 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}}}

## Synthesis

The initial AI response made assumptions because the original prompt did not clearly specify many things. The improved prompt made these requirements clear by requiring many things such as the point to come from hall_camera and using the TF buffer to transform it into base_link. Those are just a few examples. Using the wrong transform could make the robot think an object or person is in a different location than they actually are, which could cause unsafe movement around people. The test that checks the camera source and robot body target helps detect this problem. If transform data is unavailable, the robot should not guess the person's location or continue based on incorrect data; it should return None.

## Live Issue

I ran python3 scripts/evaluate_camera_transform.py --live after my implementation passed all five course tests. The live evaluation could not return a transformed point from hall_camera to base_link, so the live transform was not verified. The implementation itself passed all five provided tests. What is unverified is if the transformation works with the current live ROS TF tree in Gazebo.
