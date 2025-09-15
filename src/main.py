from restaurant import Restaurant

from utils import loadData, createRestaurant, showUserChoices
def main():
    print("Welcome to this restaurant manager program!")
    path = 'data/restaurant_data.json'
    info = loadData(path)
    restaurant = createRestaurant(info)
    print("We created an object of your restaurant.")
    print()

    while True:
        do = input("Do you want to work on the restaurant? (yes/no): ")
        if (do.lower() == "yes"):
            print()
            while True:
                print("Choose an option from the following: ")
                showUserChoices(restaurant, path)
                x = input("Do you want to do something else (yes/no): ")
                if (x.lower() == "no"):
                    break
                elif (x.lower() != "yes"):
                    print("Invalid choice; please select 1 and try again!")
        elif (do.lower() == "no"):
            print("See you next time!")
            break
        else: 
            print("Invalid choice. Please try again!")

main()

