class GardenError(Exception):
    """Base class for garden-related errors."""
    def __init__(self, message: str = "A garden error occured."):
        super().__init__(message)


class PlantError(GardenError):
    """Error raised for plant-related problems."""
    def __init__(self, message: str = "A palnt-related error occured."):
        super().__init__(message)


class WaterError(GardenError):
    """Error raised for watering-related problems."""
    def __init__(self, message: str = "A water-related error occured."):
        super().__init__(message)
        


def check_plant_health(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting!")



def check_water_tank(water_liters: int) -> None:
    if water_liters < 5:
        raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        check_plant_health("tomato")
    except PlantError as e:
        print("caught PlantError: ", e)
    print("Testing WaterError...")
    try:
        check_water_tank(2)
    except WaterError as e:
        print("caught WaterError: ", e)
    print("Testing catching all garden errors...")
    arr: list[str] = ["plant", "water"]
    for action in arr:
        try:
            if action == "plant":
                check_plant_health("tomato")
            else:
                check_water_tank(2)
        except GardenError as e:
            print("Caught a garden error: ", e)
    print("All custom error types work correctly!")



if __name__ == "__main__":
        main()
        