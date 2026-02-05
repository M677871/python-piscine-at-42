def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    result: str
    if plant_name == "":
        raise ValueError("Plant name can not be empty!")

    if water_level < 1:
        raise ValueError(f"water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"water level {water_level} is to high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"sunlight hours {sunlight_hours} is too high (max 12)"
        )

    result = "Plant '" + plant_name + "' is healthy!"
    return result


def test_plant_checks() -> None:
    result: str
    print("===  Garden Plant Health checker ===")
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 7, 7)
        print(result)
    except ValueError as e:
        print("Error: ", e)
    print("Testing Empty plant name...")
    try:
        result = check_plant_health("", 7, 7)
        print(result)
    except ValueError as e:
        print("Error: ", e)
    print("testing bad water level...")
    try:
        result = check_plant_health("tomato", 5, 15)
        print(result)
    except ValueError as e:
        print("Error: ", e)
    print("testing bad sunlight hours...")
    try:
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as e:
        print("Error: ", e)

    print("All error raising tests completed!")


def main() -> None:
    test_plant_checks()


if __name__ == "__main__":
    main()
