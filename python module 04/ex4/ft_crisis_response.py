def print_header() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")


def remove_trailing_newline(text: str) -> str:
    if text != "" and text[-1] == "\n":
        return text[:-1]
    return text


def try_recover(filename: str) -> str:
    with open(filename, "r") as f:
        data: str = f.read()
        return data


def handle_access(filename: str, label: str) -> None:
    print(f"{label}: Attempting access to '{filename}'...")

    try:
        data: str = try_recover(filename)
        clean: str = remove_trailing_newline(data)

        print("SUCCESS: Archive recovered - ", end="")
        print(clean)
        print("STATUS: Normal operations resumed")
        print()

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")
        print()


def main() -> None:
    print_header()

    file_one: str = "lost_archive.txt"
    file_two: str = "classified_vault.txt"
    file_three: str = "standard_archive.txt"

    handle_access(file_one, "CRISIS ALERT")
    handle_access(file_two, "CRISIS ALERT")
    handle_access(file_three, "ROUTINE ACCESS")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
