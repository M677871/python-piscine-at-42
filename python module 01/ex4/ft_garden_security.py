class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age_days = 0

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            self.__height = 0
            print(f"Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age_days = age
            print(f"Age updated: {age} days [OK]")
        else:
            self.__age_days = 0
            print(f"Security: Negative age rejected")
    
    def get_height(self) -> int:
        return self.__height
    
    def get_age(self) -> int:
        return self.__age_days
    
    def __str__(self) -> str:
        return f"{self.name} ({self.__height}cm, {self.__age_days} days)"

def main() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print(f"Invalid operation attempted: height {-5}cm [REJECTED]")
    rose.set_height(-5)
    print(f"Current plant: {rose}")

if __name__ == "__main__":
    main()

