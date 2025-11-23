

class Person:
    def __init__(self, name_temp: str, stone_temp: int, unknown_temp: int, kilograms_temp: int):
        self.name = name_temp
        self.age = stone_temp
        self.unknown = unknown_temp
        self.kilograms = kilograms_temp
        self.amount_of_times_called = 0




class BabyCentre:
    def weigh(self, person: Person):
        person.amount_of_times_called += 1
        person.weight_in_kg = person.kilograms
        return person.weight_in_kg

    def feed(self, person: Person):
        person.kilograms += 1
        return person.kilograms

def weigh_ins():
    return Person.amount_of_times_called






baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")