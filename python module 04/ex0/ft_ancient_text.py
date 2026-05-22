import sys
import typing


def print_usage() -> None:
    print("Usage: ft_ancient_text.py <file>")


def print_content_block(content: str) -> None:
    print("-----")
    print(content, end="")
    if content != "" and content[-1] != "\n":
        print()
    print("-----")


def close_archive(archive: typing.IO[str], file_name: str) -> None:
    try:
        archive.close()
        print(f"File '{file_name}' closed.")
    except OSError as error:
        print(f"Error closing file '{file_name}': {error}")


def recover_file(file_name: str) -> None:
    archive: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        archive = open(file_name)
        print_content_block(archive.read())
    except (OSError, UnicodeError) as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if archive is not None:
            close_archive(archive, file_name)


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print_usage()
        return
    recover_file(argv[1])


if __name__ == "__main__":
    main(sys.argv)
