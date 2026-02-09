import math


def distance_3d(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx: int = x2 - x1
    dy: int = y2 - y1
    dz: int = z2 - z1
    return math.sqrt((dx * dx) + (dy * dy) + (dz * dz))


def parse_coordinates(raw: str) -> tuple[int, int, int]:
    parts: list[str] = raw.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


if __name__ == "__main__":
    print("=== Game coordinate system ===")
    origin: tuple[int, int, int] = (0, 0, 0)
    pos1: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {pos1}")
    d1: float = distance_3d(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {d1:.2f}")
    print()

    raw_ok: str = "3, 4, 0"
    print(f'parsing coordinates: "{raw_ok}"')
    pos2: tuple[int, int, int] = parse_coordinates(raw_ok)
    print(f"Parsed position: {pos2}")
    d2: float = distance_3d(origin, pos2)
    print(f"distance between {origin} and {pos2}: {d2}")

    raw_bad: str = "abc, def, ghi"
    print(f"parsing invalid coordinates: {raw_bad}")
    try:
        _ = parse_coordinates(raw_bad)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print()
    print("Unpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y} z={z}")
    print(f"coordinates: x={x}, y={y}, z={z}")
