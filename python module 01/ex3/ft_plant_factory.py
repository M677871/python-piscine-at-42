class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age_days: int = age_days

    def get_info(self) -> str:
        return f"{self.name}: ({self.height}cm, {self.age_days} days)"


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]
    total_plants = len(plants)

    for i in range(total_plants):
        print(f"Created: {plants[i].get_info()}")
    print(f"Total plants created: {total_plants}")


if __name__ == "__main__":
    main()
