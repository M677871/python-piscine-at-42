class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height_increase: int) -> None:
        self.height += height_increase
    
    def age(self, days: int) -> None:
        self.age += days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


