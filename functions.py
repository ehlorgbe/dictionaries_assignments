import random
import data
def stock_level(food_item):
    """determine random stock levels"""
    dict = {}
    for i in food_item:
        dict.update({i : random.randint(25,50)})
    return dict   

# Updating menu items
def update_item(menu_dicts, item_code, new_description=None, new_price=None):
    if item_code in menu_dicts:
        if new_description:
            menu_dicts[item_code][0] = new_description
        if new_price:
            menu_dicts[item_code][1] = new_price
        print(f"Updated {item_code}: ${menu_dicts[item_code]}")
    else:
        print(f"Item {item_code} not found.")

# Adding new items
def add_item(menu_dicts, item_code, description, price):
    if item_code not in menu_dicts:
        menu_dicts[item_code] = [description, price]
        print(f"Added {item_code}: {menu_dicts[item_code]}")
    else:
        print(f"Item {item_code} already exists.")

# Removing items
def remove_item(menu_dicts, item_code):
    if item_code in menu_dicts:
        del menu_dicts[item_code]
        print(f"Removed {item_code}.")
    else:
        print(f"Item {item_code} not found.")

# Displaying the menu
def display_menu(menu_dicts):
    for item_code, details in menu_dicts.items():
        print(f"{item_code}: {details[0]} - ${details[1]}")



def customer_request(item_code, quantity):
    if item_code not in data.menu_dicts:
        return f"Item {item_code} is not on the menu."
    if item_code in data.menu_dicts:
        stock = all_stock[item_code]
        if quantity > stock:
            return f"Not enough stock for {menu_dicts[item_code]['name']}. Available: {stock}, Requested: {quantity}."
        all_stock[item_code] -= quantity
        return f"Order successful! {quantity} {menu_dicts[item_code]['name']} ordered."
    else:
        return "Drinks have no stock limitation."
