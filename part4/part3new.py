# Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.
#
# An example execution of the program:
#
# Sample output
# Index: 0
# New value: 10
# [10, 2, 3, 4, 5]
# Index: 2
# New value: 250
# [10, 2, 250, 4, 5]
# Index: 4
# New value: -45
# [10, 2, 250, 4, -45]
# Index: -1
from itertools import count
from tabnanny import check


def the_values():
    values = []
    while True:
        index = int(input("Please give an index:"))
        values.append(index)
        print(f"New value:{index}")
        print(values)

        if index == -1:
            break

#
# Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.
#
# An example of expected behaviour:
#
# Sample output
# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]

def list_of_the_numbers():
    value = 0
    list_of_numbers = []
    number_of_items = int(input("How many items do you want to add?:"))
    amount_of_items = 0
    while True:
        items = int(input(f"Item {value + 1}:"))
        print(f"Item {value + 1}: {items}")
        value += 1
        amount_of_items += 1
        list_of_numbers.append(items)
        print(list_of_numbers)
        if number_of_items == amount_of_items:
            break

# Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
#
# The list is printed out in the beginning and after each operation. Have a look at the example execution below:
#
# Sample output
# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!

def addition_removal_or_exit():
    the_list = []
    number = 1
    while True:
        add_or_remove = input("a(d)d, (r)emove or e(x)it:")
        if add_or_remove == "d":
            the_list.append(number)
            number += 1
            print(the_list)
        elif add_or_remove == "r":
            the_list.pop(0)
            print(the_list)

        elif add_or_remove == "x":
            print("Bye!")
            break


# Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
#
# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

def the_words():
    store_the_words = []
    number = 0
    while True:
        word = input("word:")
        if word not in store_the_words:
            store_the_words.append(word)
            number += 1
        else:
            print(f"You've typed in {number} different words")
            break


# Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:
#
# in the order the items were added
# ordered from smallest to greatest
# The program exits when the user types in 0.
#
# An example of expected behaviour:
#
# Sample output
# New item: 3
# The list now: [3]
# The list in order: [3]
# New item: 1
# The list now: [3, 1]
# The list in order: [1, 3]
# New item: 9
# The list now: [3, 1, 9]
# The list in order: [1, 3, 9]
# New item: 5
# The list now: [3, 1, 9, 5]
# The list in order: [1, 3, 5, 9]
# New item: 0
# Bye!

def list_sort():
    the_list = []
    while True:
        item = int(input("New item:"))
        the_list.append(item)
        sorted_verion = sorted(the_list)
        print(f"The list now: {the_list}")
        print(f"The list sorted: {sorted_verion}")
        if item == 0:
            print("Bye!")
            break

#
# Please write a function named length which takes a list as its argument and returns the length of the list.
#
# my_list = [1, 2, 3, 4, 5]
# result = length(my_list)
# print("The length is", result)
#
# # the list given as an argument doesn't need to be stored in any variable
# result = length([1, 1, 1, 1])
# print("The length is", result)
# Sample output
# The length is 5
# The length is 4

def length(my_list):
    result = len(my_list)
    print(f"The length is: {result}")

my_list = [1, 2, 3, 4, 5]


# Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
#
# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)

def mean(my_list):
    adding = sum(my_list)
    division = len(my_list)
    print(f"The mean value is: {adding / division}")

my_list = [1, 2, 3, 4, 5]


# Please write a function named  range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.
#
# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)

def range_of_list(my_list):
    maximum_number = max(my_list)
    minimum_number = min(my_list)
    print(f"The range of the list is: {maximum_number - minimum_number}")

my_list = [1, 2, 3, 4, 5]

#
# Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.
#
# This is how it should work:
#
# Sample output
# Please type in a string: Python
# P
# *
# y
# *
# t
# *
# h
# *
# o
# *
# n
# *


def user_input():
    word = input("Please type in a word:")
    for letter in word:
        print(letter)
        print("*")
#
# Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.
#
# An example of expected behaviour:
#
# Sample output
# Please type in a positive integer: 4
# -4
# -3
# -2
# -1
# 1
# 2
# 3
# 4

def number_range():
    # holding_positive_number = 0
    positive_number = int(input("Type in a positive number:"))
    for i in range(-positive_number, positive_number + 1):
        print (i)

# Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.
#
# For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:
#
# Sample output
# ***
# *******
# *
# *
# **

my_list = [3, 7, 1, 1, 2]

