from typing import Any
from collections.abc import Callable

from functools import (
    reduce,
    partial,
    lru_cache,
    singledispatch,
)

from operator import add, mul


def spell_reducer(
    spells: list[int],
    operation: str
) -> int:

    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(
        operations[operation],
        spells
    )


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:

    return {
        "fire": partial(
            base_enchantment,
            50,
            "Fire"
        ),
        "ice": partial(
            base_enchantment,
            50,
            "Ice"
        ),
        "lightning": partial(
            base_enchantment,
            50,
            "Lightning"
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")

    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    def enchantment(
        power: int,
        element: str,
        target: str
    ) -> str:
        return (
            f"{element} enchantment "
            f"({power}) on {target}"
        )

    enchanted = partial_enchanter(enchantment)

    print(enchanted["fire"]("Sword"))
    print(enchanted["ice"]("Shield"))
    print(enchanted["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print(
        f"Cache info: {memoized_fibonacci.cache_info()}"
    )

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher({"unknown": "spell"}))
