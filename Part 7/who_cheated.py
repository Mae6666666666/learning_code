# load a file which contains name, hour and minute in start_times.csv
# load submissions.csv in the format name, ask, points, hour and minute
# whoever spent more than three hours on this task (so three hours overdue) is classed a cheater
# make the function cheaters and loop thru the file

# make a function called cheater
# load file for both start times and submission
# find the hour and minutes and stick it in the datetime object for start time
# and do a separate datetime function with submission times
# once the times are stored, compare the two. if the hours are more than 3, put them in a cheater variable (their name)
# then print the cheaters out once finished

import datetime
from time import strptime


def cheaters():
    storing_submissions = []
    storing_start_times = []
    student_db = {}

    with open("submissions.csv", "r") as submissions:
        storing_submissions.append(submissions)
        for element in submissions:
            getting_rid_of_semicolon = element.replace("\n", "")
            giving_semicolon_a_space = getting_rid_of_semicolon.split(";")
            student_name = giving_semicolon_a_space[0]
            storing_time = giving_semicolon_a_space[3]

            student_db[student_name] = {}
            student_db[student_name]["end_time"] = storing_time


    with open("start_times.csv", "r") as start_times:
        for element in start_times:
            getting_rid_of_semicolon = element.replace("\n", "")
            getting_a_space = getting_rid_of_semicolon.split(";")
            student_name = getting_a_space[0]
            student_times = getting_a_space[1]
            student_db[student_name]["start_time"] = student_times

        for student in student_db:

            student_times = student_db[student]

            start_time = student_times["start_time"]
            end_time = student_times["end_time"]
            start_datetime = datetime.datetime.strptime(start_time, "%H:%M")
            end_datetime = datetime.datetime.strptime(end_time, "%H:%M")
            difference = end_datetime - start_datetime

            difference_in_seconds = difference.total_seconds()
            if difference_in_seconds > 10800:
                print(f"{student} is a dirty cheating skank")
            else:
                print(f"{student} passed")
cheaters()