def list_of_stars(my_list):
    index = 0

    while index < len(my_list):
        print(my_list[index] * "*")
        index += 1

# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.
#
# Please also write a main program which asks the user to type in words until they type in a palindrome:
#
# Sample output
# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

# word = input("Type in a word:")
def palindtomes(word):
    word_backwards = word[::-1]
    while True:
        if word_backwards == word:
            print("That is a palindrome")
            break
        else:
            print("That is not a palindrome")
            break

# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
#
# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)
# Sample output
# The result is 9


my_list = [1, -2, 3, -4, 5]
def sum_of_positives(my_list):
    result = 0
    for item in my_list:
        if item > 0:
            result += item
            print(f"The result is {result}")

# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.
#
# my_list = [1, 2, 3, 4, 5]
# new_list = even_numbers(my_list)
# print("original", my_list)
# print("new", new_list)
# Sample output
# original [1, 2, 3, 4, 5]
# new [2, 4]

new_list = []
my_list = [1, 2, 3, 4, 5]
def even_numbers(my_list):
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
            print(f"Old list: {my_list}")
            print("New list:", new_list)

# Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.
#
# my_list = ["first", "second", "fourth", "eleventh"]
#
# result = length_of_longest(my_list)
# print(result)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
#
# result = length_of_longest(my_list)
# print(result)
# Sample output
# 8
# 7

longest = []
longest_length = 0
my_list = ["first", "second", "fourth", "eleventh"]
my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
def length_of_longest(my_list):
    longest = (max(my_list))
    longest_length = len(longest)
    print(longest_length)


# Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.
#
# my_list = ["first", "second", "fourth", "eleventh"]
#
# result = shortest(my_list)
# print(result)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
#
# result = shortest(my_list)
# print(result)
# Sample output
# first
# tim
my_list = ["first", "second", "fourth", "eleventh"]
my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
shortest_list = min(my_list)
shortest_list2 = min(my_list2)
def shortest(my_list):
        print(shortest_list)
        print(shortest_list2)

# Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.
#
# The order of the strings in the returned list should be the same as in the original.
#
# my_list = ["first", "second", "fourth", "eleventh"]
#
# result = all_the_longest(my_list)
# print(result) # ['eleventh']
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
#
# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']


#im not sure what key does in this. i went on the python help thing, not the ai and it did work when i eventually wrotw it properly but i didnt know how to find the answer without looking for help and finding something i hadnt learned yet
my_list = ["first", "second", "fourth", "eleventh", "adele", "mark", "dorothy", "tim", "hedy", "richard"]
def all_the_longest(my_list):
    # length = max(len(my_list))
    print (max(my_list, key=len))


# Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.
#
# Hint: use f-strings to format the floating point numbers into suitable strings.
#
# An example of expected beahviour:
#
# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)
# Sample output
# ['1.23', '0.33', '0.11', '3.45']

my_list = [1.234, 0.3333, 0.11111, 3.446]
def formatted(my_list):
    for num in my_list:
        print(f"New list: {num:.2f}")


# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.
#
# An example of how the function should work:
#
# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']

my_list = ["Hi", "there", "example", "one more"]
def everthing_reversed(my_list):
    for i in my_list:
        reversed_word = i[::-1]
        print(reversed_word)


# Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
#
# An example of expected behaviour:
#
# first_string = "abcdbde"
# print(most_common_character(first_string))
#
# second_string = "exemplaryelementary"
# print(most_common_character(second_string))
# Sample output
# b
# e

# Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.
#
# An example of how the function should work:
#
# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))
# Sample output
# 3

the_matrix = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]


def count_matching_elements(my_matrix: list, element: int):
    total = 0
    for row in my_matrix:
        for number in row:
            if number == element:
                total += 1
    return total


# print(count_matching_elements(the_matrix, 1))




# In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.
#
# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:
#
# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.
#
# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0
#
#

the_game_board = [[1, 1, 1, 2], [1, 1, 2, 2], [1, 0, 0, 2], [0, 2, 1, 2]]
def who_won(game_board):
    total_player_1 = 0
    total_player_2 = 0
    for row in game_board:
        for number in row:
            if number == 1:
                total_player_1 += 1
                break
            elif number == 2:
                total_player_2 += 1
                break
            else:
                break
    if total_player_1 > total_player_2:
        print("1")
    elif total_player_1 < total_player_2:
        print("2")
    else:
        print("Tie")

