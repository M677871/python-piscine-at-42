from ex0.creature import Creature
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    base1: Creature = factory1.create_base()
    base2: Creature = factory2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())

    print(" fight!")

    print(base1.attack())
    print(base2.attack())


def main() -> None:
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
