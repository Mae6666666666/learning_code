

class Person:
    def __init__(self, name: str):
        self.name = name
    def return_first_name(self):
        return self.name.split()[0]

    def return_last_name(self):
        return self.name.split()[1]


peter = Person("Peter Pythons")
print(peter.return_first_name())
print(peter.return_last_name())


paula = Person("Paula Pythonnen")
print(paula.return_first_name())
print(paula.return_last_name())

#
# age_original = 56
#
# def change(age: int):
#     print(age)
#     print("changing age")
#     age = age + 1
#     print(age)
#
# # change(age_original)
# # print(age_original)
#
# class Thing:
#     def __init__(self, age: int):
#         self.age = age
#
# def changeClass(thing: Thing):
#     print(thing.age)
#     thing.age += 1
#     print(thing.age)
#
# age_class_orignal = Thing(56)
# changeClass(age_class_orignal)
#
# print(age_class_orignal)
