import json
from restaurant import Restaurant
from menuitems import MenuItem
from category import Category

def loadData(path):
    """
    Load the json data from a json file
    Parameters:
        path (string): path of the json file
    """
    try:
        with open(path, 'r') as f:
            info = json.load(f)
            return info
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(e)

def createRestaurant(info):
    categories = []
    for cat in info["menu"]:
        it = []
        for i in cat["items"]:
            it.append(MenuItem(id=i["id"], name=i["name"], price=i["price"], description=i["description"], ingredients=i["ingredients"] ))
        categories.append(Category(id=cat["id"], category=cat["category"], items=it))
    res = Restaurant(name=info["restaurant"], location=info["location"], cuisine=info["cuisine"], time=info["time"], delivery=info["delivery"], menu=categories)
    return res

def showUserChoices():
    return

def viewRestaurant():
    return

def viewCategory(category: Category):
    return

def viewAll():
    return

def addItem():
    return

def deleteItem():
    return

def updateFile(path, restaurant: Restaurant):
    with open(path, 'w') as f:
        json.dump(restaurant.dict(), f)

def searchItem():
    return

def searchCategory():
    return