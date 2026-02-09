def main() -> None:
    print("=== Achievement Tracker System ===")
    alice: set[str] = (
        ({"first_kill", "level_10", "treasure_hunter", "speed_demon"})
    )
    bob: set[str] = ({"first_kill", "level_10", "boss_slayer", "collector"})
    charlie: set[str] = (
        ({"level_10", "treasure_hunter", "boss_slayer", "speed_demon"})
    )

    print(f"Player alice acheivements: {alice}")
    print(f"Player bob acheivements: {bob}")
    print(f"Player charlie acheivements: {charlie}")

    print("=== Achievement Analytics ===")
    unique_achievements: set[str] = alice.union(bob).union(charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    common_achievemts: set[str] = alice.intersection(bob).intersection(alice)
    print(f"Common to all players: {common_achievemts}")

    bob_or_charlie: set[str] = bob.union(charlie)
    alice_only: set[str] = alice.difference(bob_or_charlie)

    alice_or_charlie: set[str] = alice.union(charlie)
    bob_only: set[str] = bob.difference(alice_or_charlie)

    alice_or_bob: set[str] = alice.union(bob)
    charlie_only: set[str] = charlie.difference(alice_or_bob)

    rare: set[str] = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
