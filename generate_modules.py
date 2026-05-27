import os

m6 = "python module 06"
m7 = "python module 07"

os.makedirs(f"{m6}/alchemy/grimoire", exist_ok=True)
os.makedirs(f"{m6}/alchemy/transmutation", exist_ok=True)
os.makedirs(f"{m7}/ex0", exist_ok=True)
os.makedirs(f"{m7}/ex1", exist_ok=True)
os.makedirs(f"{m7}/ex2", exist_ok=True)

def w(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

w(f"{m6}/elements.py", """
def create_fire() -> str:
    return "Fire element created"

def create_water() -> str:
    return "Water element created"
""")

w(f"{m6}/alchemy/__init__.py", """
from .elements import create_air
from .potions import healing_potion as heal
from . import transmutation

__all__ = ["create_air", "heal", "transmutation"]
""")

w(f"{m6}/alchemy/elements.py", """
def create_earth() -> str:
    return "Earth element created"

def create_air() -> str:
    return "Air element created"
""")

w(f"{m6}/alchemy/potions.py", """
from alchemy.elements import create_earth, create_air
import elements

def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion() -> str:
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"
""")

w(f"{m6}/alchemy/transmutation/__init__.py", """
from . import recipes
__all__ = ["recipes"]
""")

w(f"{m6}/alchemy/transmutation/recipes.py", """
from ..elements import create_air
from alchemy.potions import strength_potion
import elements

def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{elements.create_fire()}'"
""")

w(f"{m6}/alchemy/grimoire/__init__.py", "")

w(f"{m6}/alchemy/grimoire/light_spellbook.py", """
def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    valid_resp = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({valid_resp})"
""")

w(f"{m6}/alchemy/grimoire/light_validator.py", """
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    low_ing = ingredients.lower()
    is_valid = any(a in low_ing for a in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}- {status}"
""")

w(f"{m6}/alchemy/grimoire/dark_spellbook.py", """
from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid_resp = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({valid_resp})"
""")

w(f"{m6}/alchemy/grimoire/dark_validator.py", """
from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    low_ing = ingredients.lower()
    is_valid = any(a in low_ing for a in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}- {status}"
""")


w(f"{m6}/ft_alembic_0.py", """
import elements

print("=== Alembic 0 ===")
print("Using: 'import ...' structure to access elements.py")
print(f"Testing create_fire: {elements.create_fire()}")
""")

w(f"{m6}/ft_alembic_1.py", """
from elements import create_water

print("=== Alembic 1 ===")
print("Using: 'from ... import ...' structure to access elements.py")
print(f"Testing create_water: {create_water()}")
""")

w(f"{m6}/ft_alembic_2.py", """
import alchemy.elements

print("=== Alembic 2 ===")
print("Accessing alchemy/elements.py using 'import ...' structure")
print(f"Testing create_earth: {alchemy.elements.create_earth()}")
""")

w(f"{m6}/ft_alembic_3.py", """
from alchemy.elements import create_air

print("=== Alembic 3 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print(f"Testing create_air: {create_air()}")
""")

w(f"{m6}/ft_alembic_4.py", """
import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}") # type: ignore
except Exception as e:
    import traceback
    import sys
    traceback.print_exc(file=sys.stdout)
""")

w(f"{m6}/ft_alembic_5.py", """
from alchemy import create_air

print("=== Alembic 5 ===")
print("Accessing the alchemy module using 'from alchemy import ...'")
print(f"Testing create_air: {create_air()}")
""")

w(f"{m6}/ft_distillation_0.py", """
from alchemy.potions import strength_potion, healing_potion

print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
print(f"Testing strength_potion: {strength_potion()}")
print(f"Testing healing_potion: {healing_potion()}")
""")

w(f"{m6}/ft_distillation_1.py", """
import alchemy
from alchemy.potions import strength_potion

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {strength_potion()}")
print(f"Testing heal alias: {alchemy.heal()}")
""")

w(f"{m6}/ft_transmutation_0.py", """
import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
""")

w(f"{m6}/ft_transmutation_1.py", """
import alchemy.transmutation

print("=== Transmutation 1 ===")
print("Import transmutation module directly")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
""")

w(f"{m6}/ft_transmutation_2.py", """
import alchemy

print("=== Transmutation 2 ===")
print("Import alchemy module only")
print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
""")

w(f"{m6}/ft_kaboom_0.py", """
import alchemy.grimoire.light_spellbook as light

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(f"Testing record light spell: {light.light_spell_record('Fantasy', 'Earth, wind and fire')}")
""")

w(f"{m6}/ft_kaboom_1.py", """
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now- THIS WILL RAISE AN UNCAUGHT EXCEPTION")
from alchemy.grimoire.dark_spellbook import dark_spell_record
print(dark_spell_record("Test", "bats"))
""")

# ================== M7 ==================

w(f"{m7}/ex0/creature.py", """
import abc

class Creature(abc.ABC):
    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.creature_type = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")
    def attack(self) -> str:
        return "Flameling uses Ember!"

class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"

class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"

class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass

class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()
    def create_evolved(self) -> Creature:
        return Pyrodon()

class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()
    def create_evolved(self) -> Creature:
        return Torragon()
""")

w(f"{m7}/ex0/__init__.py", """
from .creature import CreatureFactory, FlameFactory, AquaFactory, Creature
__all__ = ["CreatureFactory", "FlameFactory", "AquaFactory", "Creature"]
""")

w(f"{m7}/battle.py", """
from ex0 import FlameFactory, AquaFactory, CreatureFactory

def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())

if __name__ == "__main__":
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    test_battle(FlameFactory(), AquaFactory())
""")


w(f"{m7}/ex1/capabilities.py", """
import abc
from ex0.creature import Creature, CreatureFactory

class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        pass

class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.is_transformed = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass

class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"
    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"
    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()
    def create_evolved(self) -> Creature:
        return Bloomelle()

class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)
    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."
    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"
    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)
    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"
    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()
    def create_evolved(self) -> Creature:
        return Morphagon()
""")

w(f"{m7}/ex1/__init__.py", """
from .capabilities import HealingCreatureFactory, TransformCreatureFactory
__all__ = ["HealingCreatureFactory", "TransformCreatureFactory"]
""")

w(f"{m7}/capacitor.py", """
from ex1 import HealingCreatureFactory, TransformCreatureFactory

def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal()) # type: ignore
    
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal()) # type: ignore

def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform()) # type: ignore
    print(base.attack())
    print(base.revert()) # type: ignore
    
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform()) # type: ignore
    print(evolved.attack())
    print(evolved.revert()) # type: ignore

if __name__ == "__main__":
    test_healing()
    test_transform()
""")


w(f"{m7}/ex2/strategies.py", """
import abc
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability

class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this normal strategy")
        print(creature.attack())

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        trans_creature = creature # type: ignore
        print(trans_creature.transform())
        print(trans_creature.attack())
        print(trans_creature.revert())

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        heal_creature = creature # type: ignore
        print(heal_creature.attack())
        print(heal_creature.heal())
""")

w(f"{m7}/ex2/__init__.py", """
from .strategies import NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleStrategy
__all__ = ["NormalStrategy", "AggressiveStrategy", "DefensiveStrategy", "BattleStrategy"]
""")


w(f"{m7}/tournament.py", """
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy, BattleStrategy

def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            c1 = opponents[i][0].create_base()
            s1 = opponents[i][1]
            
            c2 = opponents[j][0].create_base()
            s2 = opponents[j][1]
            
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            
            if not s1.is_valid(c1):
                classname = s1.__class__.__name__.replace('Strategy', '').lower()
                print(f"Battle error, aborting tournament: Invalid Creature '{c1.name}' for this {classname} strategy")
                return
            if not s2.is_valid(c2):
                classname = s2.__class__.__name__.replace('Strategy', '').lower()
                print(f"Battle error, aborting tournament: Invalid Creature '{c2.name}' for this {classname} strategy")
                return
            
            s1.act(c1)
            s2.act(c2)

if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])
    
    print("\\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])
    
    print("\\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])
""")

print("Successfully written all files.")
