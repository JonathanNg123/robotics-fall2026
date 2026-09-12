# Mission 2

## Measurement Explanation

For the curved trial, estimated traveled path was 0.374 m because it most likely measured the distance the robot travled on a curve path. This is longer than the start-to-end path being 0.359 because that path measured the straight line between where the robot started and where it ended up.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## Motion Comparison

For the cuved trial, the live simulation results matched fairly similar to my prediction. This is because it moved forward while turning right which is what I predicted. The robot moved forward 0.374m while turning right -58.9 degrees which is not one to one with my prediction, but very similar.

## Prediction Locks

{'curve': '2026-09-11T15:53:35.191351+00:00', 'curve_modified': '2026-09-11T15:57:07.616983+00:00', 'rotation': '2026-09-11T15:46:25.125193+00:00', 'straight': '2026-09-11T07:44:08.972337+00:00'}

## Predictions

{'curve': 'I predict a turn to the right while moving forward for 4 seconds because the forward speed is postive and turning speed is negative.', 'curve_modified': 'This curve should be tighter and turn the other way (left) because the forward speed is slightly slower while the turning speed is larger and also positive.', 'rotation': 'I predict its position will stay the same while its direction will turn left for abount 3 seconds.', 'straight': 'I predict the robot will move forward only with no turning and will move 0.45 meters.'}

## Safety Explanation

The command guard checks every driving command before sending it to the robot while also preventing too high of speeds and values that are invalid. The final zero command tells the robot to stop by changing its forward and turning speed to zero. The timeout is needed if a program crashes or communication stops when the robot is in motion
