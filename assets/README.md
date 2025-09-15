# Lab\_02: User-Driven Applications with JSON for a Restaurant Management Program

## Program Description
This program, built by Joelle and June, is designed to help restaurants manage their data. The **restaurant's data** is stored in a **.json file**, which contains basic restaurant information, menu categories in the restaurant, and all items in the menu. The program introduces itself and asks the user if they would like to manage their restaurant data. If the response is **'yes'**, eight options are displayed:

    1. View Menu
    2. View Category
    3. Add Menu Item
    4. Remove Menu Item
    5. Update Menu Item
    6. Adjust Restaurant Info
    7. Search Menu Item
    8. Save and Exit

Users can choose what they would like to do by entering a number. **Ensure that changes are saved by entering 8** before responding **'no'** to the 'Would you like to do something else?' prompt. The adding menu item, removing menu item, updating menu item (options 3, 4, 5 respectively), and adjusting restaurant info options (option 6) modify the restaurant object created from the JSON file. To save changes to the file, option 8 must be chosen before exiting.

---

## Folder Structure

```bash
|LAB_02/
|   data/             
|       restaurant_data.json   # JSON file containing menu categories, with each category containing menu items.
|       copy.json              # JSON file that is a copy of restaurant_data.json, if you want to use restaurant.json for testing purposes.
|   src/              
|       main.py               # Main program logic that allows user to handle restaurant data
|       restaurant.py         # Class for restaurant: contains operations (describe, dict, addItem, deleteItem), basic restaurant info, and categories in the restaurant menu
|       category.py           # Class for a category in the menu: contains operations (describe, dict, addItem, deleteItem), category info, and items in that category
|       menuitems.py          # Class for a menuitem: contains operations (describemenu, dict), and item info
|       utils.py              # Helper functions that allow users to choose what to do with their restaurant and handles all operations, such as modifying restaurant information, searching for an item, deleting an item, and saving data to the JSON file.
|   assets/           
|       README.md             # Documentation for the program
|
```

Data is stored in the data/ folder. The src/ handles logic and classes, including the main file, the class files, and the operation (utils) file. The assets/ folder stores documentation.

---

## Deployment
To deploy this program, the only dependency you need is **Python**. Ensure Python is installed, clone the github repository with 'git clone', and run the **main.py** file in LAB_02/src/main.py.

---

## Example of input and output

INPUT:
```text
Welcome to this restaurant manager program!
We created an object of your restaurant.

Do you want to work on the restaurant? (yes/no): yes 
```

OUTPUT:
```text
Choose an option from the following: 
1. View Menu
2. View Category
3. Add Menu Item
4. Remove Menu Item
5. Update Menu Item
6. Adjust Restaurant Info
7. Search Menu Item
8. Save and Exit
```

INPUT:
```text
Please select an option: 1
```
OUTPUT:
```text
-----------------------------------------------------------------------------------

Welcome to restaurant K-Restaurant!
We are located at the location: 1 Lamplighter Way, 01354, and we serve Korean food!
We are open at 11:00 AM - 10:00 PM!
We do delivery!

MENU
Here is what we serve:

-----------------------------------------------------------------------------------

Here is a list of items in category Appetizer!

Menu Item: Japchae
Price: $11.99
Description: Stir-fried glass noodles with vegetables and beef.
Ingredients: glass noodles, vegetables, beef, soy sauce

Menu Item: Tteokbokki
Price: $9.99
Description: Spicy rice cakes cooked in a sweet and spicy sauce.
Ingredients: rice cakes, gochujang, fish cakes, green onions

Menu Item: Pajeon
Price: $6.99
Description: Korean savory pancake with green onions and seafood.
Ingredients: flour, green onions, seafood, egg

Menu Item: Kimbap
Price: $7.99
Description: Rice rolls filled with vegetables and meat, wrapped in seaweed.
Ingredients: rice, seaweed, vegetables, meat

Menu Item: Dumpling
Price: $5.99
Description: Korean dumpling with vegetables and beef broth.
Ingredients: dumplings, vegetables, beef broth, green onions

-----------------------------------------------------------------------------------

Here is a list of items in category Main Course!

Menu Item: Korean Pork Belly
Price: $15.99
Description: Grilled pork belly served with a side of kimchi and rice.
Ingredients: pork belly, kimchi, rice, garlic

Menu Item: Bibimbap
Price: $12.99
Description: A bowl of warm rice topped with vegetables, beef, a fried egg, and gochujang sauce.
Ingredients: rice, vegetables, beef, egg, gochujang

Menu Item: Kimchi Stew
Price: $10.99
Description: A spicy stew made with kimchi, tofu, and pork.
Ingredients: kimchi, tofu, pork, green onions

Menu Item: Bulgogi
Price: $14.99
Description: Marinated beef grilled to perfection, served with rice and vegetables.
Ingredients: beef, soy sauce, sugar, garlic, vegetables

Menu Item: Galbi
Price: $16.99
Description: Korean BBQ short ribs marinated in a sweet and savory sauce.
Ingredients: short ribs, soy sauce, sugar, garlic, pear

Menu Item: Sundubu Jjigae
Price: $13.99
Description: Spicy soft tofu stew with seafood and vegetables.
Ingredients: soft tofu, seafood, vegetables, gochujang

-----------------------------------------------------------------------------------

Here is a list of items in category Dessert!

Menu Item: Mochi Ice Cream
Price: $4.99
Description: Sweet rice cake filled with ice cream.
Ingredients: rice flour, sugar, ice cream

Menu Item: Hotteok
Price: $3.99
Description: Korean sweet pancakes filled with brown sugar and nuts.
Ingredients: flour, brown sugar, nuts, cinnamon

Menu Item: Bingsu
Price: $5.99
Description: Shaved ice dessert topped with sweet red beans, fruit, and condensed milk.
Ingredients: shaved ice, red beans, fruit, condensed milk

-----------------------------------------------------------------------------------
Do you want to do something else (yes/no):
```