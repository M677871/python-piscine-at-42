import sys

def main() -> None:
    print("=== Inventory System Analytics ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        name, qty = arg.split(":")
        inventory[name] = int(qty)
    
    total_items: int = sum(inventory.values())
    unique_items: int = len(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Total item types: {unique_items}")

    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        percent: float = (qty / total_items) * 100
        unit: str = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percent:.1f}%)")
    print("\n ===Inventory statistics ===")
    most_item: str = max(inventory, key = inventory.get)
    least_min: str = min(inventory, key = inventory.get)

    print(f"Most abundant: {most_item} ({inventory[most_item]} units)")
    print(f"Least abundant: {least_min} ({inventory[least_min]}) units")
    print("\n=== Item Categories ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}

    for item, qty in inventory.items():
        if qty >= 5:
             moderate[item] = qty
        else:
            scarce[item] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print(f"\n=== Management Suggestions ===")
    restock: list[str] = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)

    print(f"Restock needed: {restock}")
    print("\n === Dictionary Properties Deno ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()