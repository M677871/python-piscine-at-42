from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast

class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
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
        trans_creature = cast(TransformCapability, creature)
        print(trans_creature.transform())
        print(creature.attack())
        print(trans_creature.revert())

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this defensive strategy")
        heal_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(heal_creature.heal())
