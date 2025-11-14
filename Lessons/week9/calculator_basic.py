
class Calculator:
    user_choice = int(input("Enter your choice. add(1), sub(2), times(3), div(4): "))
    if user_choice == 1:
        def add(self):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            print(num1 + num2)
    elif user_choice == 2:
        def sub(self):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            print(num1 - num2)
    elif user_choice == 3:
        def multiply(self):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            print(num1 * num2)
    elif user_choice == 4:
        def divide(self):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            try:
                 print(num1 / num2)
            except ZeroDivisionError:
                print("Will not except division by zero")

calculator = Calculator()
calculator.add()
calculator.sub()
calculator.multiply()
calculator.divide()