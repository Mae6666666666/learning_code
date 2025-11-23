def take_two_nums(num1: int, num2: int):
    answer_add = num1 + num2
    answer_sub = num1 - num2
    answer_mul = num1 * num2
    answer_div = num1 / num2
    print(f"adding {num1} and {num2} gives {answer_add}")
    print(f"subtracting {num1} and {num2} gives {answer_sub}")
    print(f"timsing {num1} and {num2} gives {answer_mul}")
    print(f"dividing {num1} and {num2} gives {answer_div}")


def user_calculator():
    while True:
        user_number1 = int(input("Give a number: "))
        ser_number2 = int(input("Give another number: "))
        times_divide_etc = input("Add(a), Subtract(s), Times(t) or Divide(d): ").lower()
        if times_divide_etc == "a":
            print(f"{user_number1} + {ser_number2} = {user_number1 + ser_number2}")
            continuing = input("Continue? (y), (n):")
            if continuing == "n":
                print("bye")
                break
        elif times_divide_etc == "s":
            print(f"{user_number1} - {ser_number2} = {user_number1 - ser_number2}")
            continuing = input("Continue? (y), (n):")
            if continuing == "n":
                print("bye")
                break

        elif times_divide_etc == "t":
            print(f"{user_number1} x {ser_number2} = {user_number1 * ser_number2}")
            continuing = input("Continue? (y), (n):")
            if continuing == "n":
                print("bye")
                break

        elif times_divide_etc == "d":
            print(f"{user_number1} / {ser_number2} = {user_number1 / ser_number2}")
            continuing = input("Continue? (y), (n):")
            if continuing == "n":
                print("bye")
                break
user_calculator()