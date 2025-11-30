

class SimpleDate:
    # full_date = []
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # def altogether(self):
    #     self.full_date.append(self.day)
    #     self.full_date.append(self.month)
    #     self.full_date.append(self.year)
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        if self.day != other.day:
            return self.day < other.day
        else:
            return False



    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        if self.day != other.day:
            return self.day > other.day
        else:
            return False

    def __eq__(self, other):
        if self.year != other.year:
            return False
        if self.month != other.month:
            return False
        if self.day != other.day:
            return False
        return self.day == other.day

    def __ne__(self, other):
        if self.year == other.year:
            return False
        if self.month == other.month:
            return False
        if self.day == other.day:
            return False
        return self.day != other.day

    def __add__(self, other):
        # if other < (30 - self.day):
        #     self.day += other
        # else:

        self.day = (self.day + other) % 31
        if (self.day + other) > 30:
            self.month = ((self.month + int((self.day + other)/30)) % 12)+1




        # if self.day == 30:
        #     self.day = 1
        #     self.month += 1
        # if self.month == 12:
        #     self.year += 1



d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(28, 12, 1985)

d3 = d1 + 3
d4 = d2 + 400

print(d1)
print(d2)
print(d3)
print(d4)

print(((29+3002)%30)+1)
print(1%12)