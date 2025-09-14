from category import Category
class Restaurant:
    """
    A restaurant defined by its name, location, cuisine, and menu

    Attributes:
        name (string): name of the restaurant
        location (string): restaurant address
        cuisine (string): type of cuisine of the restaurant
        menu (list): list of menu categories, with each category having a list of items
    
    Methods:
        describe(), dict(), addItem(), deleteItem()
    """
    def __init__(self, name: str, location: str, cuisine: str, time: str, delivery: bool, menu: list[Category]):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.time = time
        self.delivery = delivery
        self.menu = menu

    def describe(self):
        """
        Describe this restaurant
        Parameters: None
        Returns: None
        """
        print()
        print("-----------------------------------------------------------------------------------")
        print()
        print(f"Welcome to restaurant {self.name}!")
        print(f"We are located at the location: {self.location}, and we serve {self.cuisine} food!")
        print(f"We are open at {self.time}!")
        if (self.delivery):
            print("We do delivery!")
        else:
            print("We do not do delivery")
        print()
        print("MENU")
        print("Here is what we serve: ")
        for i in range(len(self.menu)):
            self.menu[i].describe()
        print()
        print("-----------------------------------------------------------------------------------")
            
    def dict(self):
        """
        Makes a dictionary of this restaurant
        Parameters: None
        Returns: dictionary of the restaurant
        """
        return {
            "name": self.name,
            "location": self.location,
            "cuisine": self.cuisine,
            "time": self.time,
            "delivery": self.delivery,
            "menu": [cat.dict() for cat in self.menu]
        }
    
    def addItem(self, category: Category, index: int):
        """
        Adds category to restaurant
        Parameters: 
            category (Category): category to add
            index (int): index to add to
        Returns: Success message (string)
        """
        self.menu.insert(index, category)
        ret_msg = f"Added category {category.category} at index {index}!"
        return ret_msg

    def deleteItem(self, cat: Category):
        """
        Deletes category in restaurant
        Parameters: 
            cat (Category): category to delete
        Returns: Success message (string) or error message (string)
        """
        if cat in self.menu:
            self.menu.remove(cat)
            ret_msg = f"Removed category: {cat.category}"
            return ret_msg
    
        ret_msg = f"Category {cat} not found!"
        return ret_msg