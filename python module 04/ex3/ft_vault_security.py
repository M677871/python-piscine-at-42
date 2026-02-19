def print_header() -> None:
    print("=== CYBER ARCHIVES- VAULT SECURITY SYSTEM ===")

def secure_read(filename: str) -> str:
    with open(filename, "r") as f:
        data: str = f.read()
        return data


def secure_write(filename: str, text: str) -> None:
    with open(filename, "w") as f:
        f.write(text)


def main() -> None:
    print_header()

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    read_file: str = "some_classified_read.txt"
    write_file: str = "some_classified_write.txt"
    write_text: str = "[CLASSIFIED] New Security protocols archived\n"

    print("SECURE EXTRACTION")
    data: str = secure_read(read_file)
    print(data, end="")

    print("SECURE PRESERVATION")
    secure_write(write_file, write_text)

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()