
# user_name will ask for a name to be typed
user_name = input("Please give your name: ")
# print(user_name) will print whatever the user has typed (e.g Mae)
print(user_name)

# the def getting_first_and_second_value holds two arguments and groups everything inside the indent so it can be used all at once
def getting_first_and_second_value(first_value, second_value):
    # first_and_second_times_two adds both first and second value in the def function and times it by two
    first_and_second_times_two = (first_value + second_value) * 2
    # printing will show put first_and_second_times_two
    print(first_and_second_times_two)
# this def getting_third_and_fourth_value groups several actions inside this function to be called all at once later
def getting_third_and_fourth_value():
    # third_value takes the user's third number, which can only be an integer (since it has an int next to it)
    third_value = int(input("Enter value: "))
    # fourth_value takes the fourth value from the user that can also be only an integer
    fourth_value = int(input("Enter second value: "))
    # getting_first_and_second_value(third_value, fourth_value) will call the first def function so everything in it can run
    getting_first_and_second_value(third_value, fourth_value)

# this will call the second def function, which will let the entire program run and work
getting_third_and_fourth_value()



