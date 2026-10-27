# Lab 7 saved answers

## mission_1.diagnosis
The two images I compared was `normal_1` and `dim_1. In `normal_1`, the detector was able to see that the cup was there, but the green bounding box also included some of the desk. The threshold mask also shows some unwanted areas from the laptop and other objects. In `dim_1`, the lighting appeared to be darker, but the detector still included some parts of the mug and surrounding background. The settings that I used were the ones recommended which  allowed other objects with similar colors to pass the filter. This also shows that these settings used were detecting the presence of a mug, but not necessarily being able to locate it accurately.

## mission_1.limitations
One parameter I changed during practice was thhe brightness. Lowering the minimum brightness made it so darker pixels passed through the color filter. Just like the images that were compared, this helped detect the mug in darker lighting, but it could also included more area around that we did not need. A limitation could be that objects can have similar colors to the mug. This means that changing brightness is not enough as the detector might not give an accurate image due to similar colors.

## mission_2.choice
I would recommend the learned detector with an acceptance threshold of 0.50. This is because it performed better than the classical detector due to the fact it produced fewer false boxes and was able to actaully located one mug under normal conditions. However, it still missed mugs under dim and occluded conditions, so it would need additional testing. Using normal_1, it  had a mask IoU of 0.5756 and a Dice score of 0.7306. Although it looked like the mug was very well highlighted, it included 4,453 extra pixels and missed 1,852 mug pixels. This shows that it does have it's limitations. One important is that it does not show whether the detector would work well with different camera angles or lighting conditions.

## mission_2.comparison
For normal, the detector had 0 correct boxes, 2 false boxes, and 2 missed mugs, while for learned had 1 correct box, 0 false boxes, and 1 missed mug. For dim, the classical detector had 0 correct boxes, 2 false boxes, and 2 missed mugs, while for learned had 0 correct boxes, 0 false boxes, and 2 missed mugs. This was the same for occluded conditions as well. This shows that the learned detector was better at avoiding false detections than the other detectors. In the normal_1 image, it was shown that the classical detector's box had a large area around the mug, while the learned detector's box had a better accuracy on the mug. This matters because detecting an object is different from locating it.

## pillar_search.diagnosis
In my saved blue-only attempt (20261027T055019-77eef8f8), the controller detected and centered the blue pillar. The camera showed the blue pillar while the color mask just showed a white area. The controller used the centroid marker to compare the pillar's position with the center of the image. No setting was changed.

## pillar_search.evidence
In my four-color attempt (20261027T055424-e5479a3b), the robot centered all four pillars in the order red, green, turquoise, and blue. The camera images and color masks showed me how the controller saw the colored regions and used the centroids to adjust its turning direction. However, centering a colored region doesn't mean that that is the correct object. Another object with a similar color could produce the same detection. Additional sensors or information would be needed to estimate distance better.

## line_following.comparison
During the practice, the robot followed the line consistently. For the curved track, the robot did well on the straight sections, but was not great when turning. I then increased the gain to 0.15 and it handled the curves a lot better although not perfect. Increasing the gain makes the robot respond more strongly to the error. The camera mask identifies the magenta line, the image error shows how far it is from the target position, and the steering command uses that error to correct the robot's direction.

## line_following.limits
During both curved attempts I noticed that the robot stopped before reaching the red finish marker. I think this is due to the fact that the camera lost track of the line. Additional sensors like LiDAR and depth cameras would help detect people and obstacles.

## final.synthesis
The three missions taught me how important it is for robots to correctly interpret visual information before making decisions. In Mission 1, after comparing the classical and learned detectors, I learned that the detector was generally better at identifying the mug in normal conditions, but it still struggled with difficult lighting and occlusion. In Mission 2, the robot used its camera to find and center colored pillars. This showed how camera information can guide robot movement. In Mission 3, the robot followed a magenta line using its camera. It performed well on the straight practice route, but no so much on the curved track. Overall, these missions showed me how robot behavior depends on both perception and control settings. 

## final.course_reflection
What stood out about the activity in this lab was how different all 3 missions were. Normally we would do everything with just one terminal use, but this time we needed to open multiple different enviornments. The mission involving the pillars were very interesing as it opened a camera of what the robot actually sees which is the first time ive ever seen that. It was so cool to see the camera update in real time as it turned.
