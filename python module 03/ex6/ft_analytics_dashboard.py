PlayerRow = tuple[str, int, list[str], str]


def print_title(title: str) -> None:
    print(title)


def get_sample_data() -> tuple[list[PlayerRow], list[str], list[int]]:
    players_data: list[PlayerRow] = [
        (
            "alice",
            2300,
            [
                "first_kill",
                "level_10",
                "treasure_hunter",
                "speed_demon",
                "boss_slayer",
            ],
            "north",
        ),
        (
            "bob",
            1800,
            ["first_kill", "level_10", "collector"],
            "east",
        ),
        (
            "charlie",
            2150,
            [
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist",
                "legendary",
                "master",
            ],
            "central",
        ),
        (
            "diana",
            2400,
            ["first_kill", "boss_slayer", "collector", "legendary"],
            "north",
        ),
        (
            "eve",
            1650,
            ["treasure_hunter", "collector"],
            "east",
        ),
        (
            "frank",
            1950,
            ["first_kill", "level_10", "speed_demon"],
            "central",
        ),
    ]

    all_players: list[str] = [
        player[0] for player in players_data
    ]
    all_scores: list[int] = [
        player[1] for player in players_data
    ]

    return players_data, all_players, all_scores


def demonstrate_list_comprehensions(
    players_data: list[PlayerRow],
    all_scores: list[int],
) -> None:
    print_title("=== list Comprehension Examples ===")

    high_scorers: list[str] = [
        player[0] for player in players_data if player[1] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled: list[int] = [
        score * 2 for score in all_scores
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [
        player[0]
        for player in players_data
        if len(player[2]) >= 3
    ]
    print(
        f"Active players (>=3 achievements): "
        f"{active_players}"
    )


def demonstrate_dict_comprehensions(
    players_data: list[PlayerRow],
) -> None:
    print_title("=== dict Comprehension Examples ===")

    player_scores: dict[str, int] = {
        player[0]: player[1] for player in players_data
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len(
            [
                player
                for player in players_data
                if player[1] > 2000
            ]
        ),
        "medium": len(
            [
                player
                for player in players_data
                if 1800 <= player[1] <= 2000
            ]
        ),
        "low": len(
            [
                player
                for player in players_data
                if player[1] < 1800
            ]
        ),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        player[0]: len(player[2]) for player in players_data
    }
    print(f"Achievement counts: {achievement_counts}")


def demonstrate_set_comprehensions(
    players_data: list[PlayerRow],
    all_players: list[str],
) -> set[str]:
    print_title("=== set Comprehension Examples ===")

    unique_players: set[str] = {
        name for name in all_players
    }
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {
        ach
        for player in players_data
        for ach in player[2]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {
        player[3] for player in players_data
    }
    print(f"Active regions: {active_regions}")

    return unique_achievements


def demonstrate_combined_analysis(
    players_data: list[PlayerRow],
    all_players: list[str],
    all_scores: list[int],
    unique_achievements: set[str],
) -> None:
    print_title("=== Combined Analysis ===")

    print(f"Total players: {len(all_players)}")
    print(
        f"Total unique achievements: "
        f"{len(unique_achievements)}"
    )

    average_score: float = sum(all_scores) / len(all_scores)
    print(f"Average score: {average_score}")

    top_score: int = max(all_scores)
    top_players: list[str] = [
        player[0]
        for player in players_data
        if player[1] == top_score
    ]
    top_ach_counts: list[int] = [
        len(player[2])
        for player in players_data
        if player[1] == top_score
    ]

    if len(top_players) > 0:
        print(
            f"Top performer: {top_players[0]} "
            f"({top_score} points, "
            f"{top_ach_counts[0]} achievements)"
        )

    lowest_score: int = min(all_scores)
    lowest_players: list[str] = [
        player[0]
        for player in players_data
        if player[1] == lowest_score
    ]

    if len(lowest_players) > 0:
        print(
            f"Lowest score: {lowest_players[0]} "
            f"({lowest_score} points)"
        )

    leaderboard: list[tuple[int, str]] = sorted(
        [
            (player[1], player[0])
            for player in players_data
        ],
        reverse=True,
    )
    print(f"Leaderboard (score, name): {leaderboard}")


def main() -> None:
    print_title("=== Game Analytics Dashboard ===")

    players_data, all_players, all_scores = get_sample_data()

    demonstrate_list_comprehensions(players_data, all_scores)
    demonstrate_dict_comprehensions(players_data)

    unique_achievements = demonstrate_set_comprehensions(
        players_data,
        all_players,
    )

    demonstrate_combined_analysis(
        players_data,
        all_players,
        all_scores,
        unique_achievements,
    )


if __name__ == "__main__":
    main()
