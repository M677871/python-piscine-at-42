class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    len_of_array = len(plants)
    for i in range(len_of_array):
        print(f"{plants[i].name}: {plants[i].height}cm, {plants[i].age} days old")