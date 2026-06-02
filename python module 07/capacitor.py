from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


def test_healing() -> None:
    print("Testing Creature with healing capability")
    print(" base:")

    factory = HealingCreatureFactory()

    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(HealCapability, base).heal())

    evolved: Creature = factory.create_evolved()
    print(" envolved")
    print(evolved.describe())
    print(evolved.attack())
    print(cast(HealCapability, base).heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    print(" base:")

    factory = TransformCreatureFactory()

    base: Creature = factory.create_base()

    print(base.describe())
    print(base.attack())
    print(cast(TransformCapability, base).revert())
    print(base.attack())
    print(cast(TransformCapability, base).revert())
    print(" evolved:")

    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).transform())
    print(evolved.attack())
    print(cast(TransformCapability, base).revert())


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()
