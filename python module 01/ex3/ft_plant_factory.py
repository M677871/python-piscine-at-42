class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age_days: int = age_days

    def get_info(self) -> str:
        return f"{self.name}: ({self.height}cm, {self.age_days} days)"


def generate_plants(count: int) -> list[Plant]:
    p1: tuple[str, int, int] = ("Rose", 25, 30)
    p2: tuple[str, int, int] = ("Oak", 200, 365)
    p3: tuple[str, int, int] = ("Cactus", 5, 90)
    p4: tuple[str, int, int] = ("Sunflower", 80, 45)
    p5: tuple[str, int, int] = ("Fern", 15, 120)
    plants: list[tuple[str, int, int]] = [p1, p2, p3, p4, p5]
    p: list[Plant] = [None] * count
    for i in range(count):
        name: str = plants[i % 5][0]
        height: int = plants[i % 5][1] + (i % count)
        age: int = plants[i % 5][2] + (7 + i % count)
        p[i] = Plant(name, height, age)
    return p


def main() -> None:
    print("=== Plant Factory Output ===")
    plants: list[Plant] = generate_plants(20)
    total_plants = 0
    for plant in plants:
        print(f"Created: {plant.get_info()}")
        total_plants += 1
    print(f"Total plants created: {total_plants}")


if __name__ == "__main__":
    main()
