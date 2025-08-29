def example_func():
    with open("../other/example.txt") as new_file:
        count = 0
        total_length = 0

        for line in new_file:
            line = line.replace("\n", "")
            count += 1
            print("Line", count, line)
            length = len(line)
            total_length += length

    print("Total length of lines:", total_length)


# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:
#
# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...
# Please write a function named largest, which reads the file and returns the largest number in the file.
#
# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.
#
# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions following this exercise.
#

def largest():
    my_list = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            converting = int(line)
            my_list.append(converting)
    return max(my_list)

# get_data_from_largest = largest()
# print(get_data_from_largest)

def example2():
    with open("grades.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")

            name = parts[0]
            grades = parts[1:]
            print("Name:", name)
            print("Grades:", grades)


# my_dictonary = {}
#
# my_dictonary["car"] = "ford"
# my_dictonary["wheels"] = 4
# my_dictonary["names"] = ["old girl", "megatron", "galbatron"]
#
# print(my_dictonary["wheels"])
# print(my_dictonary["names"][0])

# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:
#
# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...
# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.
#
# NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
#

my_dic = {}
def read_fruits():
    with open("fruits.csv") as new_file:
        for fruit in new_file:
            parts = fruit.replace("\n", "")
            # print(parts)
            parts = parts.split(";")
            # print(parts)
            # print(parts[1])
            floats = float(parts[1])

            fruit_key = parts[0]

            my_dic[fruit_key] = floats
            print(my_dic)



# The file matrix.txt contains a matrix in the format specified in the example below:
#
# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
#
# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as
#
# 1,2,3
# 2,3,4
# the function should return the list [6, 9].
#
# Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. The file you are working with is always named matrix.txt.
#
# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions before this exercise.

def matrix_sum():
    total = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            gapless = line.replace("\n", "")
            parts = gapless.split(",")
            for string_num in parts:
                converting = int(string_num)
                total += converting

        return(total)

# print(matrix_sum())

def matrix_max(file_name:str):
    my_list = []
    with open(file_name) as new_file:
        for line in new_file:
            no_gap = line.replace("\n", "")
            parts = no_gap.split(",")
            for string_num in parts:
                converting = int(string_num)
                my_list.append(converting)
        print(my_list)
        return max(my_list)

 # print(matrix_max("matrix.txt"))


# This program works with two CSV files. One of them contains information about some students on a course:
#
# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder
# The other contains the number of exercises each student has completed each week:
#
# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
# As you can see above, both CSV files also have a header row, which tells you what each column contains.
#
# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:
#
# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35
# Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at the prompt. You might want to hard-code the user input, like so:
#
# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
# The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be executed.
#
# Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with True:
#
#
# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
# When you have verified your program works correctly, you can remove the if structure, keeping the commands asking for input.
#
# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
#
# NB2: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

#How to figure out how far i am and what to do:
# handle file 1:
#Maes interpretation of the question: we ask the user for the info (students1.csv) and the exercise
# and then print out the name first and last in it as well as totaling the amount of exercises in it.
# we don't want to show the student id.
# question plan:
# load students file first, worry about other file later
# make a for loop so the code runs through the lines
# replace line breaks with the replace function and set it to ""
# (the split function will always make the variable stored in a list)
# use the split function with the separator (which is the ("x") thing) and set that to a variable
# create other variables to make the components in the current list clear. like setting the first
# component of parts as zero and using the variable 'key' to make it more clear when we turn it into a dictionary.
# we put those new variables like key into a dictionary, like dictionary_name[key] = {whatever you need to put in it}

# handle file 2:
# we first load the file called exercise1.csv so we can use it and set it is 'new_file'☑️
# we do a for loop for the amount of lines in the new file☑️
# get rid of line breaks and store that in a variable like the file 1 did.☑️
# where there are ; forexample, we use split to remove the ; and replace it with a
# comma to make it neater and into a list.☑️
# now we have the list that will be stored in a variable, we add different names for variables so we can use the in
# a dictionary properly. for example, we use parts[0] and set it to the variable named key because it
# is going to be the key for our dictionary. we do this with the values(s) too☑️
# then we put the newly made variables into the dictionary. for example: my_dic[key] = {value}☑️

