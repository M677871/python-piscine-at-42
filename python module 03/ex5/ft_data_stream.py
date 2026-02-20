import typing
import time


def print_header() -> None:
    print("=== Game Data Stream Processor ===")


def game_event_generator(
    total_events: int,
) -> typing.Generator[str, None, None]:
    players: list[str] = ["alice", "bob", "charlie", "diana", "eve"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]

    i: int = 0
    while i < total_events:
        player_idx: int = i % len(players)
        action_idx: int = i % len(actions)
        level: int = 5 + (i % 15)

        player: str = players[player_idx]
        action: str = actions[action_idx]

        event: str = f"Player {player} (level {level}) {action}"
        yield event
        i += 1


def fibonacci_generator(limit: int) -> typing.Generator[int, None, None]:
    a: int = 0
    b: int = 1
    count: int = 0

    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i: int = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(limit: int) -> typing.Generator[int, None, None]:
    count: int = 0
    candidate: int = 2

    while count < limit:
        if is_prime(candidate):
            yield candidate
            count += 1
        candidate += 1


def process_events_stream(event_stream: typing.Generator[str, None, None],
                          show_first: int) -> tuple[int, int, int, int]:
    total_events: int = 0
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0

    for event in event_stream:
        if total_events < show_first:
            print(f"Event {total_events + 1}: {event}")
        elif total_events == show_first:
            print("...")

        level_start: int = event.find("level ") + 6
        level_end: int = event.find(")", level_start)
        level: int = int(event[level_start:level_end])

        total_events += 1

        if level >= 10:
            high_level_players += 1

        if "treasure" in event:
            treasure_events += 1

        if "leveled up" in event:
            level_up_events += 1

    return total_events, high_level_players, treasure_events, level_up_events


def print_stream_analytics(
    total: int,
    high_level: int,
    treasure: int,
    level_up: int,
    processing_time: float,
) -> None:
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")


def print_generator_demonstrations() -> None:
    print("=== Generator Demonstration ===")

    fib_gen: typing.Generator[int, None, None] = fibonacci_generator(10)
    fib_values: list[str] = []

    for fib_num in fib_gen:
        fib_values.append(str(fib_num))

    print(f"Fibonacci sequence (first 10): {', '.join(fib_values)}")

    prime_gen: typing.Generator[int, None, None] = prime_generator(5)
    prime_values: list[str] = []

    for prime_num in prime_gen:
        prime_values.append(str(prime_num))

    print(f"Prime numbers (first 5): {', '.join(prime_values)}")


def main() -> None:
    print_header()

    total_events: int = 1000
    print(f"Processing {total_events} game events...")

    event_stream: typing.Generator[str, None, None] = (
        game_event_generator(total_events)
    )

    start_time: float = time.time()
    total: int
    high_level: int
    treasure: int
    level_up: int
    total, high_level, treasure, level_up = (
        process_events_stream(event_stream, 3)
    )
    end_time: float = time.time()

    processing_time: float = end_time - start_time

    print_stream_analytics(total, high_level, treasure, level_up,
                           processing_time)

    print_generator_demonstrations()


if __name__ == "__main__":
    main()
