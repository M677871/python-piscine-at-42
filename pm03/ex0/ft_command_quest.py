import sys


if __name__ == "__main__":
    print("=== command quest ===")

    argc: int = len(sys.argv)
    args_received: int = (argc - 1)

    if args_received == 0:
        print("no arguments provided!")
        print(f"program name: {sys.argv[0]}")
        print(f"total arguments: {argc}")
    else:
        print(f"program name: {sys.argv[0]}")
        print(f"arguments received: {args_received}")

        i: int = 1
        while i < argc:
            print(f"argument {i}: {sys.argv[i]}")
            i += 1

        print(f"total arguments: {argc}")
