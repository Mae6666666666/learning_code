

def logging_required_fields():
    user_info = []
    while True:
        email = input("Enter your email: ")
        # card_number = input("Enter your card number: ")
        if email[-3] == "com":
            print("Valid email entered!")
            user_info.append(email)

            break
        else:
            print("Invalid email entered, please try again")


    name = input("Enter your name: ")
    if len(name) <= 3:
        print("Invalid name entered")
    else:
        print("Name added!")
        user_info.append(name)
    age = input("Enter your age: ")
    if len(age) == 0:
        print("Invalid age entered")
    else:
        user_info.append(age)

    if len(user_info) <= 2:
        print("Please add more than 2 fields")
        give_phone_num = input("Enter your phone number: ")
        if len(give_phone_num) < 10:
            print("Invalid phone number entered")
        else:
            user_info.append(give_phone_num)
            print("Thank you!")
            with open("user_info.txt", "w") as file:
                file.write(user_info)


# to get whole number you do isdecimal()
# for whole number u do isnumberical()
def is_something():
    str1 = "362436"  # decimal characters
    str2 = "3"  # unicode digit
    str3 = "½¼"  # fractional value

    print("str1 :")
    print("str1.isdecimal () : ", str1.isdecimal())
    print("str1.isnumeric () : ", str1.isnumeric())
    print("str1.isdigit () : ", str1.isdigit())

    print("str2 :")
    print("str2.isdecimal () : ", str2.isdecimal())
    print("str2.isnumeric () : ", str2.isnumeric())
    print("str2.isdigit () : ", str2.isdigit())

    print("str3 :")
    print("str3.isdecimal () : ", str3.isdecimal())
    print("str3.isnumeric () : ", str3.isnumeric())
    print("str3.isdigit () : ", str3.isdigit())

give_num_decimal = input("Enter your number: ")
give_num_numeric = input("Enter your number: ")
give_num_digit = input("Enter your number: ")
# this accepts whole numbers
# don't take floats
if give_num_decimal.isdecimal():
    print (True)
else:
    print("Invalid input!!")
# this will not except a whole number like 22
# don't take floats
if give_num_digit.isdigit():
    print (True)
else:
    print("Invalid input!!")
#     this won't accept floats
if give_num_digit.isdecimal():
    print (True)
else:
    print("Invalid input!!")


