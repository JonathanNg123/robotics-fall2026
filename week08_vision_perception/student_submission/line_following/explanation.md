# line_following

## comparison
During the practice, the robot followed the line consistently. For the curved track, the robot did well on the straight sections, but was not great when turning. I then increased the gain to 0.15 and it handled the curves a lot better although not perfect. Increasing the gain makes the robot respond more strongly to the error. The camera mask identifies the magenta line, the image error shows how far it is from the target position, and the steering command uses that error to correct the robot's direction.

## limits
During both curved attempts I noticed that the robot stopped before reaching the red finish marker. I think this is due to the fact that the camera lost track of the line. Additional sensors like LiDAR and depth cameras would help detect people and obstacles.
