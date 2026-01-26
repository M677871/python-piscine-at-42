def check_temperature(temp_str: str) -> int:
    temperature: int

    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError("NOT_A_NUMBER")

    if temperature < 0:
        raise ValueError("TOO_COLD")

    if temperature > 40:
        raise ValueError("TOO_HOT")

    return temperature


def test_temperature_input() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]
    value: str
    result: int

    print("=== Garden Temperature Checker ===")

    for value in tests:
        print("Testing temperature:", value)
        try:
            result = check_temperature(value)
            print("Temperature", result, "°C is perfect for plants!")
        except ValueError as error:
            if error.args[0] == "NOT_A_NUMBER":
                print("Error:", "'" + value + "'", "is not a valid number")
            elif error.args[0] == "TOO_HOT":
                print("Error:", value, "°C is too hot for plants (max 40°C)")
            elif error.args[0] == "TOO_COLD":
                print("Error:", value, "°C is too cold for plants (min 0°C)")

    print("All tests completed- program didn't crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
