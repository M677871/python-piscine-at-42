def print_header() -> None:
    print("=== Cyber Archives - Preservation System ===")


def build_entries() -> list[str]:
    entries: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n",
    ]
    return entries


def write_entries(filename: str, entries: list[str]) -> None:
    f: object = open(filename, "w")
    for line in entries:
        f.write(line)
    f.close()


def print_entries(entries: list[str]) -> None:
    for line in entries:
        print(line, end="")


def main() -> None:
    filename: str = "new_discovery.txt"

    print_header()

    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successully...")
    print("Inscribing preservation data...")

    entries: list[str] = build_entries()
    write_entries(filename, entries)
    print_entries(entries)

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()