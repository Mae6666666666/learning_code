# Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments. The first element should be the name and the second the age.
#
# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# first rite a function which takes two arguments
# make a tuple in a tuple for name and age
# call the function

name_and_age = (("Denji", 16), ("Shigaraki", 23), ("Sanji", 19))
def new_person(name_and_age: tuple):
    print(name_and_age)

new_person(name_and_age[0])