"""
app.py
Main application script to calculate and display inventory status.
(Preventive Maintenance: Added docstrings and modularized the main logic)
"""
from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item

def calculate_total_value(inventory_list: list) -> float:
    # Adaptive Maintenance: Added type hints and a dedicated calculation function
    # Corrective Maintenance: Added a guard against empty inventory lists to prevent crash errors
    if not inventory_list:
        return 0.0
        
    total = 0.0
    for item in inventory_list:
        total += (item.get("quantity", 0) * item.get("price", 0.0))
    return total

def main():
    total_value = calculate_total_value(items)
    
    # Perfective Maintenance: Improved output formatting with f-strings and a clean UI table
    print("="*45)
    print(" 📦 INVENTORY STATUS ACCOUNTING REPORT ")
    print("="*45)
    print(f"Total Inventory Value: ${total_value:,.2f}\n")
    
    if items:
        highest = highest_stock_item(items)
        lowest = lowest_stock_item(items)
        print(f"Highest Stock Item: {highest['item_name']} ({highest['quantity']} units)")
        print(f"Lowest Stock Item:  {lowest['item_name']} ({lowest['quantity']} units)")
    print("="*45)

if __name__ == "__main__":
    main()