# plan for part 3 list thinf:☑️☑️
# create file for it☑️
# load the file so can use☑️
# for loop to run thru lines☑️
# get rid of line breaks☑️
# get rid of ; to make it into a list with split☑️
# store it in the dictioary☑️
# convert str numbers to int and store them☑️
# compare the scores to the list given in question with grades. e.g
# eg 10 of the exercise is done, add one point with the scores etc☑️
# later print out the total gradestudent gets, get rid of the grade originally there next to the name first and last☑️


# exec_nbr is total of all exercises on one line together
# exec_pts is the number of questions
# exm_pts is the total gained on the exam questions
# total is the total number of exec_pts and exm_pts
# grade is the boundary that total number is in.
# i will write a plan and try to impliment it

# i need to create file for it
# load file
# get rid of lines breaks
# get rid of ; to turn into a list
# make the colum 30 characters for the name and 10 characters wide
# use f strings to make the columns wider and taller
# use if statements to determine the grade of the students


def student_info():
    my_student_db = {}
    if False: #Feature flag
        # this is never executed
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")

    else:
        # hard-coded input
        student_info = "students1.csv"
        exercise_data = "exercise1.csv"
        exam_data = "exam_points1.csv"


    with open(student_info) as new_file:
        for line in new_file:
            no_gap = line.replace("\n", "")
            parts = no_gap.split(";")
            key = parts[0]
            first_name = parts[1]
            second_name = parts[2]
            my_student_db[key] = {"first": first_name, "second": second_name}

    with open(exercise_data) as new_file:
        for line in new_file:
            no_gap = line.replace("\n", "")
            parts = no_gap.split(";")
            key = parts[0]
            number_list = parts[1:]
            my_number_list = []
            for str_num in number_list:
                num = int(str_num)
                my_number_list.append(num)
            my_student_db[key]["grades"] = my_number_list

    with open(exam_data) as new_file:
        for line in new_file:
            no_gap = line.replace("\n", "")
            parts = no_gap.split(";")
            key = parts[0]
            number_list = parts[1:]
            my_numbers = []
            for num in number_list:
                numbers = int(num)
                my_numbers.append(numbers)

            my_student_db[key]["score"] = my_numbers

    for key in my_student_db:
        a_student = my_student_db[key]
        # print (a_student["grades"])
        sum_of_nums = sum(a_student["grades"])
        exam_grade = sum(a_student["score"])
        pass_grade = 0

        if exam_grade <= 14:
            pass_grade = 0
        elif exam_grade >= 15 and exam_grade <= 17:
            pass_grade = 1
        elif exam_grade >= 18 and exam_grade <= 20:
            pass_grade = 2
        elif exam_grade >= 21 and exam_grade <= 23:
            pass_grade = 3
        elif exam_grade >= 24 and exam_grade <= 27:
            pass_grade = 4
        elif exam_grade >= 28:
            pass_grade = 5
        print(f"key: {key}" ,my_student_db[key]["first"], my_student_db[key]["second"], pass_grade)

# student_info()


















            # print(parts[0]) #use this as the key
            # print( my_student_db[parts[0]]) #use this as the object to store the total of the grats
            # print(parts[1:]) #use this to get just the grase without the id
            # calculating = int(parts)
            # print(calculating)
            # my_student_db[parts[0]] = {}


student_info()
# {"key":"value"}
# my_dic = {}
# my_dic["09438573409"] = {"first": "mojo", "second": "jojo"}
# my_dic["09438573410"] = {"first": "pink", "second": "mcFace"}
#
# print(my_dic["09438573410"]["first"])
#12345678;4;1;1;4;5;2;4
all_student_db = {'12345678':  {'first': 'peter', 'second': 'pythons', "grades":[4,1,1,4,5,2,4]},
                  '12345687':  {'first': 'jean', 'second': 'javanese'},
                  '12345699':  {'first': 'alice', 'second': 'adder'}}





all_student_db["12345687"] = {'first': 'jean', 'third': 'mcflyface', 'second': 'javanese'}
all_student_db["12345678"]["grades"] = [4,1,1,4,5,2,4]

#this is the ideal way to add a value to a dic
all_student_db["12345687"]["third"] = "mcflyface"
# print(all_student_db["12345687"]["third"])
# print(all_student_db["12345699"]["second"])
