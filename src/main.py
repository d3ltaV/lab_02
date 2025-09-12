from restaurant import Restaurant

from utils import loadData, createRestaurant, showUserChoices
def main():
    print("Welcome to this restaurant manager program!")
    path = 'data/restaurant_data.json'
    info = loadData(path)
    restaurant = createRestaurant(info)
    print("We created an object of your restaurant.")
    do = input("Do you want to work on the restaurant? (yes/no): ")
    if (do):
        while True:
            print("Choose an option from the following: ")
            showUserChoices(restaurant, path)
            x = input("Do you want to do something else (yes/no): ")
            if (x.lower() == "no"):
                break
    else:
        print("See you next time!")
main()

