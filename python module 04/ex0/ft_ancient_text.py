def print_header() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")


def read_whole_file(filename: str) -> str:
    f: object = open(filename, "r")
    content: str = f.read()
    f.close()
    return content

def print_recovered_data(data: str) -> None:
    print("RECOVERED DATA:")
    print(data, end="")


def main() -> None:
    filename: str = "ancient_fragment.txt"
    print_header()
    print(f"Accessing Storage vault: {filename}")

    try:
        print("connection established...")
        data: str = read_whole_file(filename)
        print_recovered_data(data)
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"Error: Storage vault not found: Run data generator first.")


if __name__ == "__main__":
    main()

