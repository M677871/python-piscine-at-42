class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age_days: int = age_days

    def grow(self, height_increase: int = 1) -> None:
        self.height += height_increase

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def main() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    height_before_grow: int = rose.height
    print("=== Day 1 ===")
    print(rose.get_info())
    for _ in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - height_before_grow}cm")


if __name__ == "__main__":
    main()
