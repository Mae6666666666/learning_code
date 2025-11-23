import pandas as pd

from Lessons.week7.main import electric_vehicles_data


def finding_the_users_car():
    data = pd.read_csv("electric_vehicles.csv")
    user_car_brand_input = input("Enter the car brand: ")
    if user_car_brand_input in data:
        print(f"Info: {data[user_car_brand_input] == user_car_brand_input}")

    else:
        print("No brand of this exists in this file")
finding_the_users_car()

