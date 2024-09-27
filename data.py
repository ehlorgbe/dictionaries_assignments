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

# Convert list to list of dictionaries
menu_dicts = {}
for item in menu_items:
    item_parts = item.split()
    item_dict = {
        item_parts[0]:[item_parts[1].replace('​​', ''),int(item_parts[2])]
    }
    menu_dicts.update(item_dict)

# Print the resulting list of dictionaries
print(menu_dicts)
