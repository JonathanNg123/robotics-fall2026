# mission_2 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### prediction

The estimated forward distance will be greater than the robot's actual distance. If the strafe pod is too small, the sideway distance will be less than the robot's actual distance.

### calibration_analysis

I predicted that a forward scale that was too large would overestimate the forward distance while a strafe scale that was too small would underestimate the sideways distance. The forward scale changed how the encoder ticks were turned into forward distance while the strafe scale changed how the sideways movement was estimated. The sideways pod is necessary because a robot can move sideways with no turns so the forward pod can not measure all of the motion. Some drift remained after calibration because odometry is only an estimate and small errors can always occur.