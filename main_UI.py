import data
import functions

customer_order = []
def show_main_menu():
    print("Elliot's diner") 
    print("__________")
    print('U to UPDATE a menu item')
    print('T to TAKE a customer order\n')

    user_choice_menu = input("Your choice: ")
    if user_choice_menu in "Uu":
        functions.display_menu(data.menu_dicts)
        print("________\n")
        print("A to add a new menu items")
        print("C to change item name or price")
        print("R to remove an item from the menu\n")
        update_choice = input("Your choice: ")
        if update_choice in "Cc":
            print("leave empty and press Enter to keep existing values ")
            functions.update_item(data.menu_dicts,input("item_code: "),input("new name: "),input("new price: "))
        elif update_choice in "Aa":   #this is contains bugs fix it
            item_code = (input("New item code: ")).upper()
            if item_code[0] not in ["D","A","S","E","T"]:
                print("Invalid item code")
            else:
                functions.add_item(data.menu_dicts,item_code,input("New item name: "),input("price: "))
        elif update_choice in "Rr":
                functions.remove_item(data.menu_dicts,input("item code: "))
        show_main_menu()
    elif user_choice_menu in "Tt":
         print(functions.customer_request(input("item code: "),int(input("Quantiy: "))))
         show_main_menu()
         

            


show_main_menu()

# functions.display_menu(data.menu_dicts)
# print(data.drink_items)