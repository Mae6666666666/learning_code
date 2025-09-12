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
    print(bands.loc[bands["band_id"] == "B0001", "name"])
    # you use .loc to locate to the file it's attached to, then add the file nme in the square
    # then the name of what u want and then == to show it is equals to a certain key, so B0001 is
    # equals to Gorillaz in the file, and then we do the name
    # bit because that's what the band name it is stored in is called
    # print(myvar.loc[myvar["cars"] == "cars"])
using_pandas()
