# Please write a function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle. The function should return the length of the hypotenuse, or the side opposite to the right angle.
#
# You can use the Pythagorean theorem to calculate the result. You will need the sqrt function from the math module.
#
# Some examples:
#
# print(hypotenuse(3,4)) # 5.0
# print(hypotenuse(5,12)) # 13.0
# print(hypotenuse(1,1)) # 1.4142135623730951
import math


def hypotenuse(length1: float, length2: float):
    power_length1 = length1 * length1
    power_length2 = length2 * length2
    adding_powers = power_length1 + power_length2
    square_root_lengths = math.sqrt(adding_powers)
    print(square_root_lengths)

hypotenuse(4, 2)