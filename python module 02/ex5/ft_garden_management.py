class GardenError(Exception):
    """Basw class for garden-related errors."""


class PlantError(GardenError):
    """Error raised for plant-related problems."""


class WaterError(GardenError):
    """Error raised for water-related problems."""


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plants(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print("Added", plant_name, "successfully")

    def check_plant_health(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> str:
        if plant_name.strip() == "":
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        return (
            f"{plant_name}: healthy (water: {water_level}, "
            f"sun: {sunlight_hours})"
        )

    def water_plants(self, water_in_tank: int) -> None:
        print("openning water system")
        try:
            plant_count = 0
            for _ in self.plants:
                plant_count += 1
            if water_in_tank < plant_count:
                raise WaterError("not enough water in the tank")

            for plant in self.plants:
                print("Watering", plant, "- success")
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()
    print("Adding plants to garden...")
    plants: list[str] = ["tomato", "lettuce", ""]
    for plant in plants:
        try:
            manager.add_plants(plant)
        except PlantError as e:
            print("Error adding plant:", e)

    print("watering plants...")
    try:
        manager.water_plants(10)
    except WaterError as e:
        print("caught WaterError: ", e)

    print("Checking plant health...")
    try:
        health = manager.check_plant_health("tomato", 5, 8)
        print(health)
    except GardenError as e:
        print("Error checking tomato:", e)
    try:
        health = manager.check_plant_health("lettuce", 15, 8)
        print(health)
    except GardenError as e:
        print("Error checking lettuce:", e)
    print("Testing error recovery...")
    try:
        raise WaterError("not enough water in tank")
    except GardenError as e:
        print("caught GardenError:", e)
    print("system recovery and continuing...")
    print("garden management system test completed!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
