from typing import List
class MenuItem:
    """
    A menu item defined by its id, name/category, and list of items

    Attributes:
        id (int): id of the category
        name (string): name of the item
        price (float): price of item
        description (string): description of item
        ingredients (list): list of ingredients of the item
    
    Methods:
        dict(), describemenu()
    """
    def __init__(self, id: int, name: str, price: float, description: str, ingredients: list[str]):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.ingredients = ingredients
        
    def dict(self):
        """
        Makes a dictionary of this item
        Parameters: None
        Returns: dictionary of the item
        """
        return {
            "id":self.id, 
            "name":self.name, 
            "price":self.price, 
            "description":self.description, 
            "ingredients":self.ingredients
        }
    
    def describemenu(self):
        """
        Describe this item
        Parameters: None
        Returns: None
        """
        print("Menu Item: " + self.name
            + "\nPrice: $" + str(self.price)
            + "\nDescription: " + self.description
            + "\nIngredients: " + ", ".join(self.ingredients))