import sys


def print_header() -> None:
    print("=== Command Quest ===")


def get_program_name() -> str:
    return sys.argv[0]


def get_total_arguments() -> int:
    return len(sys.argv)


def get_arguments_received() -> int:
    return len(sys.argv) - 1


def has_arguments() -> bool:
    return get_arguments_received() > 0


def print_no_arguments_info() -> None:
    print("No arguments provided!")
    print(f"Program name: {get_program_name()}")
    print(f"Total arguments: {get_total_arguments()}")


def print_with_arguments_info() -> None:
    print(f"Program name: {get_program_name()}")
    print(f"Arguments received: {get_arguments_received()}")

    arguments_count: int = get_arguments_received()
    i: int = 1
    while i <= arguments_count:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {get_total_arguments()}")


def main() -> None:
    print_header()

    if has_arguments():
        print_with_arguments_info()
    else:
        print_no_arguments_info()


if __name__ == "__main__":
    main()
