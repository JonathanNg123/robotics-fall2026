# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Jonathan Ng
- Email: Jonathan.ng03@login.cuny.edu

## mission_1.command_path_explanation

A proposed command travels on /student_cmd_vel. The guard takes the proposed command and checks it before sending it to the robot. Then after being approved, it is published to /cmd_vel and sent to the robot.

## mission_1.graph_explanation

A ROS 2 graph shows the running ROS programs which are the nodes and how they can communicate using the topics. An example can be /ros.gz.bridge which shows the LiDAR information through the /scan topic which allows another node to subscribe to it.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found many different numbers as well as .inf under ranges which represents the distance in meters taken by the LiDAR of an object in a particular direction to the robot. I believe .inf means there is no object in the way of the robot for that specific direction.

## mission_1.tools_explanation

Gazebo is responsibile for the simulation, environment, and physics involved with the robot while RViz is responsibile for showing the ROS 2 data. 

## mission_2.measurement_explanation

For the curved trial, estimated traveled path was 0.374 m because it most likely measured the distance the robot travled on a curve path. This is longer than the start-to-end path being 0.359 because that path measured the straight line between where the robot started and where it ended up.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

For the cuved trial, the live simulation results matched fairly similar to my prediction. This is because it moved forward while turning right which is what I predicted. The robot moved forward 0.374m while turning right -58.9 degrees which is not one to one with my prediction, but very similar.

## mission_2.prediction_locks

{'curve': '2026-09-11T15:53:35.191351+00:00', 'curve_modified': '2026-09-11T15:57:07.616983+00:00', 'rotation': '2026-09-11T15:46:25.125193+00:00', 'straight': '2026-09-11T07:44:08.972337+00:00'}

## mission_2.predictions

{'curve': 'I predict a turn to the right while moving forward for 4 seconds because the forward speed is postive and turning speed is negative.', 'curve_modified': 'This curve should be tighter and turn the other way (left) because the forward speed is slightly slower while the turning speed is larger and also positive.', 'rotation': 'I predict its position will stay the same while its direction will turn left for abount 3 seconds.', 'straight': 'I predict the robot will move forward only with no turning and will move 0.45 meters.'}

## mission_2.safety_explanation

The command guard checks every driving command before sending it to the robot while also preventing too high of speeds and values that are invalid. The final zero command tells the robot to stop by changing its forward and turning speed to zero. The timeout is needed if a program crashes or communication stops when the robot is in motion

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
