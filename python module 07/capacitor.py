from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast

def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    
    print("base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(HealCapability, base).heal())
    
    print("evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(HealCapability, evolved).heal())

def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    
    print("base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(TransformCapability, base).transform())
    print(base.attack())
    print(cast(TransformCapability, base).revert())
    
    print("evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).transform())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).revert())

if __name__ == "__main__":
    test_healing()
    test_transform()
