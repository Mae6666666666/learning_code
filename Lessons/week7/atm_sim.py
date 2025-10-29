
def making_an_atm():
    balance = open("balance.txt", "w")
    balance.write("£")
    balance.write("1000000")
    balance_in_int = int(balance.read())
    while True:
        user_input = input("Check balance(c), Deposit money(d), withdraw money(w), or exit(e): ")
        if user_input == "c":
            print(balance)
        elif user_input == "w":
            how_much_to_withdraw = int(input("How much to deposit?: "))
            how_much_to_withdraw_in_str = str(how_much_to_withdraw)
            if how_much_to_withdraw > balance_in_int:
                print("Not enough money!")
            else:
                print("Withdrawn!")
                balance.write(how_much_to_withdraw_in_str)
        elif user_input == "d":
            how_much_to_deposit = int(input("How much to deposit?: "))
            balance_in_int += how_much_to_deposit
            how_much_to_deposit_in_str = str(how_much_to_deposit)
            balance.write(how_much_to_deposit_in_str)
            print("Deposited!")
        elif user_input == "e":
            print("Bye!")
            break
        else:
            print("Invalid input!")



making_an_atm()