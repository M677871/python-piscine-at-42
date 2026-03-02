import math
from typing import Tuple, List


def distance_3d(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> float:
    x1: int
    y1: int
    z1: int
    x1, y1, z1 = p1
    x2: int
    y2: int
    z2: int
    x2, y2, z2 = p2
    dx: int = x2 - x1
    dy: int = y2 - y1
    dz: int = z2 - z1
    return math.sqrt((dx * dx) + (dy * dy) + (dz * dz))


def parse_coordinates(raw: str) -> Tuple[int, int, int]:
    parts: List[str] = raw.split(",")
    return tuple((int(parts[0]), int(parts[1]), int(parts[2])))


def print_header() -> None:
    print("=== Game Coordinate System ===")


def demonstrate_coordinate_creation() -> None:
    origin: Tuple[int, int, int] = tuple((0, 0, 0))
    pos1: Tuple[int, int, int] = tuple((10, 20, 5))
    print(f"Position created: {pos1}")

    d1: float = distance_3d(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {d1:.2f}")
    print()


def demonstrate_coordinate_parsing() -> Tuple[int, int, int]:
    origin: Tuple[int, int, int] = tuple((0, 0, 0))
    raw_ok: str = "3,4,0"
    print(f'Parsing coordinates: "{raw_ok}"')

    pos2: Tuple[int, int, int] = parse_coordinates(raw_ok)
    print(f"Parsed position: {pos2}")

    d2: float = distance_3d(origin, pos2)
    print(f"Distance between {origin} and {pos2}: {d2}")

    return pos2


def demonstrate_error_handling() -> None:
    raw_bad: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {raw_bad}")

    try:
        parse_coordinates(raw_bad)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details- Type: {type(e).__name__}, Args: {e.args}")
    print()


def demonstrate_unpacking(pos: Tuple[int, int, int]) -> None:
    print("Unpacking demonstration:")
    x: int
    y: int
    z: int
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print_header()

    demonstrate_coordinate_creation()

    pos2: Tuple[int, int, int] = demonstrate_coordinate_parsing()

    demonstrate_error_handling()

    demonstrate_unpacking(pos2)


if __name__ == "__main__":
    main()
