# mission_3 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### technical_analysis

I predicted that increasing speed and having too little derivative control would increase tracking error as well as reduce safety. The robot creates the heading from its current position to the next point and then compares it with its estimated heading. The controller then uses this heading error to adjust the wheel speeds to make sure the robot is back on track. Even with well-tuned PID, an inaccurate odometry can cause the controller to follow the wrong path.

### human_centered_analysis

The consequential failure would be the robot getting too close to a pedestrian and maybe hitting them. This can be due to it not following the proper path. I would choose more pedestrian clearance and use a slower speed because safety is more important than completing the delivery faster. The engineers are responsibile for verifying the deicisons.