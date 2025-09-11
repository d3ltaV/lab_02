from restaurant import Restaurant

from utils import loadData, createRestaurant
def main():
    path = 'data/restaurant_data.json'
    info = loadData(path)
    restaurant = createRestaurant(info)
    # restaurant.describe()

main()