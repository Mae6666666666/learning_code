

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount
        return self.balance

    def subtract_from_balance(self, amount: float):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        regular_lunch = 2.50
        if payment >= regular_lunch:
            self.lunches += 1
            payment -= regular_lunch
            return payment
        else:
            return f"Not enough money, balance: {payment}."

    def eat_special(self, payment: float):
        special_lunch = 4.30
        if payment >= special_lunch:
            self.specials += 1
            payment -= special_lunch
            return payment
        else:
            return f"Not enough money, balance: {payment}."

    def eat_lunch_lunchcard(self, card: LunchCard):
        regular_lunch = 2.50

        if card.balance > regular_lunch:
            card.balance -= regular_lunch
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        special_lunch = 4.30

        if card.balance > special_lunch:
            card.balance -= special_lunch
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        return card.balance





exactum = PaymentTerminal()

cards = LunchCard(2)
print(f"Card balance is {cards.balance} euros")

result = exactum.eat_special_lunchcard(cards)
print("Payment successful:", result)

exactum.deposit_money_on_card(cards, 100)
print(f"Card balance is {cards.balance} euros")

result = exactum.eat_special_lunchcard(cards)
print("Payment successful:", result)
print(f"Card balance is {cards.balance} euros")

print("Funds available at the terminal:", exactum.funds)
print("Regular lunches sold:", exactum.lunches)
print("Special lunches sold:", exactum.specials)