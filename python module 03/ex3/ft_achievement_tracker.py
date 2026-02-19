from typing import Set, Tuple


def print_header() -> None:
    print("=== Achievement Tracker System ===")


def create_player_achievements() -> Tuple[Set[str], Set[str], Set[str]]:
    alice: Set[str] = set(("first_kill", "level_10", "treasure_hunter", "speed_demon"))
    bob: Set[str] = set(("first_kill", "level_10", "boss_slayer", "collector"))
    charlie: Set[str] = set(("level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"))
    return alice, bob, charlie


def print_player_achievements(alice: Set[str], bob: Set[str], charlie: Set[str]) -> None:
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")


def calculate_unique_achievements(alice: Set[str], bob: Set[str], charlie: Set[str]) -> Set[str]:
    return alice.union(bob).union(charlie)


def calculate_common_achievements(alice: Set[str], bob: Set[str], charlie: Set[str]) -> Set[str]:
    return alice.intersection(bob).intersection(charlie)


def calculate_rare_achievements(alice: Set[str], bob: Set[str], charlie: Set[str]) -> Set[str]:
    bob_or_charlie: Set[str] = bob.union(charlie)
    alice_only: Set[str] = alice.difference(bob_or_charlie)
    
    alice_or_charlie: Set[str] = alice.union(charlie)
    bob_only: Set[str] = bob.difference(alice_or_charlie)
    
    alice_or_bob: Set[str] = alice.union(bob)
    charlie_only: Set[str] = charlie.difference(alice_or_bob)
    
    return alice_only.union(bob_only).union(charlie_only)


def print_achievement_analytics(alice: Set[str], bob: Set[str], charlie: Set[str]) -> None:
    print("=== Achievement Analytics ===")
    
    unique_achievements: Set[str] = calculate_unique_achievements(alice, bob, charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    
    common_achievements: Set[str] = calculate_common_achievements(alice, bob, charlie)
    print(f"Common to all players: {common_achievements}")
    
    rare_achievements: Set[str] = calculate_rare_achievements(alice, bob, charlie)
    print(f"Rare achievements (1 player): {rare_achievements}")
    print()
    
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
    print(f"Charlie unique: {charlie.difference(alice.union(bob))}")

def main() -> None:
    print_header()
    
    alice: Set[str]
    bob: Set[str] 
    charlie: Set[str]
    alice, bob, charlie = create_player_achievements()
    
    print_player_achievements(alice, bob, charlie)
    print()
    
    print_achievement_analytics(alice, bob, charlie)


if __name__ == "__main__":
    main()
