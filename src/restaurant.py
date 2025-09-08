from category import Category
from typing import List
class Restaurant:
    """
    A restaurant defined by its name, location, cuisine, and menu

    Attributes:
        name (string): name of the restaurant
        location (string): restaurant address
        cuisine (string): type of cuisine of the restaurant
        menu (list): list of menu categories, with each category having a list of items
    
    Methods:
        describe(), viewCategories(), addItem(), deleteItem()
    """
    def __init__(self, name: str, location: str, cuisine: str, menu: List[Category]):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.menu = menu
    
    def describe():
        print()
