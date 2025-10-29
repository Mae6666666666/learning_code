# sep = "x" is used in print statements with lists. it will add
# whatever is in the quotes between each word in the print list
# e.g

def separating():
    print("hello", "my", "name", "is", "Mae", sep = "-")

# separating()

# for loop
# while true
# if elif, else
# load files
# write to files
# pass values into function e.g separating(oiuwieb)
# use the split function e.g new_file.split(";")
# get rid of line breaks or whatever u want with an empty value e.g new_file.replace("\n", "")



# how to use a class (its literally just to group multiple functions together so they can load at once)
# to do the power of which e.g print(2 ** 3) the ** makes it so its literally 2 to the power of 3
# to find the modulus number on the left e.g print(3 // 4) would give you DON'T LISTEN TO THIS RN

def using_for_loop():
    my_list = [1, 2, 3, 4]
    for number in my_list:
        print(number)
# using_for_loop()

def using_if_statements():
    my_input = int(input("0 or 1?:"))
    if my_input == 0:
        print("0")
    elif my_input == 1:
        print("1")
    else:
        print("no")

def using_while_loop():
    my_list = [1, 2, 3, 4]
    while True:
        print(my_list)
        break
# using_for_loop()
def writing_a_file():
    with open("my_test", "w") as testing:
        uhh = testing.write("hubwhb")
def opening_a_file():
    with open("my_test.csv") as testing:
        testing_uh = testing.split(";")
        testing_uh2 = testing.replace(";", "")
        print("h")  # ignore this line

def splitting():
    sum_str = "jnwdsc; jnqw; ijqwnb"
    splitting_a_file = sum_str.split(";")

def replacing():
    sum_str = "knef, ijwnef, jnwed, iwnec\n"
    replacing_a_file = sum_str.replace("\n", "")

# descrie how to search with pandas
# create a function that does it
# pandas are open source made only by people not python use pip.install

def importing():
    import math
    response = math.sqrt(16)
    print(response)
#A built in python function that allows the user to use all math functions in code

def importing_quicker():
    from math import sqrt
    square_root = sqrt(81)
    print(square_root)
#this located the built-in mmath import and only takes the square root function from it
# so you only need to do sqrt(x) instead of math.sqrt(x)

# pandas are functions you import that are made by random people over the world.
# python did not build in this function or make this either, it was made by random people
# who like wasting their time on code. Which means they get the bigger bucks. you use a .pip install
# function to import the data
# online and bring it to pycharm to use. this can give data like files containing Gorillaz music
# neatly separated by album, release date, name etc

def using_pandas():
    # C:\Users\your project root > pip install pandas
    # install using that
    import pandas as pd
    # mydataset = {
    #     'cars': ["BMW", "Volvo", "Ford"],
    #     'passings': [3, 7, 2]
    # }
    bands = pd.read_csv("db_00/bands.csv")

    # myvar = pandas.DataFrame(mydataset)
    band_name = bands.loc[ # locates whatever is in the square brackets
        bands["band_id"] == "B0001", #search in bands.csv which looks specifically in the column named "band_id" for that band id
        "name" # then in the band id number searcher (B0001), then it looks specifically for the column in that named "name"
         ].values[0] # gets rid of the value in front of whatever you want to search with .values[0]


    print(band_name) # prints the name of whatever has the band id of B0001, like Gorillaz for example
    # you use .loc to locate to the file it's attached to, then add the file nme in the square
    # then the name of what u want and then == to show it is equals to a certain key, so B0001 is
    # equals to Gorillaz in the file, and then we do the name
    # bit because that's what the band name it is stored in is called
    # print(myvar.loc[myvar["cars"] == "cars"])


import random
# this import lets you use a command called randint to randomly call out a
# number that's between the range you give it. like so:
def using_random():
    number_picked = random.randint(1, 1000)
    # this command picks a number between that range and stores it in number_picked
    print(number_picked)
# using_random()

def using_case():
    value = 32
    match value:
        # match will link the variable given to match and basically tell it that it wants to
        # do a case statement
        case n if 0 <= n <= 10:
            # okay so, with the match value thing, it is saying as well that whatever
            # you set the variable to (like n), it means value in this case and holds all of that data
            # you put the if statement so it's like if 0 is less than or equal to n (value) or n (value)
            # is less than or equal to 10 then it does whatever is below it

            print("Between 0 and 10")
        case n if 11 <= n <= 20:
            print("Between 11 and 20")
        case n if 21 <= n <= 50:
            print("Between 21 and 50")
        case _:
            # this just means else. literally. it's like saying if none of the above apply, do this
            print("Out of range")

