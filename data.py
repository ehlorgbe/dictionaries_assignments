menu_items = [
    'D1 ​​SODA 3',
    'D2 ​​LEMONADE 3',
    'D3 ​​TEA 2',
    'D4 WATER 0',
    'A1 ​​POTATO_CAKES 7',
    'A2 ​​SPINACH_DIP 5',
    'A3 ​​OYSTERS 13',
    'A4 ​​CHEESE_FRIES 4',
    'A5 ​​ONION_RINGS 7',
    'S1 ​​COBB 14',
    'S2 ​​CAESAR 13',
    'S3 ​​GREEK 12',
    'E1 ​​BURGER 16',
    'E2 ​​PASTA 15',
    'E3 ​​GNOCCHI 14',
    'E4 ​​GRILLED_STEAK_SANDWICH 17',
    'T1 ​​CARAMEL_CHEESECAKE 13',
    'T2 ​​APPLE_COBBLER 12',
    'T3 ​​BROWNIE_SUNDAE 9',
    'T4 ​​FLAN 8'
]


drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items =['T1', 'T2',  'T3', 'T4']

# creating random stock numbers in the range 25 to 50 for all items except drinks
import functions
appetizer_stock = functions.stock_level(appetizer_items)
salad_stock = functions.stock_level(salad_items)
entree_stock = functions.stock_level(entree_items)
dessert_stock = functions.stock_level(dessert_items)




# Convert list to list of dictionaries
menu_dicts = {}
for item in menu_items:
    item_parts = item.split()
    item_dict = {
        item_parts[0]:[item_parts[1].replace('​​', ''),int(item_parts[2])]
    }
    menu_dicts.update(item_dict)

# Print the resulting list of dictionaries
# print(menu_dicts)
