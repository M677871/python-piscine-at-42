class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    len_of_array = len(plants)
    for i in range(len_of_array):
        plants[i].display()