from item import Item

class Suitcase:
    adding_item = []
    adding_item_amount = 0
    adding_weight = 0
    def __init__(self, max_weight: int):
        self.max_weight = max_weight

    def start(self):
        if self.adding_item_amount == 1:
            return f"{self.adding_item} item ({self.max_weight} kg)"
        else:
            return f"{self.adding_item} items ({self.max_weight} kg)"


    def add_item(self, book):
        self.adding_item_amount += 1
        self.adding_item.append(book)
        self.adding_weight += self.max_weight

    def print_items(self):
        for item in self.adding_item:
            print(item)

    def weight(self):
        return self.adding_weight

    def heaviest_item(self):
        heaviest = self.adding_item


book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} kg")



