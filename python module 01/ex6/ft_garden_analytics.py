class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self, height: int = 1) -> None:
        self.height += height
        print(f"{self.name} grew {height}cm")

    def __str__(self) -> str:
        return f"{self.name} Tree: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True

    def __str__(self) -> str:
        status: str = "Blooming" if self.blooming else "Not Blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"
            


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points

    def __str__(self) -> str:
        return f"{super().__str__(self)}, Prize points: {self.points}"


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            return height >= 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

def main():
    """Program entry point."""
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()

    print("Height validation test:",
          GardenManager.GardenStats.validate_height(5))

    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()  