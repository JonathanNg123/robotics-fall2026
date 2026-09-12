# Mission 3

## Data To Command

The front_distance() function looks at the list of distance readings and checks if each distance is valid and in front of the robot. After validating the distances, it then finds the closest valid distance. The decide_velocity() function uses the closest distance to decide whether the robot should move or stop. If an obstacle is in the way, the robot stops.

## Missing Data Safety

The robot stops when there is no valid front measurement because it still does not know if the path ahead is clear. If the data is invalid, letting the robot move can cause it to run into an obstacle that it was not able to detect. Stopping is the safer option.

## System Layers

My decision functions determine whether the robot should move or stop. The supplied ROS node takes the readings from /scan and uses the decision funtions to make a decision. It then puts the chosen velocity to /student_cmd_vel. The command guard basically adds more safety by regulating how the command is passed. These work together by making the robot adjust to obstacles while making sure its safe.
