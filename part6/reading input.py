# Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.
#
# An example of the function in action:

# first make a define function to hold the code in
# then ask user for a number between 5 and 10
# use an if statement that says if boundary is equals or higher than 5 and equals or lower than ten
# if true is the case, print out, you've typed the number {number}
# else, print You must type in an integer between 5 and 10
# wrap in a for loop
# once the input follows the rules, break

def read_input():
    while True:
        user_number = int(input("Please give a number:"))
        if user_number >= 5 and user_number <= 10:
            print(f"Your number is {user_number}")
            break
        else:
            print("You must type in an integer between 5 and 10")
