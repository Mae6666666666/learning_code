# give_a_number = int(input("Please gave a number: "))

# if give_a_number < 7:
#     print("Sad")
# elif give_a_number == 7:
#     print("Happy")
# elif give_a_number < 7:
#     print("Ehhhh")

# match give_a_number:
#     case 7:
#         print("Happy")
#     case give_a_number if give_a_number < 7:
#         print("Sad")
#     case give_a_number if give_a_number > 7:
#         print("Ehhhh")
    # you did it without help!!!!

# remember, if you wanna remove a range from a list when printing like printing in between set number sets,
# its like [x:y]
#
# lists = ["apple", "orange", "watermelon"]
#
# lists.insert(2, "mango")
# # this will let you put in stuff to a list in specific positions instead of using .append
#
# print(lists)

my_list = ["1", 2, 3, 4.5, 6, 7, 8, 9, 10]
print(f"My list in full: {my_list}")
print(f"My list with first value: {my_list[0]}")

my_list.append(len("Hello"))
print(f"Appended word: {my_list}")

my_list.remove(my_list[0])
print(f"My list removing first value: {my_list}")

# NOT FINISHED!!!
empty_user_list = []
user_input = int(input("Please give a number: "))
add_or_delete = input("Add(a) or delete(d)? or clear(c): ")

if add_or_delete == "a":
    empty_user_list.append(user_input)
elif add_or_delete == "d":
    what_place_to_delete = int(input("What place should be deleted?: "))
    if what_place_to_delete <= len(empty_user_list):
        empty_user_list.remove(empty_user_list[what_place_to_delete])


#How to use numpy (It basically just allows a list to become an array because arrays
# can only be the same data type together like a string, but a list can have multiple data
# types in one list.)
import numpy as np
# [0, :] as printing a list will print everything from placement 0 onwards
# [:, 0] as printing a list will print
# [:] as printing will just print everything im pretty sure cuz : means everything in this context.







