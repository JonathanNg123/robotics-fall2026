# Instructor notes — Week 6

## Intent and teaching sequence

This lab teaches students to investigate SLAM and localization, not implement the underlying algorithms. The five tutorials are deliberately short bridges from earlier labs: dead reckoning from Lab 4, evidence interpretation from Labs 1 and 3, and sensor uncertainty and safe decisions from Lab 5. Students make predictions before each experiment, then use measured and visual evidence to revise their understanding.

The current mission numbering is unchanged: Mission 1 makes the first map; Mission 2 compares a second strategy; Mission 3 contains all four AMCL trials, including the degraded-scan analysis. The student guide allows revisiting tutorials and completed work.

## Timing to pilot

The previous 3–3.5-hour estimate should be rechecked with an unfamiliar student after adding the tutorials. Aim for short tutorial interactions and reserve most time for two mapping runs and four localization trials. If the pilot runs long, streamline explanations or launch overhead rather than removing controlled runs or forcing a rushed final synthesis.

## Experimental controls and interpretation

For map comparisons, keep the world, robot, map settings, start conditions, and run duration similar. The route strategy should be the main planned change. Students record remaining confounds. Known fraction measures observed area, not correctness. The composite score is a transparent discussion scaffold; inspect wall alignment, duplicated structures, unobserved rooms, and map clipping. Accept a well-supported conclusion that loop-closure evidence is insufficient.

For localization, distinguish three claims:

1. **Concentration:** AMCL covariance or particle spread became smaller.
2. **Consistency:** current scans and estimated pose appear compatible with the map.
3. **Correctness:** an independent reference supports the actual pose.

The recorder subscribes to an optional `/course_reference_pose` PoseStamped topic only when its frame is `map`. The standard launch does not produce a certified reference. Do not grade numeric position error until a source and frame alignment have been tested in the course container. World-frame Gazebo coordinates must not be subtracted directly from map-frame AMCL estimates. The app shows unavailable error as unavailable, not zero. A concentrated but incorrect estimate is an important case for discussion.

The degraded-scan proxy keeps approximately half of scan messages and adds range noise. This is a pedagogical perturbation, not a calibrated physical sensor model. Students compare normal and degraded runs while acknowledging other sources of variation.

## Suggested assessment

- Mission 1 route prediction, guided observations, valid map, and interpretation: 25
- Mission 2 controlled comparison, metrics, visual evidence, and loop-closure reasoning: 25
- Mission 3 four predictions/trials, uncertainty-versus-correctness analysis, and fallback rule: 35
- Evidence-based final synthesis and individual reflection: 10
- Complete, inspectable artifacts: 5

Automated checks establish minimum evidence, not the quality of every causal claim. Manually inspect whether screenshots and numeric data support the student's interpretation, whether controls were credible, and whether uncertainty is treated honestly.

## Support and release checks

- Preflight verifies installed ROS components before a mission; live topic checks occur after launching Gazebo and SLAM.
- If `/map` is absent, check `/scan`, `/odom`, TF, simulated time, and SLAM lifecycle. If map saving times out, wait for `/map` and map-server lifecycle readiness.
- If AMCL has no pose samples, check the initial pose, the map/world match, `/scan`, and frame alignment. For degraded mode, confirm both raw and degraded scan topics.
- Never advise a student to reset, clean, or overwrite their submission in response to a course update. Back up `student_submission/`, inspect `git status`, and preserve their commit.
- Pilot all four trials in the actual shared container before release. Verify map-pair validation, screenshot uploads, browser restart, old-save migration, readiness, ZIP contents, and a personal-fork Git commit.
