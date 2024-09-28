import random

def stock_level(food_item):
    """determine random stock levels"""
    dict = {}
    for i in food_item:
        dict.update({i : random.randint(25,50)})
    return dict   


