class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, n: str, h: int, age: int, td: int) -> None:
        super().__init__(n, h, age)
        self.td = td

    def produce_shade(self) -> None:
        shade = self.td * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        h: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, h, age)
        self.harvest_season = harvest_season
        self.nutrional_value = nutritional_value

    def info(self) -> None:
        print(f"{self.name} is rich in {self.nutrional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 5, 10, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    cedar = Tree("Cedar", 1000, 5555, 100)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    cucumber = Vegetable("Cucumber", 30, 40, "summer", "vitamin A")

    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print(f"{tulip.name} (Flower): {tulip.height}cm, "
          f"{tulip.age} days, {tulip.color} color")
    tulip.bloom()

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.td}cm diameter")
    oak.produce_shade()
    print(f"{cedar.name} (Tree): {cedar.height}cm, {cedar.age} days, "
          f"{cedar.td}cm diameter")
    cedar.produce_shade()

    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
          f"{tomato.harvest_season} harvest")
    tomato.info()
    print(f"{cucumber.name} (Vegetable): {cucumber.height}cm, "
          f"{cucumber.age} days, {cucumber.harvest_season} harvest")
    cucumber.info()


if __name__ == "__main__":
    main()
