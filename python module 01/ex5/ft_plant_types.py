"""Exercise 6: Garden Analytics Platform"""


class Plant:
    """Base plant."""

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        """Grow plant."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Flowering plant."""

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """Prize flower."""

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    """Manages multiple gardens."""

    total_gardens = 0

    class GardenStats:
        """Statistics helper."""

        @staticmethod
        def validate_height(height: int) -> bool:
            """Validate height."""
            return height >= 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant):
        """Add plant to garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Grow all plants."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    @classmethod
    def create_garden_network(cls):
        """Create garden network."""
        print(f"Total gardens managed: {cls.total_gardens}")


def main():
    """Program entry point."""
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

    print("Height validation test:",
          GardenManager.GardenStats.validate_height(-5))

    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
