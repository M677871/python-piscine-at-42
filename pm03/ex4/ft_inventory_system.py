import sys
from typing import Dict, List, Tuple


def print_header() -> None:
    print("=== Inventory System Analysis ===")


def parse_inventory_from_args() -> Dict[str, int]:
    inventory: Dict[str, int] = dict()
    
    for arg in sys.argv[1:]:
        name: str
        qty_str: str
        name, qty_str = arg.split(":")
        inventory[name] = int(qty_str)
    
    return inventory


def calculate_inventory_totals(inventory: Dict[str, int]) -> Tuple[int, int]:
    total_items: int = sum(inventory.values())
    unique_items: int = len(inventory)
    return total_items, unique_items


def print_inventory_summary(total_items: int, unique_items: int) -> None:
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")


def print_current_inventory(inventory: Dict[str, int], total_items: int) -> None:
    print("=== Current Inventory ===")
    
    for item, qty in inventory.items():
        percent: float = (qty / total_items) * 100
        unit: str = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percent:.1f}%)")


def find_most_and_least_abundant(inventory: Dict[str, int]) -> Tuple[str, str]:
    most_item: str = max(inventory, key=inventory.get)
    least_item: str = min(inventory, key=inventory.get)
    return most_item, least_item


def print_inventory_statistics(inventory: Dict[str, int]) -> None:
    print("=== Inventory Statistics ===")
    
    most_item: str
    least_item: str
    most_item, least_item = find_most_and_least_abundant(inventory)
    print(f"Most abundant: {most_item} ({inventory[most_item]} units)")
    print(f"Least abundant: {least_item} ({inventory[least_item]} units)")


def categorize_items(inventory: Dict[str, int]) -> Tuple[Dict[str, int], Dict[str, int]]:
    moderate: Dict[str, int] = dict()
    scarce: Dict[str, int] = dict()
    
    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
    
    return moderate, scarce


def print_item_categories(moderate: Dict[str, int], scarce: Dict[str, int]) -> None:
    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def find_restock_items(inventory: Dict[str, int]) -> List[str]:
    restock: List[str] = []
    
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    
    return restock


def print_management_suggestions(restock: List[str]) -> None:
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")


def print_dictionary_properties(inventory: Dict[str, int]) -> None:
    print("=== Dictionary Properties Demo ===")
    key_names: List[str] = []
    for key in inventory.keys():
        key_names.append(key)
    
    value_list: List[int] = []
    for value in inventory.values():
        value_list.append(value)
    
    print(f"Dictionary keys: {', '.join(key_names)}")
    print(f"Dictionary values: {', '.join(map(str, value_list))}")
    print(f"Sample lookup- 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    print_header()
    
    inventory: Dict[str, int] = parse_inventory_from_args()
    
    total_items: int
    unique_items: int
    total_items, unique_items = calculate_inventory_totals(inventory)
    print_inventory_summary(total_items, unique_items)
    print()
    
    print_current_inventory(inventory, total_items)
    print()
    
    print_inventory_statistics(inventory)
    print()
    
    moderate: Dict[str, int]
    scarce: Dict[str, int]
    moderate, scarce = categorize_items(inventory)
    print_item_categories(moderate, scarce)
    print()
    
    restock: List[str] = find_restock_items(inventory)
    print_management_suggestions(restock)
    print()
    
    print_dictionary_properties(inventory)


if __name__ == "__main__":
    main()