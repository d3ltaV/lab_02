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
    """
    Create a restaurant object from the json data
    Parameters
        info (dict): dictionary of the restaurant data
    Returns: Restaurant object
    """
    categories = []
    for cat in info["menu"]:
        it = []
        for i in cat["items"]:
            it.append(MenuItem(id=i["id"], name=i["name"], price=i["price"], description=i["description"], ingredients=i["ingredients"] ))
        categories.append(Category(id=cat["id"], category=cat["category"], items=it))
    res = Restaurant(name=info["restaurant"], location=info["location"], cuisine=info["cuisine"], time=info["time"], delivery=info["delivery"], menu=categories)
    return res

def showUserChoices(res: Restaurant, path: str):
    """
    Show the user the choices they can make
    Parameters:
        res (Restaurant): the restaurant object
    Returns: None
    """
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
        updateFile(path, res)
        print("Updates have been saved. Exiting...")
    else:   
        print("Invalid choice. Please try again.")
        showUserChoices(res, path)
    return

def viewRestaurant(restaurant: Restaurant):
    """
    View the restaurant info
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    restaurant.describe()
    return

def viewCategory(restaurant: Restaurant):
    """
    View a specific category in the restaurant
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    x = input("Enter category name: ")
    for i in restaurant.menu:
        if i.category.lower() == x.lower():
            i.describe()
            return
    print("Category not found!")
    return

def searchItem(restaurant: Restaurant):
    """
    Search for a specific item in the restaurant
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    s = input("What item do you want to search? Plesae enter the exact name to learn more about it: ")
    for cat in restaurant.menu:
        for i in cat.items:
            if (i.name.lower() == s.lower()):
                i.describemenu()
                return
    print("Item not found!")
    return

def editRestaurant(restaurant: Restaurant):
    """
    Edit the restaurant info
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    print("Here are the options for editing the restaurant: ")
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
            print(f"Name updated to {restaurant.name}")
            break
        elif choice == '2':
            l = input("Enter new location: ")
            restaurant.location = l
            print(f"Location updated to {restaurant.location}")
            break
        elif choice == '3':
            c = input("Enter new cuisine: ")
            restaurant.cuisine = c
            print(f"Cuisine updated to {restaurant.cuisine}")
            break
        elif choice == '4':
            t = input("Enter new hours: ")
            restaurant.time = t
            print(f"Hours updated to {restaurant.time}")
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
        else:
            print("Invalid choice. Please try again.")

def addItem(restaurant: Restaurant):
    """
    Add a new item to a category in the restaurant
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    y=input("What is the name of the item you would you like to add?: ")
    while True:
        p=input("What is the price of the item?: ")
        try: 
            p = float(p)
            break
        except ValueError:
            print("Enter a number!")
    d=input("Please give a description of the item: ")
    ing=input("Please list the ingredients of the item, separated by commas: ")
    ing_list = ing.split(",")
    new_item = MenuItem(0, y, p, d, ing_list)
    cat = input("At which category would you like to add it? (appetizer, main, dessert): ") 
    ind= int(input("At which index would you like to add it?: "))

    for c in restaurant.menu:
        if c.category.lower() == cat.lower():
            msg = c.addItem(new_item, ind)
            print(msg)
            return
    print("Category not found!")
    return

def deleteItem(restaurant: Restaurant):
    """
    Delete an item from a category in the restaurant
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    x = input("Enter item name to delete: ")
    for i in restaurant.menu:
        for j in i.items:
            if j.name == x:
                msg = i.deleteItem(j)
                print(msg)
                return
    print(f"Item {x} not found.")
    return

def updateItem(restaurant: Restaurant):
    """
    Update an item in a category in the restaurant
    Parameters:
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    print("Which item would you like to update?")
    x=input("Enter item name to update: ")
    for i in restaurant.menu:
        for j in i.items:
            if j.name.lower() == x.lower():
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
    print(f"Item {x} not found.")   
    return

def updateFile(path, restaurant: Restaurant):
    """
    Update the json file with the current restaurant data
    Parameters:
        path (string): path of the json file
        restaurant (Restaurant): the restaurant object
    Returns: None
    """
    with open(path, 'w') as f:
        json.dump(restaurant.dict(), f)