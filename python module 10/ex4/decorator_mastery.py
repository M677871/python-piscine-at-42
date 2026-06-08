from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            f"spell completed in "
            f"{end - start:.3f} seconds"
        )

        return result

    return wrapper


def power_validator(
    min_power: int
) -> Callable:

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            power = kwargs.get("power")

            if power is None:
                if len(args) >= 2:
                    power = args[-1]

            if power < min_power:
                return (
                    "Insufficient power "
                    "for this spell"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int
) -> Callable:

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(
                1,
                max_attempts + 1
            ):
                try:
                    return func(
                        *args,
                        **kwargs
                    )

                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f" ({attempt}/"
                            f"{max_attempts})"
                        )

            return (
                f"Spell casting failed "
                f"after {max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(
        name: str
    ) -> bool:

        return (
            len(name) >= 3
            and all(
                char.isalpha()
                or char.isspace()
                for char in name
            )
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:

        return (
            f"Successfully cast "
            f"{spell_name} "
            f"with {power} power"
        )


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        print("Result: Fireball cast!")
        return "Fireball cast!"

    fireball()

    print("\nTesting retrying spell...")

    counter = {"attempts": 0}

    @retry_spell(3)
    def unstable_spell():
        counter["attempts"] += 1
        if counter["attempts"] < 3:
            raise Exception("fail")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("X"))

    mage = MageGuild()

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))
