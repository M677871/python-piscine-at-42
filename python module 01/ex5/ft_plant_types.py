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

