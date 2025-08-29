# exec_nbr is total of points earned in all exercises
# exec_pts is the total number of exercises theyve done
# exm_pts is the total amount of exams they took
# total is the total number of exec_pts and exm_pts
# grade is the boundary that total number is in.
# i will write a plan and try to impliment it

# scores == amount of exams they took
# grades file is used in the first and second column exec_nbr exec_pts
# score (exam_points1) is used in the third and fourth column exm_pts total
# the grade in the column is simply finding what the total column is and giving it the score in the grade boundary

# loop thru my studentdb ☑️
# make variable called full_name and add first and second of the names. make it a string ☑️
# add numbers together in grades. put them in a variable to show the exec_nbr should be 21 27 and 35  ☑️
# find len of grades. put them in a variable to show exec_pts  ☑️
# add together score and put it in a variable to get exm_pts ☑️
# tally together exec_pts and exm_pts and put them in a total variable  ☑️
# compare the total variable number to the grade boundaries in the question and give a score using if statements

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

        my_student_db[key]["final grade"] = pass_grade
    full_name = ""
    for key in my_student_db:
        full_name = my_student_db[key]["first"] + " " + my_student_db[key]["second"]
        exec_nbr = sum(my_student_db[key]["grades"])
        exec_pts = len(my_student_db[key]["grades"])
        exm_pts = sum(my_student_db[key]["score"])
        total = exec_pts + exm_pts
        final_grade = my_student_db[key]["final grade"]
        print(full_name, exec_nbr, exec_pts, total, final_grade)







        # print(my_student_db[key]["first"], my_student_db[key]["second"], pass_grade)
    print(my_student_db)
    my_student_db["12345678"]["final grade"] = 3

student_info()
