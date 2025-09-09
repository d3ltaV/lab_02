class MenuItem:
    def __init__(self, id, name, price, description, ingredients):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.ingredients = ingredients
        
    def dict(self):
        return {
            "id":self.id, 
            "name":self.name, 
            "price":self.price, 
            "description":self.description, 
            "ingredients":self.ingredients
        }
    
    def describemenu(self):
        print("Menu Item: " + self.name
              + "\nPrice: $" + str(self.price)
              + "\nDescription: " + self.description
              + "\nIngredients: " + ", ".join(self.ingredients))