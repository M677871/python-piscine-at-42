def water_plants(plant_list: list[str | None]) -> bool:
    plant: str | None = None

    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError("invalid plant")
            print("Watering", plant)
    except ValueError:
        print("Error: Cannot water", plant, "- invalid plant!")
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
