class GardenError(Exception):
    """Basw class for garden-related errors."""


class PlantError(GardenError):
    """Error raised for plant-related problems."""


class WaterError(GardenError):
    """Error raised for water-related problems."""


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []


    def add_plants(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print("Added", plant_name, "successfully")
    

    # def check_plant_health(self, plant_name: str, water_level: int, sunlight_hours: int) -> str:



        
