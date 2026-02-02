class GardenError(Exception):
    """Base class for garden-related errors."""


class PlantError(GardenError):
    """Error raised for plant-related problems."""


class WaterError(GardenError):
    """Error raised for watering-related problems."""


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants = self.plants + [plant_name]

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print("Watering ", plant, " - success", sep="")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int,
    ) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")

        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )

        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        print(
            plant_name,
            ": healthy (water: ",
            water_level,
            ", sun: ",
            sunlight_hours,
            ")",
            sep="",
        )

    def check_water_tank(self, water_level: int) -> None:
        if water_level < 1:
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    manager = GardenManager()

    print("=== Garden Management System ===")
    print("Adding plants to garden...")

    try:
        manager.add_plant("tomato")
        print("Added tomato successfully")
    except GardenError as error:
        print("Error adding plant:", error)

    try:
        manager.add_plant("lettuce")
        print("Added lettuce successfully")
    except GardenError as error:
        print("Error adding plant:", error)

    try:
        manager.add_plant("")
        print("Added  successfully")
    except GardenError as error:
        print("Error adding plant:", error)

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except ValueError as error:
        print("Error checking tomato:", error.args[0])

    try:
        manager.check_plant_health("lettuce", 15, 8)
    except ValueError as error:
        print("Error checking lettuce:", error.args[0])

    print("Testing error recovery...")
    try:
        manager.check_water_tank(0)
    except GardenError as error:
        print("Caught GardenError:", error)

    print("System recovered and continuing...")
    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
