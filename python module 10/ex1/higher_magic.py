from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return (
            spell1(target, power),
            spell2(target, power)
        )

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")

    def fireball_simple(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal_simple(target: str, power: int) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball_simple, heal_simple)
    res_comb = combined("Dragon", 0)

    print(
        f"Combined spell result: "
        f"{res_comb[0]}, {res_comb[1]}"
    )

    print("\nTesting power amplifier...")

    def check_power(target: str, power: int) -> str:
        return f"{power}"

    mega_spell = power_amplifier(check_power, 3)
    original_power = 10
    amplified_power = mega_spell("Dummy", original_power)
    print(f"Original: {original_power}, Amplified: {amplified_power}")
