# Please write a function named  range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.
#
# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)
# Sample output
# The range of the list is 4
# from part4.part4 import my_list

# def range_of_list(my_listA):
#     my_list = [1, 2, 3, 4, 5]
#     greatest = max(my_listA)
#     smallest = min(my_listA)
#     result = (greatest - smallest)
#     return result
#
# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list)
# print("The range of the list is", result)
#
# my_list2 = [10, 222, 345, 444, 526]
# result = range_of_list(my_list2)
# print("The range of the list is", result)

# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
#
# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)
# Sample output
# The result is 9

adding = 0
my_list = [1, -2, 3, -4, 5]
def sum_of_positives(my_list):
    for positives in (my_list):
        if my_list > 0:
            adding.append(my_list)
            positives += adding
        return positives


result = sum_of_positives(my_list)
