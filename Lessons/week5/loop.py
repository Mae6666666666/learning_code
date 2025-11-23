def finding_a_number():
    while True:
        user_input = int(input("Give a number between 10 and 50: "))
        if user_input >= 10 and user_input <= 50:
            print(f"{user_input} is in the range!")
            break
        else:
            print(f"{user_input} is not in the range")
finding_a_number()

