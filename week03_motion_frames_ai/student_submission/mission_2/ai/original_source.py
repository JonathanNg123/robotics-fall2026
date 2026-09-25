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