# print(who_won(the_game_board))

# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.
#
# An example of expected behaviour:
#
#
# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))
# Sample output
# howdydoody

strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
def longest(strings):
    longest_string = ""
    for word in strings:
        if len(word) > len(longest_string):
            longest_string = word
    print(longest_string)



# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.
#
# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.
#
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

def row_correct(sudoku: list, row_no: int):
    the_row: list = sudoku[row_no]
    for i in range(1, 10):
        if the_row.count(i) > 2:
            print("False")
        else:
            print("True")
            break

# print(row_correct(sudoku, 1))
# Sample output
# True
# False

# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.
#
# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.
#
# Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.
#
# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
#
# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))
# Sample output
# False
# True

# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
#
# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.
#
# An example of the function at work:
#
# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)
#     print("doubled:", numbers_doubled)
# Sample output
# original: [2, 4, 5, 3, 11, -4]
# doubled: [2, 4, 5, 3, 11, -4, 2, 4, 5, 3, 11, -4]

numbers = [2, 4, 5, 3, 11, -4]
def double_items(numbers: list):
    numbers_doubled = []
    item = 0
    if __name__ == "__main__":
        for number in numbers:
            item += 1
            numbers_doubled.append(number)
        print("original:", numbers)
        print("doubled:", numbers_doubled * 2)

# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.
#
# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.
#
# The function should not have a return value - it should directly modify the list it receives as a parameter.
#
# An example of how the function works:
#
# if __name__ == "__main__":
#     numbers = [2, 4, 6, 1, 3, 5]
#     remove_smallest(numbers)
#     print(numbers)
# Sample output
# [2, 4, 6, 3, 5]

numbers = [2, 4, 6, 1, 3, 5]
def remove_smallest(numbers: list):
    if __name__ == "__main__":
        smallest = min(numbers)
        result = numbers.remove(smallest)
        print(numbers)

# Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.
#
# Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.
#
# NB: when compared to the sudoku exercises, the arguments the function takes are the other way around here. The column x comes first, and the row y second.
#
# The board consists of the following strings:
#
# "": empty square
# "X": player 1 symbol
# "O": player 2 symbol
# The function should return True if the square was empty and the symbol was successfully placed on the game board. The function should return False if the square was occupied, or if the coordinates weren't valid.
#
# An example execution of the function:
#
# game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
# print(play_turn(game_board, 2, 0, "X"))
# print(game_board)
# Sample output
# True
# [['', '', 'X'], ['', '', ''], ['', '', '']]

game_board = [["", "", "x"], ["", "", ""], ["", "", ""]]
def play_turn(game_board: list, x: int, y: int, piece: str):
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False

    return(game_board)

# print(play_turn(game_board, 2, 0, "X"))

# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
#
# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.
#
# The following matrix
#
# 1 2 3
# 4 5 6
# 7 8 9
# transposed looks like this:
#
# 1 4 7
# 2 5 8
# 3 6 9
# The function should not have a return value. The matrix should be modified directly through the reference.

# my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# def transpose(matrix: list):
#     for column in matrix:
#         for number in column

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(matrix: list):
    result = [[],[],[]]
    for number in reversed(range(0, 3)):
        # print(f"number: {number}")
        inner_list = matrix[number]
        # print(f"Inner list: {inner_list}")
        for inner_number in reversed(range(0, 3)):
            # print(f"Inner number: {inner_number}")
            # print(inner_list[inner_number])
            print(f"number: {number}")
            print(f"Inner number: {inner_number}")
            result[2 - number].append(inner_list[inner_number])
    print(result)

# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.
#
# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.
#
# An example of the function in action:
#
# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])
# Sample output
# 1
# 6
# 120


def factorials(n: int):
    total = 1
    for adding in range(1, n + 1):
        print(adding)
        total = total * adding

    return total

# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.
#
# For example, the function call histogram("abba") should print out
#
# Sample output
# a **
# b **
# while histogram("statistically") should print out
#
# Sample output
# s **
# t ***
# a **
# i **
# c *
# l **
# y *

my_string = ""

# my_list = [1,4,7,9]
# my_list[0] = "second number"
# my_dic = {}
#
# my_first_letter = "s"
# # my_dic["s"]
# my_dic["second number"] = "l"
# myString = "second number"
# my_dic["third number"] = 3
# my_dic["fourth number"] = "hello Mo fo"
#
# # print(my_dic["s"])
#
#
# if "s" not in my_dic:
#     my_dic["s"] = "*"
# else:
#     my_dic["s"] += "*"




