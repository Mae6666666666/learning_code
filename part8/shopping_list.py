from fractions import Fraction
from numbers import Number

shopping_list = ["bananas", "eggs", "milk", "cereal", "bread"]

def total_units(ShoppingList):
    print(len(shopping_list))
    print(shopping_list[0])
    print(shopping_list.amount(1))
    print(shopping_list.item(2))
    print(shopping_list.amount(2))




total_units(shopping_list)