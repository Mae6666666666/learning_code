

class LunchCard:
    def __init__(self, balance_temp: float):
        self.balance = balance_temp

    def __str__(self):
        rounded_balance = float(round(self.balance, 1))
        return f'The balance is {rounded_balance} euros'

    def eat_lunch(self):
        if self.balance < 2.60:
            self.balance = self.balance
        else:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance < 4.60:
            self.balance = self.balance
        else:
            self.balance += 4.60

    def deposit_money(self, amount: float):
        if amount < 0:
            raise Exception('You cannot deposit an amount of money less than zero')
        else:
            self.balance += amount


def multiple_cards():
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    peters_card.eat_special()
    graces_card.eat_lunch()
    print(f"peter balance: {peters_card}")
    print (f"grace balance: {graces_card}")
    peters_card.deposit_money(20)
    graces_card.eat_special()
    print(f"peter balance: {peters_card}")
    print(f"grace balance: {graces_card}")
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    graces_card.deposit_money(50)
    print(f"peter balance: {peters_card}")
    print(f"grace balance: {graces_card}")


multiple_cards()


