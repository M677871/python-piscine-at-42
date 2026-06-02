from abc import ABC, abstractmethod
from ex0.creature import CreatureFactory, Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target="itself") -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} use Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target="itself and others") -> str:
        return f"{self.name} heals {target} for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Shifting(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shifing", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} morphs into a dragonic battle form!"
        return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} unleashes a devastating morph strike!"

    def revert(self) -> str:
        return f"{self.name} stabilizes its form"


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shifting()

    def create_evolved(self) -> Creature:
        return Morphagon()
