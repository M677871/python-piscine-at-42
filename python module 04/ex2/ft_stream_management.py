import sys

def print_header() -> None:
    print("=== CYBER ARCHIVES- COMMUNICATION SYSTEM ===")


def ask(prompt: str) -> str:
    answer: str = input(prompt)
    return answer


def write_standard(message: str) -> None:
    sys.stdout.write(message + "\n")


def write_alert(message: str) -> None:
    sys.stderr.write(message + "\n")


def main() -> None:
    print_header()

    id: str = ask("Input Stream active. Enter archivist ID: ")
    status: str = ask("Input Stream active. Enter status report: ")

    write_standard(f"[STANDARD] Archive status from {id}: {status}")
    write_alert("[ALERT] System diagnostic: Communication channels verified")
    write_standard("[STANDARD] Data transmission complete")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()