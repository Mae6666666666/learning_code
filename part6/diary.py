# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.
#
# NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.
#
# The program should work as follows:

# print instructions 1 - add an entry, 2 - read entries, 0 - quit
# add input called function that takes whatever the user types. 1 2 or 0
# if option:
#     1. then do add an entry
#           a. entry1 = "Today I ate porridge"
#           b. then do the adding the file bit like: with open(file_name, "w") as new_file:
#           c. then do file_name.write(entry1)
#     2. then print out what's currently in the file:
#           a. print out print("Entry:")
#           b. open file before you can print whats in it. use the with open(file_name) as new_file function
#           a. print(file_name)
#     0. then end code:
#           a. print("bye!)
#           b. break

def diary_entry():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        user_input = int(input("Function:"))
        if user_input == 1:
            entry = "Today i ate porridge"
            with open("diary.txt", "w") as new_file:
                new_file.write(entry)
                print(f"Diary entry: {entry}")
                print("Diary saved")
        elif user_input == 2:
            print("Entry:")
            with open("diary.txt") as new_file:
                print(new_file.read())
        else:
            print("Bye!")
            break

diary_entry()