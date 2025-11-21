

class BankAccount:

    def __init__(self, owner_name_temp: str, account_number_temp: str, balance_temp: float):
        self.owner_name = owner_name_temp
        self.account_number = account_number_temp
        self.balances = balance_temp

    def __service_charge(self):
        fee = self.balances / 100
        self.balances -= fee

    def deposit(self, amount: float):
        self.balances += amount
        self.__service_charge()


    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balances -= amount
            self.__service_charge()
        else:
            raise ValueError("Not enough money in balance")

    @property
    def balance(self):
        return self.balances


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)


