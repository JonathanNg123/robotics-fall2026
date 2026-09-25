"""Mission 2 student implementation.

Complete only ``transform_camera_point`` after preserving the initial AI output
in the guide. Course tests supply both real and simulated TF buffers.
"""
from geometry_msgs.msg import PointStamped

def transform_camera_point(tf_buffer, point: PointStamped) -> PointStamped | None:
    if point.header.frame_id != "hall_camera":
        raise ValueError("Point must be in the hall_camera frame")

    try:
        return tf_buffer.transform(point, "base_link")

    except Exception:
        return None
