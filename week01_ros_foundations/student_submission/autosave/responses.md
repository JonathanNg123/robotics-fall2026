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



## mission_2.motion_comparison



## mission_2.prediction_locks

{'straight': '2026-09-11T07:44:08.972337+00:00'}

## mission_2.predictions

{'straight': 'I predict the robot will move forward only with no turning and will move 0.45 meters.'}

## mission_2.safety_explanation



## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
