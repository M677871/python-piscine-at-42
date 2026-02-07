def check_temperature(temp_str: str) -> int:
    temperature: int

    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temperature < 0:
        raise ValueError(f"Error: {temperature} °C is too cold"
                         f"for plants (min 0°C)")

    if temperature > 40:
        raise ValueError(f"Error: {temperature} °C is too hot"
                         f"for plants (max 40°C)")

    return temperature


def test_temperature_input() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]
    value: str
    result: int

    print("=== Garden Temperature Checker ===")

    for value in tests:
        print("Testing temperature: ", value, sep="")
        try:
            result = check_temperature(value)
            print("Temperature ", result, "°C is perfect for plants!", sep="")
        except ValueError as error:
            print(error)

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
