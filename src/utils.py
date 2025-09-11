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
    print("1. View Menu")
    print("2. Add Menu Item")
    print("3. Remove Menu Item")
    print("4. Update Menu Item")
    print("5. Adjust Restaurant Info")
    print("6. Search Menu Item")
    print("7. Save and Exit")
    choice = input("Please select an option: ")
    if choice == '1':
        viewRestaurant()
    elif choice == '2':
        addItem()
    elif choice == '3':
        deleteItem()
    elif choice == '4':
        updateFile()
    elif choice == '5':
        editRestaurant()
    elif choice == '6':
        searchItem()
    elif choice == '7':
        print("Updates have been saved. Exiting...")
        exit()
    else:   
        print("Invalid choice. Please try again.")
    return

def viewRestaurant(restaurant: Restaurant):
    restaurant.describe()
    return

def viewCategory(restaurant: Restaurant):
    x=input("Enter category name: ")
    for i in restaurant.menu:
        if i.category == x:
            i.category.describe()
    return

def editRestaurant():
    return

def addItem(restaurant: Restaurant):
    y=input("Which menu would you like to add?: ")
    p=input("What is the price of the item?: ")
    d=input("Please give a description of the item: ")
    ing=input("Please list the ingredients of the item, separated by commas: ")
    ing_list = ing.split(",")
    new_item = MenuItem(0, y, p, d, ing_list)
    cat = input("At which category would you like to add it?(appetizer, main, dessert): ")
    valid = True    
    while (valid):
        ind= int(input("At which index would you like to add it?: "))
        if (ind < 0 or ind > len(restaurant.menu)):
            print("Invalid index. Please try again.")
        else: break
    for c in restaurant.menu:
        if c.category == cat:
            c.addItem(new_item, ind)
    return

def deleteItem():
    x=input("Enter item name to delete: ")
    for i in Restaurant.menu:
        for j in i.items:
            if j.name == x:
                i.deleteItem(j)
                print(f"Item {x} has been deleted.")
                return
            else:
                print(f"Item {x} not found.")
    return

def updateFile():
    return

def searchItem():
    return

def searchCategory():
    return

def exit():
    return