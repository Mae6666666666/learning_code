import pandas as pd

student_data = pd.read_csv("student_test_scores.csv")
electric_vehicles_data = pd.read_csv("electric_vehicles.csv")
def examples_of_pandas():
    # .head will hold the first five values in the file it is given, in this case a csv. this is a pandas function
    # (five values is default for them unless u put a number in those brackets)
    print(student_data.head())
    # tail will hold the last five items in the csv file in pandas (
    # five values is default for them unless u put a number in those brackets)
    print(student_data.tail())

    # this will print out the row called Maths and print out the mean of that column using .mean() if you didnt use .mean(),
    # then it would just display the whole row of maths
    print(student_data["Maths"].mean())

def see_who_passed():
    # this will hold peoples student_data in a passed variable if the column english score is higher or equals to 80,
    # if not, it's not added
    passed = student_data[student_data["English"] >= 80]
    print(passed)


def average_for_all_subjects():

    print(f"Average for English: {student_data["English"].mean()}")
    print(f"Average for Maths: {student_data["Maths"].mean()}")
    print(f"Average for IT: {student_data["IT"].mean()}")
    print(f"Average for science: {student_data["Science"].mean()}")
    print(f"Highest score for English: {student_data['English'].max()}")
    print(f"Highest score for Maths: {student_data['Maths'].max()}")
    print(f"Highest score for IT: {student_data['IT'].max()}")
    print(f"Highest score for Science: {student_data['Science'].max()}")


def user_input():
    give_a_number = int(input("Enter a number from 1 to 100: "))
    what_subject = input("Enter a subject name: ")
    while True:
        if what_subject == "science":
            print(f"Scores lower than {give_a_number} in {what_subject}: {student_data['Science'] < give_a_number}")
            break
        elif what_subject == "english":
            print(f"Scores lower than {give_a_number} in {what_subject}: {student_data['English'] < give_a_number}")
            break
        elif what_subject == "IT":
            print(f"Scores lower than {give_a_number} in {what_subject}: {student_data['IT'] < give_a_number}")
            break
        elif what_subject == "maths":
            print(f"Scores lower than {give_a_number} in {what_subject}: {student_data['Maths'] < give_a_number}")
            break
        else:
            print(f"Invalid input for {what_subject} or {give_a_number}")


def tinkering_with_electric_vehicles():
    for thing in electric_vehicles_data["brand"]:
        if thing == "Ford":
            print(thing)
tinkering_with_electric_vehicles()