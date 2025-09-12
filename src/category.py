from menuitems import MenuItem
class Category:
    """
    A category defined by its id, name/category, and list of items

    Attributes:
        category (string): name of the category
        id (int): id of the category
        items (list): list of categories items
    
    Methods:
        describe(), dict(), addItem(), deleteItem()
    """
    def __init__(self, id: int, category: str, items: list[MenuItem]):
        self.id = id
        self.category = category
        self.items = items
    def describe(self):
        """
        Describe this category
        Parameters: None
        Returns: None
        """
        print(f"Here is a list of items in category {self.category}!")
        for i in range(len(self.items)):
            self.items[i].describemenu()

    def dict(self):
        """
        Makes a dictionary of this category
        Parameters: None
        Returns: dictionary of the category
        """
        return {
            "id": self.id,
            "category": self.category,
            "items": [item.dict for item in self.items]
        }
    
    def addItem(self, item: MenuItem, index: int):
        """
        Adds item to category
        Parameters: 
            item (MenuItem): item to add
            index (int): index to add to
        Returns: Success message (string)
        """
        self.menu.insert(index, item)
        ret_msg = f"Added category {item.name} at index {index}!"
        return ret_msg

    def deleteItem(self, item: MenuItem):
        """
        Deletes category in restaurant
        Parameters: 
            item (MenuItem): item to delete
        Returns: Success message (string) or error message (string)
        """
        if item in self.items:
            self.menu.remove(item)
            ret_msg = f"Removed category: {item.name}"
            return ret_msg
    
        ret_msg = f"Category {item.name} not found!"
        return ret_msg