

class Car:
    def __init__(self, make_temp: str, top_speed_temp: int):
        self.make = make_temp
        self.top_speed = top_speed_temp

    def __str__(self):
        return str(self.top_speed)

def fastest_car(cars_list: list):
    the_fastest_car = Car("fake", 0)
    for car in cars_list:
        if car.top_speed > the_fastest_car.top_speed:
            the_fastest_car = car
    return the_fastest_car









if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))