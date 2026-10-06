from dataclasses import dataclass

@dataclass(frozen=True)
class LabConfig:
    id: str
    title: str
    stages: tuple[str, ...]
    missions: tuple[str, ...]
    submission_directory: str = "student_submission"

LAB = LabConfig(
    id="week06_slam_localization",
    title="Week 6: SLAM and Localization",
    stages=("intro", "tutorial_1", "tutorial_2", "preflight", "tutorial_3",
            "mission_1", "mission_2", "tutorial_4", "tutorial_5", "mission_3", "final"),
    missions=("mission_1", "mission_2", "mission_3"),
)
