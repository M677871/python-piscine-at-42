import sys
import typing


def print_usage() -> None:
    print("Usage: ft_archive_creation.py <file>")


def print_content_block(content: str) -> None:
    print("-----")
    print(content, end="")
    if content != "" and content[-1] != "\n":
        print()
    print("-----")


def close_archive(
    archive: typing.IO[str],
    file_name: str,
    announce: bool,
) -> bool:
    try:
        archive.close()
    except OSError as error:
        print(f"Error closing file '{file_name}': {error}")
        return False
    if announce:
        print(f"File '{file_name}' closed.")
    return True


def read_archive(file_name: str) -> tuple[bool, str]:
    archive: typing.IO[str] | None = None

    print(f"Accessing file '{file_name}'")
    try:
        archive = open(file_name)
        content: str = archive.read()
        print_content_block(content)
    except (OSError, UnicodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return False, ""
    finally:
        if archive is not None:
            if not close_archive(archive, file_name, True):
                return False, ""
    return True, content


def add_archive_markers(content: str) -> str:
    transformed: str = ""

    for line in content.splitlines(True):
        if line.endswith("\r\n"):
            transformed += line[:-2] + "#\r\n"
        elif line.endswith("\n"):
            transformed += line[:-1] + "#\n"
        elif line.endswith("\r"):
            transformed += line[:-1] + "#\r"
        else:
            transformed += line + "#"
    return transformed


def save_archive(file_name: str, content: str) -> bool:
    archive: typing.IO[str] | None = None
    closed: bool = True

    print(f"Saving data to '{file_name}'")
    try:
        archive = open(file_name, "w")
        archive.write(content)
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return False
    finally:
        if archive is not None:
            closed = close_archive(archive, file_name, False)
    if not closed:
        return False
    print(f"Data saved in file '{file_name}'.")
    return True


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print_usage()
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    success, content = read_archive(argv[1])
    if not success:
        return

    transformed: str = add_archive_markers(content)
    print("Transform data:")
    print_content_block(transformed)

    new_file_name: str = input("Enter new file name (or empty): ")
    if new_file_name == "":
        print("Not saving data.")
        return
    if not save_archive(new_file_name, transformed):
        print("Data not saved.")


if __name__ == "__main__":
    main(sys.argv)
