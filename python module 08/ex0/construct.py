import sys
import os
import site


def main() -> None:
    if sys.prefix != sys.base_prefix:
        env_path = os.environ.get("VIRTUAL_ENV", sys.prefix)

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(env_path)}")
        print(f"Environment path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("safe to install packages without affecting")
        print("the global system")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.excepthook}")
        print("Virtual Environment. None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("the machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")


if __name__ == "__main__":
    main()
