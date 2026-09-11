# Mission 1

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard takes the proposed command and checks it before sending it to the robot. Then after being approved, it is published to /cmd_vel and sent to the robot.

## Graph Explanation

A ROS 2 graph shows the running ROS programs which are the nodes and how they can communicate using the topics. An example can be /ros.gz.bridge which shows the LiDAR information through the /scan topic which allows another node to subscribe to it.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found many different numbers as well as .inf under ranges which represents the distance in meters taken by the LiDAR of an object in a particular direction to the robot. I believe .inf means there is no object in the way of the robot for that specific direction.

## Tools Explanation

Gazebo is responsibile for the simulation, environment, and physics involved with the robot while RViz is responsibile for showing the ROS 2 data. 