def histogram(my_string):
    letters_dic = {}

    for letter in my_string:

        if letter not in letters_dic:
            letters_dic[letter] = "*"
        else:
            letters_dic[letter] += "*"


    print(letters_dic)
# histogram("sups")
# histogram("super sisters")


# Please write a phone book application. It should work as follows:
#
# Sample output
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

def phone_book():
    name = ""
    while True:
        command = int(input("1 search, 2 add, 3 quit:"))
        if command == 1:
            name_search = input("name:")
            if name_search == name:
                print(number)
            if name_search != name:
                print("no number")
        if command == 2:
            name_add = input("name:")
            number = int(input("number:"))
            print("ok!")
            name += name_add
        if command == 3:
            print("quitting...")
            break
# phone_book()

# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.
#
# An example of its use:
#
# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)
# Sample output
# {"first": 1, "second": 2, "third": 3, "fourth": 4}
# NB: the principles regarding lists covered here also hold for dictionaries passed as arguments.
#
# If you have trouble completing this exercise, the visualisation tool might help you understand what your code is or isn't doing.
#

s = {1: "first", 2: "second", 3: "third", 4: "fourth", 67: "fifth"}
def invert(dictionary: dict):
    new_dick = {}
    for key in dictionary:
        # print(f"dictionary[key] = {dictionary[key]}")
        # print(f"key= {key}")

        new_dick[dictionary[key]] = key
    return new_dick

# print(invert(s))
# print(s)

# print(s[1])

# Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.
#
# An example of its use:
#
# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
#
# my_movies = find_movies(database, "python")
# print(my_movies)
# Sample output
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]


database = [
    {
        "name": "Gone with the Python",
        "director": "Victor Pything",
        "year": 2017, "runtime": 116
     },
{
    "name": "Pythons on a Plane",
 "director": "Renny Pytholin",
 "year": 2001, "runtime": 94
},
{
    "name": "Dawn of the Dead Programmers",
    "director": "M. Night Python",
    "year": 2011,
    "runtime": 101
}
]

def find_movies(database: list, search_term: str):
    for movie in database:
        if search_term == movie["name"]:
            return movie


# found_movie = find_movies(database, "Dawn of the Dead Programmers")
# print(found_movie)
# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:
#
# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments
# An example of its use:
#
#
# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))
# Sample output
# (-1, 5, 7)

my_tuple = (5, 3, -1)
def create_tuple(x: int, y: int, z: int):
    if __name__ == "__main__":
        sorted_tuple = sorted(my_tuple)
        return sorted_tuple

# sorted_tuple_again = create_tuple(5, 3, -1)
# print(sorted_tuple_again)
# create_tuple(5, 3, -1)


# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.
#
# An example of the function in action:
#
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]
#
# print(oldest_person(people))
# Sample output
# Mary
#

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
def oldest_person(people: list):
   years = min(people)
   print(years)
# oldest_person(people)
# logic error

# In this exercise we are handling tuples just like the ones described in the previous exercise.
#
# Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.
#
# An example of its use:
#
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]
#
# older = older_people(people, 1979)
# print(older)
# Sample output
# [ 'Adam', 'Mary' ]

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
year = (1977, 1985, 1953, 1997)
def older_people(people: list, year: int):
    oldest = min(people)
    print(oldest)

# older_people(people, year)
# logic error



# In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

# adding students
#
# First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.
#
# These function are used as follows:
#
# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")
# Your program should now print out
#
# Sample output
# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database

students = {}
# students["Peter"] = "no completed courses"
def add_student(database:dict, name: str):
    



add_student(students, "Peter")
add_student(students, "Eliza")
# def add_student():
#     for name in students:
#         who_to_find = input("Name:")
#         if who_to_find == name:
#             print("no completed courses")
#         else:
#             print("no such person in the database")
#             break


# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.
#
# Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.
#
# Sample output
# Layers: 3
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC
# Sample output
# Layers: 4
# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD


def square_letters():
    amount_of_layers = int(input("Layers:"))
    amount_of_layers_times_2 = amount_of_layers * 2 - 1
    for amount_of_layers in range(1, amount_of_layers):
        print(amount_of_layers_times_2 * "D")


#a little logic error, doesnt need to be a tuple






































