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
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(e)

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

def updateFile():
    return

def searchItem():
    return

def searchCategory():
    return