
class Present:
    def __init__(self, name_temp: str, weight_temp: int):
        self.name = name_temp
        self.weight = weight_temp


    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


# book = Present("ABC Book", 2)
#
# print("The name of the present:", book.name)
# print("The weight of the present:", book.weight)
# print("Present:", book)