def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing ValueError...")
    try:
        raise ValueError("invalid literal for int()")
    except ValueError as e:
        print("caught ValueError:", e)
    print("Testing ZeroDivisionError...")
    try:
        water = 10
        plants = 0
        _ = water / plants
    except ZeroDivisionError as e:
        print("caught ZeroDivisionError:", e)
    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(
            "caught FileNotFoundError: No such File '",
            e.filename,
            "'",
            sep="",
        )
    print("Testing KeyError...")
    try:
        garden = {"rose": "needs water", "mint": "grow fast"}
        _ = garden["missing_plant"]
    except KeyError as e:
        print("caught keyError:", e)
    print("Testing multiple errors together...")
    try:
        _ = 1 / 0
    except (ValueError, FileNotFoundError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    print("All error types tested successfully!")


def test_error_types() -> None:
    garden_operations()


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
