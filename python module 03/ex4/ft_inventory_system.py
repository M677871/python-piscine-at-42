import sys


def print_header() -> None:
    print("=== Inventory System Analysis ===")


def parse_inventory_from_args() -> dict[str, int]:
    inventory: dict[str, int] = dict()

    for arg in sys.argv[1:]:
        name: str
        qty_str: str
        name, qty_str = arg.split(":")
        inventory[name] = int(qty_str)

    return inventory


def calculate_inventory_totals(
    inventory: dict[str, int],
) -> tuple[int, int]:
    total_items: int = sum(inventory.values())
    unique_items: int = len(inventory)
    return total_items, unique_items


def print_inventory_summary(
    total_items: int,
    unique_items: int,
) -> None:
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")


def print_current_inventory(
    inventory: dict[str, int],
    total_items: int,
) -> None:
    print("=== Current Inventory ===")

    for item, qty in inventory.items():
        percent: float = (qty / total_items) * 100
        unit: str = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percent:.1f}%)")


def find_most_and_least_abundant(
    inventory: dict[str, int],
) -> tuple[str, str]:
    most_item: str = max(inventory, key=inventory.get)
    least_item: str = min(inventory, key=inventory.get)
    return most_item, least_item


def print_inventory_statistics(
    inventory: dict[str, int],
) -> None:
    print("=== Inventory Statistics ===")

    most_item: str
    least_item: str
    most_item, least_item = find_most_and_least_abundant(inventory)

    print(
        f"Most abundant: {most_item} "
        f"({inventory[most_item]} units)"
    )
    print(
        f"Least abundant: {least_item} "
        f"({inventory[least_item]} units)"
    )


def categorize_items(
    inventory: dict[str, int],
) -> tuple[dict[str, int], dict[str, int]]:
    moderate: dict[str, int] = dict()
    scarce: dict[str, int] = dict()

    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty

    return moderate, scarce


def print_item_categories(
    moderate: dict[str, int],
    scarce: dict[str, int],
) -> None:
    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def find_restock_items(inventory: dict[str, int]) -> list[str]:
    restock: list[str] = []

    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)

    return restock


def print_management_suggestions(restock: list[str]) -> None:
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")


def print_dictionary_properties(
    inventory: dict[str, int],
) -> None:
    print("=== dictionary Properties Demo ===")

    key_names: list[str] = []
    for key in inventory.keys():
        key_names.append(key)

    value_list: list[int] = []
    for value in inventory.values():
        value_list.append(value)

    print(f"dictionary keys: {', '.join(key_names)}")
    print(
        f"dictionary values: "
        f"{', '.join(map(str, value_list))}"
    )
    print(
        f"Sample lookup- 'sword' in inventory: "
        f"{'sword' in inventory}"
    )


def main() -> None:
    print_header()

    inventory: dict[str, int] = parse_inventory_from_args()

    total_items: int
    unique_items: int
    total_items, unique_items = calculate_inventory_totals(inventory)

    print_inventory_summary(total_items, unique_items)
    print()

    print_current_inventory(inventory, total_items)
    print()

    print_inventory_statistics(inventory)
    print()

    moderate: dict[str, int]
    scarce: dict[str, int]
    moderate, scarce = categorize_items(inventory)

    print_item_categories(moderate, scarce)
    print()

    restock: list[str] = find_restock_items(inventory)
    print_management_suggestions(restock)
    print()

    print_dictionary_properties(inventory)


if __name__ == "__main__":
    main()
