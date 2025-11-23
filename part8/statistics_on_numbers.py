
class NumberStats:
    numbers = []
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers += number

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / self.count_numbers()

    def user_numbers(self):
        while True:
            user_number = int(input("Enter a number: "))
            if user_number == -1:
                break
            else:
                self.numbers.append(user_number)


    def sum_of_even_numbers(self):
        even_numbers = 0
        for number in self.numbers:
            if number % 2 == 0:
                even_numbers += number



        return even_numbers



    def sum_of_odd_numbers(self):
        odd_numbers = 0
        for number in self.numbers:
            if number % 2 != 0:
                odd_numbers += number

        return odd_numbers



# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers() + 1)
stats = NumberStats()
# stats.add_number(1)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
stats.user_numbers()
stats.sum_of_even_numbers()
stats.sum_of_odd_numbers()

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.sum_of_even_numbers())
print("Sum of odd numbers:", stats.sum_of_odd_numbers())