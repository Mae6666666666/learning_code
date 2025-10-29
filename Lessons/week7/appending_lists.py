from random import randint



# def making_the_list():
#     my_new_list = []
#     return my_new_list
#
#
#
# def adding_to_the_list():
#     my_new_list.append(randint(1, 10))
#     print(my_new_list)
#
# list_from_function = making_the_list()
# list_from_function(adding_to_the_list())

def making_the_list():
    return []

def adding_list_to_list(range_list):
    how_many = int(input("How many numbers to add? "))
    for i in range(how_many):
        range_list.append(randint(1, 100))
    print(sum(range_list) / len(range_list))
    return range_list

making_the_list()
print(adding_list_to_list([]))
print(adding_list_to_list([]))