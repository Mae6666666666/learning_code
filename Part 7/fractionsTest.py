# Please familiarize yourself with the Python module fractions. Use it to write a function named fractionate(amount: int), which takes the number of parts as its argument. The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.
#
# An example of the function in action:
#
# for p in fractionate(3):
#     print(p)
#
# print()
#
# print(fractionate(5))
# Sample output
# 1/3
# 1/3
# 1/3
#
# [Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
from fractions import Fraction


# print(Fraction(16, -10))
def fractionate(first_num:int):
    my_var_list = [3,4,5,6,7,8,6,5,3,4,5]
    putting_fractions_in_list = []
    doing_the_fraction = Fraction(1, first_num)

    for i in range(first_num):
        putting_fractions_in_list.append(doing_the_fraction)




    return putting_fractions_in_list
function_response = fractionate(3)


for p in fractionate(3):
    print(p)

print()

print(fractionate(5))










