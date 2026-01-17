def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count(day: int) -> None:
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)

    count(1)
