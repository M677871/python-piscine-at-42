class PlantError(Exception):
    def __init__(self, message: str = "A plant error occurred."):
        super().__init__(message)


def water_plants(plant_list: list[str | None]) -> bool:
    plant: str | None = None

    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise PlantError(
                    f"Error: Cannot water {plant} - invalid plant"
                )
            print("Watering", plant)
    except PlantError as e:
        print(e)
        return False
    finally:
        print("Closing watering system (cleanup)")

    return True


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    if water_plants(["tomato", "lettuce", "carrots"]):
        print("Watering completed successfully!")

    print("Testing with error...")
    if not water_plants(["tomato", None, "carrots"]):
        print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
