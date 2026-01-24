class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)

    plants: list[Plant] = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    len_of_array: int = len(plants)
    for i in range(len_of_array):
        print(f"{plants[i].name}: {plants[i].height}cm, "
              f"{plants[i].age} days old")
