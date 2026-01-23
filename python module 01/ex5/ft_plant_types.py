class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    @property
    def height(self) -> int:
        return self._height
    @height.setter
    def height(self, value: int) -> None:
        if value < 0:
            self._height = 0
            print("Security: Negative height rejected")
        else:
            self._height = value
    @property
    def age(self) -> int:
        return self._age
    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            self._age = 0
            print("Security: Negative age rejected")
        else:
            self._age = value


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    @property
    def color(self) -> str:
        return self._color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name,height,age)
        self.trunk_diameter = trunk_diameter

    @property
    def trunk_diameter(self) -> int:
        return self._trunk_diameter

    @trunk_diameter.setter
    def trunk_diameter(self, trunk_diameter: int) -> None:
        if trunk_diameter < 0:
            print("the truck diamter should be positive")
            self._trunk_diameter = 0
        else:
            self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrional_value = nutritional_value

    def info(self) -> None:
         print(f"{self.name} is rich in {self.nutritional_value}")

def main() -> None:
    print("=== Plant Types Test ===")
    # rose = Flower("Rose", 25, 30, "Red")
    # oak = Tree("Oak", 200, 365, 50)
    # carrot = Vegetable("Carrot", 15, 120, "Fall", "Vitamin A")
