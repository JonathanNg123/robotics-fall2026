# Week 6: SLAM and Mapping

- email: Jonathan.ng03@login.cuny.edu
- name: Jonathan Ng

## final.course_reflection

This lab helped me better understand how robots navigate and learn about their surroundings as I was able to get first hand experience controlling a robot and mapping out areas. It was fun challenging myself with 10 mintues to compare 2 different strategies. Before doing this activity, I did not fully understand how a robot could create a map without already knowing the environment. It was interesting to watch the map develop in RViz as I controlled the robot in Gazebo.

## final.synthesis

This lab uses motion estimates and LiDAR measurements to create a map of its surroundings. The motion estimates were used to help the robot track where it thinks it is moving. The LiDAR measures distances to nearby walls and obstacles. Both these are used by SLAM to build a grid map that shows the free space, occupied space, and unknown areas. The issue is that the robot will not be able to know exactly what the entire house looks like because it can only map areas that its sensors have observed. For Mission 1, I used a slow, but methodical exploration strategy for 10 minutes. This created a map with 17.81 square meters of known area, 23.91% known coverage, and a quality score of 45.8. For Mission 2, I used a fast room-by-room strategy for another 10 minutes. This produced 30.76 square meters of known area, 19.75% known coverage, and a quality score of 42.4. One limitation of SLAM is that the motion estimates can have errors as the robot moves. Revisiting areas can correct things as it helps SLAM recognize previous locations and correct some of these errors like an obstacle it had not seen. I would trust Mission 1 more for a task requiring exploration because it mapped a higher quality area which gives other robots confidence in where it is going in that space.

## mission_1.drift_and_revisit

After returning to an area that was already scanned, the RViz map clearly mapped the walls and the robot's position/direction, but I could not clearly see whether any walls shifted or doubled. Therefore, I am not sure if SLAM corrected any accumulated drift. The evidence missing would just be more data from clearer screenshots of the same area before and after so I could compare the wall positions.

## mission_1.limitations

An area that remained unknown was a large gray area on the left side of my RViz map. This is most likely due to the fact that I only  drove the robot around some of the hallways and walls and not others. This idea is also backed by the fact my map analysis showed that approximately 76.09% of the map remained unknown. Another reason could be that since the LiDAR sensor could only detect areas within its line of sight, walls and obstacles most likely blocked the robot from scanning certain spaces.

## mission_1.route.original_prediction

My route is to start near the left of the area and slowly move through the hallways while using the LiDAR sensor to map the walls and other objects near me. I will explore the center first as that is where I started and  then move to the upper right sections of the house going though the gaps that allow me to move. After exploring the whole house, I plan to return to the center where I started to see whether the map that was created looks like what was previously observed. I predict that the map that was created will be inaccurate for the areas with narrow passages and corners because the LiDAR sensor might not be able to scan those tight areas.

## mission_1.route.prediction_draft

My route is to start near the left of the area and slowly move through the hallways while using the LiDAR sensor to map the walls and other objects near me. I will explore the center first as that is where I started and  then move to the upper right sections of the house going though the gaps that allow me to move. After exploring the whole house, I plan to return to the center where I started to see whether the map that was created looks like what was previously observed. I predict that the map that was created will be inaccurate for the areas with narrow passages and corners because the LiDAR sensor might not be able to scan those tight areas. 

## mission_2.comparison

I chose to do 10 minutes for both strategies for a easier comparison. Mission 1 used a slower, but more methodical approach making sure the robot was able to get all the details. Mission 2 used a fast room-by-room strategy where the robot tried to cover as much ground as it could without paying attention to much detail. Mission 1 naturally had a higher quality score of 45.8 compared to Mission 2's 42.4. However, Mission 2 mapped a larger known area of 30.76 m² compared to Mission 1's 17.81 m². Mission 2 also mapped 3.08 m² per minute compared to Mission 1's 1.78 m² per minute. This is to be expected as mission 2's strategy of fast room-by-room strategy covered more physical space in the same amount of time, but less quality map compared to mission 1's strategy.

## mission_2.map_choice

I would personally trust the Mission 1 map more for a later robot task as a higher quaity map will most likely ensure safe and efficent task managment. Looking at the images, Mission 1 shows more detailed images making it so other robots can know exaclty where things are in the house. One limitation is that these images and measurements cannot prove that every wall is positioned correctly or that the robot could safely navigate through the mapped environment.

## mission_2.strategy.original_prediction

For this new route, I plan to explore more of the rooms and hallways that II did not do during Mission 1. Instead of spendind so much time exploring one area,I will try to move through different spaces and scan different angles much faster. I think that this new route will make a  much clearer and complete map because the LiDAR sensor will have more ares to scan that were blocked. However, even though I want this route to be faster, exploring additional areas missed in route 1 might take longer.

## mission_2.strategy.prediction_draft

For this new route, I plan to explore more of the rooms and hallways that II did not do during Mission 1. Instead of spendind so much time exploring one area,I will try to move through different spaces and scan different angles much faster. I think that this new route will make a  much clearer and complete map because the LiDAR sensor will have more ares to scan that were blocked. However, even though I want this route to be faster, exploring additional areas missed in route 1 might take longer.
