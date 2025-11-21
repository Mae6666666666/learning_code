

class Car:
    __amount_in_the_tank = 0
    __odometer = 0
    def fill_up(self):
        self.__amount_in_the_tank += 1

    def drive(self, km: int):
        self.__odometer += km

    def __str__(self):
        return f"odometer reading {self.__odometer}km, petrol remaining {self.__amount_in_the_tank} litres"




car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)
