# Week 6 — SLAM and Localization

This individual lab uses ROS 2 Jazzy, TurtleBot3 simulation, SLAM Toolbox, AMCL, RViz, and a Streamlit guide. Students use existing robotics systems to investigate how motion and sensor evidence support—or fail to support—a map and a pose belief.

## Student path

1. Guided Tutorial 1: encoders, dead reckoning, and accumulated error.
2. Guided Tutorial 2: topological versus metric maps and occupancy-grid updates.
3. ROS preflight and Guided Tutorial 3: identify measurements, estimates, and accumulated map evidence in RViz.
4. Mission 1: predict a route, map, revisit, save, and interpret.
5. Mission 2: predict and compare a controlled second strategy.
6. Guided Tutorials 4 and 5: move from SLAM to localization and read AMCL's particle belief.
7. Mission 3: predict and record four clean-start localization conditions, then apply a safe decision rule.
8. Write the technical synthesis and separate individual reflection; prepare and inspect the submission.

The guide marks original predictions before results. A prediction can be wrong and still be valuable evidence of learning. Do not edit PGM maps or evidence JSON by hand.

## Start the shared course environment

From the repository root, use the one-time setup described in [ROS_DOCKER_SETUP.md](../ROS_DOCKER_SETUP.md). Then start Lab 6:

Windows:

```powershell
.\scripts\ros_course.ps1 lab week06_slam_localization
```

macOS/Linux:

```bash
./scripts/ros_course.sh lab week06_slam_localization
```

In the browser desktop terminal, run:

```bash
bash scripts/course_preflight.sh
```

The guide opens at `http://localhost:8501`. The course launcher sets `ROS_DOMAIN_ID=26` and opens the lab directory. Follow the guide's separate terminal blocks; leave the mapping or localization launch open while running its companion commands. Stop the robot before switching terminals. Never run two Gazebo worlds or two localization systems in the same domain.

If the simulator or recorder fails, preserve `student_submission/` and rerun only the missing condition. The guide can read files from `runtime/` automatically, accept uploads when running separately, and reopen previously saved submission artifacts. In Mission 2, keep the world, robot, map resolution, starting conditions, and approximate duration as similar as practical.

## What the numbers mean

Known fraction, speckles, border contact, and the composite map score help compare maps but do not establish a true geometric map error. AMCL covariance measures modeled uncertainty, not actual position error. The supplied recorder only reports true position/heading error when it receives a separately verified `/course_reference_pose` in the `map` frame. The standard course launch does not guarantee that topic, so a missing reference is reported as unavailable; use RViz and the simulated robot for a clearly labeled qualitative judgment. Do not claim numeric true error from covariance.

## Submission and recovery

Prepare the submission in the guide. Its readiness table checks current mission artifacts, writing, and identity. The manifest records file hashes; download the ZIP as a backup. In your personal fork, commit the complete `student_submission/` directory from the repository root:

```bash
git status
git add week06_slam_localization/student_submission
git commit -m "Submit Lab 6"
git push origin main
```

Open the commit on GitHub, verify that it contains your submission files, and submit its URL through the course submission system. The ZIP is a backup, not an automatic upload.

If the guide reports an unreadable autosave, do not reset or delete files. Copy `student_submission/` somewhere safe and contact the instructor. A prior valid autosave is recovered automatically when possible, with the unreadable copy preserved.

## Maintainer verification

ROS-independent tests:

```bash
python3 app.py --smoke-test
python3 -m unittest discover -s tests -v
python3 -m compileall -q app.py analysis lab missions pages ros2_ws/src/course_slam_tools/course_slam_tools
```

Full release verification must run in the course ROS 2 container: build `ros2_ws`, run preflight, produce both maps, verify the YAML/PGM pairs and previews, run four clean-start localization conditions (including degraded scan), restart the browser, and prepare the final ZIP. Check that a confidence-only result is not labeled true error. A map-frame reference topic, if supplied for an instructor demonstration, must be calibrated and independently checked against Gazebo before numeric localization error is used for assessment.
