"""
helpers.py
Utility functions for inventory calculations.
"""

def highest_stock_item(inventory: list) -> dict:
    """Returns the item dictionary with the highest quantity."""
    if not inventory:
        return {}
    return max(inventory, key=lambda x: x.get("quantity", 0))

def lowest_stock_item(inventory: list) -> dict:
    """Returns the item dictionary with the lowest quantity."""
    if not inventory:
        return {}
    return min(inventory, key=lambda x: x.get("quantity", 0))