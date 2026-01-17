def ft_harvest_total() -> None:
    day_one_harvest = int(input("Day 1 harvest: "))
    day_tow_harvest = int(input("Day 2 harvest: "))
    day_three_harvest = int(input("Day 3 harvest: "))
    total_days = day_one_harvest + day_tow_harvest + day_three_harvest
    print(f"Total harvest: {total_days}")
