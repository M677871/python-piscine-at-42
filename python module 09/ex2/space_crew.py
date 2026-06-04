from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")

        has_leader = any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        )

        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1
                for member in self.crew
                if member.years_experience >= 5
            )

            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        crew_members = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=15
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=8
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=6
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 7, 1, 8, 0, 0),
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")

        for member in mission.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) - "
                f"{member.specialization}"
            )

    except ValidationError as error:
        print(error)

    print("=" * 40)

    try:
        bad_crew = [
            CrewMember(
                member_id="CM004",
                name="Bob Lee",
                rank=Rank.officer,
                age=28,
                specialization="Science",
                years_experience=3
            ),
            CrewMember(
                member_id="CM005",
                name="Tom Ray",
                rank=Rank.lieutenant,
                age=31,
                specialization="Medical",
                years_experience=4
            )
        ]

        SpaceMission(
            mission_id="M_BAD_01",
            mission_name="Invalid Mission",
            destination="Venus",
            launch_date=datetime(2024, 7, 1, 8, 0, 0),
            duration_days=100,
            crew=bad_crew,
            budget_millions=500.0
        )

    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
