import data
import functions


def show_main_menu():
    functions.display_menu(data.menu_dicts)
    
    print("Elliot's diner") 
    print("__________")
    print('U to UPDATE a menu item')
    print('T to TAKE a customer order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_choice_menu = input("Your choice: ")
    if user_choice_menu in "Uu":
        print("C to change item description or price")
        print("A to add a new menu items")
        print("R to remove an item from the menu")
        # update_choice = input("Your choice")
        # if update_choice in "Cc":


show_main_menu()

# functions.display_menu(data.menu_dicts)