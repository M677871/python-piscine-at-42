class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self._initial_height: int = height

    def grow(self, height: int = 1) -> None:
        self.height += height
        print(f"{self.name} grew {height}cm")

    def growth_amount(self) -> int:
        return self.height - self._initial_height

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True

    def __str__(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{super().__str__()}, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points: int = points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.points}"


class GardenManager:
    total_gardens: int = 0
    all_gardens: list["GardenManager"] = []

    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            return height >= 0

        @staticmethod
        def plant_type_count(plants: list[Plant]) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1

            return regular, flowering, prize

        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            total = 0
            for plant in plants:
                total += plant.growth_amount()
            return total

        @staticmethod
        def garden_score(plants: list[Plant]) -> int:
            score = 0
            for plant in plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            return score

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        GardenManager.total_gardens += 1
        GardenManager.all_gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")

        regular, flowering, prize = self.GardenStats.plant_type_count(
            self.plants
        )
        growth = self.GardenStats.total_growth(self.plants)

        plant_count = 0
        for _ in self.plants:
            plant_count += 1

        print(f"Plants added: {plant_count}, Total growth: {growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    def score(self) -> int:
        return self.GardenStats.garden_score(self.plants)

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")


def main() -> None:
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()

    print("=== Alice's Garden Report ===")
    alice.report()

    print(
        "Height validation test:",
        GardenManager.GardenStats.validate_height(5),
    )

    print(
        f"Garden scores - Alice: {alice.score()}, Bob: {bob.score()}"
    )

    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
