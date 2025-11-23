from collections import Counter

class ListHelper:

    def greatest_frequency(self, my_list: list):
        return Counter(my_list).most_common

    def doubles(self, my_list: list):
        doubled_items = []
        for item in my_list:
            if item == item:
                doubled_items.append(doubled_items)
        return doubled_items








numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))