def using_match_more_simply():
    user_name = "Kim"

    match user_name:
        case "Kim":
            # literally just says if user_name is kim, do the below
            print("Hello Kim!")
        case "Abe":
            print("Hey Abe!")
        case "Mae":
            print("Hi Mae!")
        case _:
            # else statement
            print("Unknown user")

# this lets you select random integers from the random function
from random import randint
def using_randint():
    a_number = random.randint(1, 4)
    print(a_number)


# it gives u x amount of random values. e.g sample(list, amount of values)
from random import sample
def using_sample(amount: int, lower: int, upper: int):
    # we set number pool into a list with the number range of whatever we put in the bottom,
    # like 6 and 20 in this case
    number_pool = list(range(lower, upper))
    # we set weekly draw as a sample which contains whatever numbers we got from number pool and then
    # the amount that we put in basically tells the code, hey, we only want the amount that is put in
    # the bottom (1) to be in this variable
    weekly_draw = sample(number_pool, amount)
    # then we print the sorted version of the list weekly draw to put the numbers in order
    print(sorted(weekly_draw))
    return sorted(weekly_draw)
# using_sample(1, 6, 20)

# this will let u use a function that when called, can calculate seconds,minutes, hours, milliseconds etc
import datetime
def using_datetime():
    # we make a new dictionary
    student_db = {}
    # open a file and name it sum else
    with open("start_times.csv", "r") as start_times:
        # for loop to go thru every element in the file
        for element in start_times:
            # this will get rid of \n bits and replace them with empty strings
            getting_rid_of_semicolon = element.replace("\n", "")
            # this will turn it into a list and take apart the elements where there is a semicolon (;)
            getting_a_space = getting_rid_of_semicolon.split(";")
            # this just gets the first item in the file which would be the name
            student_name = getting_a_space[0]
            # this gets the second item in it which would be the time
            student_times = getting_a_space[1]
            # this just adds start times to the dictionary
            student_db[student_name]["start_time"] = student_times
        #     loops thtu every student in the dictionary
        for student in student_db:
            # sets a variable as the students in the dictionary
            student_times = student_db[student]
            # basically says wherever the key start time is, the data in that now is in start time
            start_time = student_times["start_time"]
            # basically says wherever the key end time is, the data in that now is in end time
            end_time = student_times["end_time"]
            # this will have a variable that uses datetime.datetime.strptime.
            # this basically just says were gonna need to figure out these times. the start time is given and its
            # format is given after (the %H:%M)
            start_datetime = datetime.datetime.strptime(start_time, "%H:%M")
            # this does the exact same as start datetime, but it just gives the end time
            end_datetime = datetime.datetime.strptime(end_time, "%H:%M")
            # then we calculate the amount of hours that are different between the two
            difference = end_datetime - start_datetime
            # we convert that to seconds cuz its easier
            difference_in_seconds = difference.total_seconds()
            # if the difference is more than that number (3 hours) the code tells the student is a dirty cheating skank
            if difference_in_seconds > 10800:
                print(f"{student} is a dirty cheating skank")
            # if not, it just says the student passed (boringgggg)
            else:
                print(f"{student} passed")




def using_find():
    my_str = "hello there"
    position_of_letter:int = my_str.find("z")
    return position_of_letter

# print(using_find())

import pandas as pd
def doing_pandas():
    data = pd.read_csv("db_00/bands.csv")
    print(data)
# using_pandas()

class Dog():
    legs = 4
    xPos = 0
    yPos = 0
    def jump(self):
        self.yPos = self.yPos + 10

    def walk(self, distance:int):
        self.xPos = self.xPos + distance

    def reset(self):
        self.legs = 4
        self.xPos = 0
        self.yPos = 0



def run_and_jump(animal:Dog):
    animal.walk(3)
    animal.jump()
    animal.walk(3)


def add(num1: int, num2: int):
    return num1 + num2

total = add(555, 222)
print(total)