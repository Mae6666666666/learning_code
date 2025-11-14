def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


# cannot divide by zero so program will fail.
def division(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Number cannot be divided by 0")



# menu to re-use calculator
print("=======================================================================")
print("==                          Calculator App                           ==")
print("=======================================================================")
while True:
    operator = int(input("""What operation do you want to perform (enter the respective number)
                         1. addition
                         2. subtraction
                         3. division
                         4. multiplication
                         : """))
    user_num1 = input("enter number 1: ")
    user_num2 = input("enter number 2: ")

    valid_number = False
    if user_num1.isdecimal():
        valid_number = True
        num1 = int(user_num1)
        num2 = int(user_num2)
    else:
        print("incorrect format detected")
    # calling functions for operations
    if operator == 1:
        print(add(num1, num2))
    elif operator == 2:
        print(subtract(num1, num2))
    elif operator == 3:
        print(division(num1, num2))
    elif operator == 4:
        print(division(num1, num2))
    else:
        print("invalid input detected.")

    exiting = "no"
    if exit == "yes":
        print("=======================================================================")
        print("==                      Closing Calculator App                       ==")
        print("=======================================================================")
        break
    else:
        print("new calculation...")


add(1,2)
subtract(1,2)
division(1,0)
multiply(1,2)
