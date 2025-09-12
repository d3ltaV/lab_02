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

def showUserChoices(res: Restaurant):
    print("1. View Menu")
    print("2. View Category")
    print("3. Add Menu Item")
    print("4. Remove Menu Item")
    print("5. Update Menu Item")
    print("6. Adjust Restaurant Info")
    print("7. Search Menu Item")
    print("8. Save and Exit")
    choice = input("Please select an option: ")
    if choice == '1':
        viewRestaurant(res)
    elif choice == '2':
        viewCategory(res)
    elif choice == '3':
        addItem(res)
    elif choice == '4':
        deleteItem(res)
    elif choice == '5':
        updateItem(res)
    elif choice == '6':
        editRestaurant(res)
    elif choice == '7':
        searchItem(res)
    elif choice == '8':
        updateFile()
        print("Updates have been saved. Exiting...")
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

def searchItem():
    s = input("What item do you want to search? Plesae enter the exact name to learn more about it.")

    return

def editRestaurant(restaurant: Restaurant):
    while True:
        print("1. Edit Name")
        print("2. Edit Location")
        print("3. Edit Cuisine")
        print("4. Edit Hours")
        print("5. Edit Delivery Option")
        choice = input("Please select an option: ")
        if choice == '1':
            n = input("Enter new name: ")
            restaurant.name = n
            print("Name updated.")
            break
        elif choice == '2':
            l = input("Enter new location: ")
            restaurant.location = l
            print("Location updated.")
            break
        elif choice == '3':
            c = input("Enter new cuisine: ")
            restaurant.cuisine = c
            print("Cuisine updated.")
            break
        elif choice == '4':
            t = input("Enter new hours: ")
            restaurant.time = t
            print("Hours updated.")
            break
        elif choice == '5':
            d = input("Does the restaurant do delivery? (yes/no): ")
            if d.lower() == 'yes':
                restaurant.delivery = True
                print("Delivery option updated to 'yes'.")
                break
            elif d.lower() == 'no':
                restaurant.delivery = False
                print("Delivery option updated to 'no'.")
                break
            else:
                print("Invalid input.")
                return
        else:
            print("Invalid choice. Please try again.")
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

#debug
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

def updateItem(restaurant: Restaurant):
    print("Which item would you like to update?")
    x=input("Enter item name to update: ")
    for i in restaurant.menu:
        for j in i.items:
            if j.name == x:
                print("1. Update Name")
                print("2. Update Price")
                print("3. Update Description")
                print("4. Update Ingredients")
                choice = input("Please select an option: ")
                if choice == '1':
                    n = input("Enter new name: ")
                    j.name = n
                    print("Name updated.")
                    return
                elif choice == '2':
                    p = input("Enter new price: ")
                    j.price = p
                    print("Price updated.")
                    return
                elif choice == '3':
                    d = input("Enter new description: ")
                    j.description = d
                    print("Description updated.")
                    return
                elif choice == '4':
                    ing = input("Please list the ingredients of the item, separated by commas: ")
                    ing_list = ing.split(",")
                    j.ingredients = ing_list
                    print("Ingredients updated.")
                    return
                else:
                    print("Invalid choice. Please try again.")
                    return
            else:
                print(f"Item {x} not found.")   
    return
def updateFile(path, restaurant: Restaurant):
    with open(path, 'w') as f:
        json.dump(restaurant.dict(), f)