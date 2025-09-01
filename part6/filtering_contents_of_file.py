# The file solutions.csv contains some solutions to mathematics problems:
#
# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.
#
# Please write a function named filter_solutions() which
#
# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines
#
# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.
#
# Please write the lines in the same order as they appear in the original file. Do not change the original file.
#
# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once
#
# filter_solutions()
# or multiple times in a row
#
# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()
# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.

# write a function named filter_solutions
# use a for loop to go thru the lines in the file
# load solutions file in
# read solutions file in
# get rid of line breaks
# use split to get rid of the ; and make it a list
# use if statements to check if each addition and subtraction is correct
# if correct, add to correct.csv
# if incorrect, add to incorrect.csv
# call the function to make it work



def math_add_sub(first_number:int, math_symbol:str, second_number):
    if math_symbol == "-":
        total = first_number - second_number
    else:
        total = first_number + second_number
    return total
# result = math(3, "-", 2)
# print(result) #should return the result

def filter_solutions():
    incorrect = []
    correct = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            no_gap = line.replace("\n", "")
            parts = no_gap.split(";")
            math_question1 = list(parts[1])
            converting_to_int1 = int(math_question1[0])
            converting_to_int2 = int(math_question1[2])
            # print(converting_to_int1, converting_to_int2)
            result = math_add_sub(converting_to_int1, math_question1[1], converting_to_int2)
            their_answer_int = int(parts[2])
            # print(f"all parts {parts}")
            # print(f"Their answer {parts[2]}")
            # print(f"Real answer {result}")
            if their_answer_int == result:
                # print("Right")
                correct.append(no_gap)
            else:
                # print("Wrong")
                incorrect.append(no_gap)

            # print(incorrect)
            # print(correct)
    with open("correct.csv", "w") as correct_file:
        for characters in correct:
            correct_file.write(characters)
            print(characters)
    with open("incorrect.csv", "w") as incorrect_file:
        for characters in incorrect:
            incorrect_file.write(characters)
            print(characters)

    print(f"Correct {correct_file}")
    print(f"Incorrect {incorrect_file}")







            # print(parts[2])
            # print(result) #should return the result
filter_solutions()


# filter_solutions()


