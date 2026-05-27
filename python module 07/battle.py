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
    print()

def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1: Creature = factory1.create_base()
    c2: Creature = factory2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())

if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    
    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
