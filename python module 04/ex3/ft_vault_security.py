def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name) as archive:
                return True, archive.read()
        if action == "write":
            with open(file_name, "w") as archive:
                archive.write(content)
            return True, "Content successfully written to file"
        return False, "Invalid action. Use 'read' or 'write'."
    except (OSError, UnicodeError) as error:
        return False, f"{error}"


def print_read_result(label: str, file_name: str) -> tuple[bool, str]:
    print(label)
    result: tuple[bool, str] = secure_archive(file_name)
    print(result)
    return result


def main() -> None:
    sample_content: str = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    secure_archive("ancient_fragment.txt", "write", sample_content)
    print("=== Cyber Archives Security ===")
    print_read_result(
        "Using 'secure_archive' to read from a nonexistent file:",
        "/not/existing/file",
    )
    print_read_result(
        "Using 'secure_archive' to read from an inaccessible file:",
        "/etc/master.passwd",
    )
    read_result: tuple[bool, str] = print_read_result(
        "Using 'secure_archive' to read from a regular file:",
        "ancient_fragment.txt",
    )
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", read_result[1]))


if __name__ == "__main__":
    main()
