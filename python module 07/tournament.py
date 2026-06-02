from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
)


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
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            if not s1.is_valid(c1):
                classname = s1.__class__.__name__.replace(
                    'Strategy', ''
                ).lower()
                print(
                    "Battle error, aborting tournament: "
                    f"Invalid Creature '{c1.name}' for this "
                    f"{classname} strategy"
                )
                return

            if not s2.is_valid(c2):
                classname = s2.__class__.__name__.replace(
                    'Strategy', ''
                ).lower()
                print(
                    "Battle error, aborting tournament: "
                    f"Invalid Creature '{c2.name}' for this "
                    f"{classname} strategy"
                )
                return

            s1.act(c1)
            s2.act(c2)


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
