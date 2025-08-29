print("part4")
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

#This variable keeps an array stored
# my_list = [1, 2, 3, 4, 5]
# #While true will loop until the code is falaw
# while True:
#     #Variable for index and new value. index tells the computer what slot the new value is going to be in
#     index = int(input("Index:"))
#     new_value = int(input("New value:"))
#     #Add new value to the list in correct place. minus one because the code starts at 0 automatically
#     my_list[index - 1] = new_value
#     #Print out the list
#     print(my_list)
#     #If the index number is -1, it will end the loop
#     if index == -1:
#         break

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

# #Creating an empty array
# my_list =[]
# #Getting an input that asks for how many items in the list
# items = int(input("How many items?:"))
# #A for loop so it will run as many times as there are items
# for i in range(items):
#     #Item number is plus one'd every time to show item 1, item 2 etc
#     item_number = int(input(f"item {i + 1}:"))
#     #The item that was typed will now be stored in the empty array
#     my_list.append(item_number)
# #Print the final outcome of the list
# print(my_list)


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

#Set number to 0
# num = 0
# #Empty array
# my_list = []
# #Print a message
# print("The list is now []")
# #While loop, if its false, code ends
# while True:
#     #Asks for an input
#     add_or_remove = input("a(d)d, (r)emove or e(x)it:")
#     #If the answer is d it adds another number to the list and prints out the new list
#     if add_or_remove == "d":
#         num += 1
#         my_list.append(num)
#         print(f"The list is now {my_list}")
#     #If the input is r, it removes a number from the list and prits out the current list
#     elif add_or_remove == "r":
#         num += 1
#         num -= 1
#         my_list.append(num)
#         print(f"The list is now {my_list}")
#     #Code ends when user inputs "x" and then prints bye
#     elif add_or_remove == "x":
#         print("Bye!")
#         break

# Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
#
# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words
#Empty array variable
# words = []
#While true loop
# while True:
#     #Variable input
#     word = input("Word: ")
#     #if word in the empty array
#     if word in words happens more than once:
#         #end code
#         break
#     #if not, append the word to the list and print the list number
#     else:
#         words.append(word)
# print(f"You typed in {len(words)} different words")
#
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

#New empty variable
my_list = []

#While true loop
# while True:
#     #Asks for an item
#     item = int(input("New item: "))
#     #if item is 0, code ends
#     if item == 0:
#         print("Bye!")
#         break
#     #new item is appended
#     my_list.append(item)
#     #prints the list unsorted
#     print(f"The list now: {my_list}")
#     #the function sorted, automatically sorts a list that it is brought with
#     print(f"The list in order: {sorted(my_list)}")

# Please write a function named length which takes a list as its argument and returns the length of the list.
# defines the word length and takes my_list as an argument
# def length(my_list):
#     variable has a list
#     my_list = [1, 2, 3, 4, 5]
#     result is set as the length of the list
#     result = len(my_list)
#     print the length of the list
#     print(f"The length is, {result}")
# use the defined function, length
# length(my_list)


# Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
#Variable input for number of times code is run
# number = int(input("How many numbers?"))
# #adding set to 0
# adding = 0
# #my_list starts off empty
# my_list = []
# #range created to run as many times as there are in number ie 3
# for i in range(number):
#     #asks for a mean
#     mean = int(input("Type in your mean:"))
#     #adds the number to the list
#     my_list.append(mean)
#     #adds the mean to the number
#     adding += mean
#     #result equals the actual mean of the numbers
#     result = (adding / number)
# #prints out the end result
# print(f"mean value is, {result}")


# Please write a function named  range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.
#
# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)
# Sample output
# The range of the list is 4

#defines range of lists, takes an argument
# def range_of_list(my_list):
#     #two variables here, one with the smallest value in the list and one with the biggest
#     smallest = min(my_list)
#     largest = max(my_list)
#     #return the product of subtracting the two together
#     return largest - smallest
# #set the list
# my_list = [1, 2, 3, 4, 5]
# #set the result as the range of the list with my list
# result = range_of_list(my_list)
# #print result
# print("The range of the list is", result)

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

# #Variable that asks for a string
# user_input = input("Please type in a string: ")
#
# #for loop that will separate each individual letter and print an astrix between it
# for char in user_input:
#     print(char)
#     print("*")

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

# #variable asks for a positive integer
# number = int(input("Please type in a positive integer: "))
# #for loop has a range from a negative number to a positive one plus 1
# for i in range(-number, number + 1):
#     #if the number printed is 0, it'll print out i
#     if i != 0:
#         print(i)

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

# #defines the list of stars and takes the argument numbers
# def list_of_stars(numbers):
#     #for loop for every numb in numbers
#     for num in numbers:
#         #print astrix times the number
#         print('*' * num)
#
# #Actually calling the function
# list_of_stars([3, 7, 1, 1, 2])

# Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
#
# Some examples of how the function should work:
#
# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False
# Hint: the function sorted can be used on strings as well.

# #we define anagrams and put two arguments in it
# def anagrams(string1, string2):
#     #we return the sorted version of string 1 and make sure its with string 2
#     return sorted(string1) == sorted(string2)
# #we call the function and it should print out true or false
# print(anagrams("tame", "meta"))     # True
# print(anagrams("tame", "mate"))     # True
# print(anagrams("tame", "team"))     # True
# print(anagrams("tabby", "batty"))   # False
# print(anagrams("python", "java"))

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
#
# #define the word palindromes and put word in as the argument
# def palindromes(word):
#     #basically takes the string and reads it backwards. this compares the flipped and unflipped one to see if theyre the same
#     return word == word[::-1]
# #while true loop
# while True:
#     #user inputs a word
#     user_input = input("Please type in a palindrome: ")
#     #if the palindromes are being used
#     if palindromes(user_input):
#         #print this statement
#         print(f"{user_input} is a palindrome!")
#         #end code
#         break
#     #if its not backwards and forwards same then print that
#     else:
#         print("that wasn't a palindrome")

# Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
#
# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)

#defines the sum of posititves and takes the argumet numbers
# def sum_of_positives(numbers):
#     #set value to 0
#     total = 0
#     #for loop for the nums in numbers
#     for num in numbers:
#         #if the number is more than 0
#         if num > 0:
#             #add the number to 0
#             total += num
#     #then return the total
#     return total
# #my list is an array
# my_list = [1, -2, 3, -4, 5]
# #result is the sum of positives with my list
# result = sum_of_positives(my_list)
# #print the outcome
# print("The result is", result)

# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.
#
# my_list = [1, 2, 3, 4, 5]
# new_list = even_numbers(my_list)
# print("original", my_list)
# print("new", new_list)
# Sample output
# original [1, 2, 3, 4, 5]
# new [2, 4]

# #define this and put an argument in it
# def even_numbers(numbers):
#     #empty array
#     evens = []
#     #for loop
#     for num in numbers:
#         #if the nums outcome is 0 when divided by two
#         if num % 2 == 0:
#             #append the number to evens
#             evens.append(num)
#     #return whateer is in there
#     return evens
#
# #fill in the list
# my_list = [1, 2, 3, 4, 5]
# #add the even numbers to the new list
# new_list = even_numbers(my_list)
# #print these statements
# print("original", my_list)
# print("new", new_list)

# Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.
#
# An example of the function at work:
#
# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]

# #defines the list and puts argument in
# def list_sum(list1, list2):
#     #empty array
#     result = []
#     #ranfnge between the length if list 1
#     for i in range(len(list1)):
#         #attach list ones number to list 2s number
#         result.append(list1[i] + list2[i])
#     #return outcome
#     return result
# #variables a and b are arrays
# a = [1, 2, 3]
# b = [7, 8, 9]
# #print the list sum with a and bs number too
# print(list_sum(a, b))  # Output: [8, 10, 12]

# Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
#
# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]

# #define and add argument
# def distinct_numbers(numbers):
#     #return the numbers sorted and in a specific set
#     return sorted(set(numbers))
#
# #call the function to actually see results
# my_list = [3, 2, 2, 1, 3, 3, 1]
# # print the outcome
# print(distinct_numbers(my_list))

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

#this will find the biggest lettered word in an array basically

#define and add argument
# def length_of_longest(strings):
#     #set to 0
#     longest = 0
#     #for loop
#     for s in strings:
#         #if the length of s is bigger than longest
#         if len(s) > longest:
#             #add s to the longest variable
#             longest = len(s)
#     #return longest
#     return longest
# #array
# my_list = ["first", "second", "fourth", "eleventh"]
# #variable
# result = length_of_longest(my_list)
# #print the result
# print(result)  # Output: 8
#
# #array with many names
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# #result is the length with my list
# result = length_of_longest(my_list)
# #print the result
# print(result)  # Output: 7

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
#
# #define with argument
# def shortest(strings):
#     #variable with strings first letter
#     shortest_string = strings[0]
#     #for loop
#     for s in strings:
#         #if the length of s is bigger than shortest string
#         if len(s) < len(shortest_string):
#             #add s to the shortest string
#             shortest_string = s
#     #return shortest string
#     return shortest_string

# #new array
# my_list = ["first", "second", "fourth", "eleventh"]
# #result is the shortest with my list
# result = shortest(my_list)
# #print the result (just shortest(mylist)
# print(result)  # Output: first
#
# #new array
# my_lists = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# #result is whatever the shortest is within my lists
# result = shortest(my_lists)
# #print the result
# print(result)  # Output: tim

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

# #define and add argument
# def all_the_longest(strings):
#     #go through each string in strings and get the length (s) max gets the biggest value. for creates the loop to search for s in strings
#     longest_length = max(len(s) for s in strings)
#     #empty array
#     result = []
#     #another loop
#     for s in strings:
#         #if the length of s is the same length as the longest length it will append the result with s
#         if len(s) == longest_length:
#             result.append(s)
#     #return the result
#     return result
# #array
# my_list = ["first", "second", "fourth", "eleventh"]
# #result is just all the longest and my list
# result = all_the_longest(my_list)
# #print the result
# print(result)
#
# #array
# my_lists = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# #result is the longest with my lists
# result = all_the_longest(my_lists)
# #print the result
# print(result)

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

#This one took me thirty goddamn minutes
# #Make a variable with list
# my_list = [1.234, 0.3333, 0.11111, 3.446]
# #define formatted
# def formatted(my_list):
#     #set result as empty
#     result = []
#     #for loop in my lists, runs every number in my_lists
#     for number in my_list:
#         #this stupid piece of shit stores the numbers in my list but rounds them all to two decimal points
#         formatted_number = f"{number:.2f}"
#         #formatted number is added to result
#         result.append(formatted_number)
#     #result it returned
#     return(result)
#
# #new list is whatever is in formatted my list
# new_list = formatted(my_list)
# #it prints out the result of whatever is in formatted my list
# print(new_list)

# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.
#
# An example of how the function should work:
#
# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']
#
# this variable has a list
# my_list = ["Hi", "there", "example", "one more"]
#define the word everything_reversed and add the argument my list
# def everything_reversed(my_list):
# empty array
#     result = []
#for loop that goes through the list backwards. ::-1 goes from back to front
#     for words in (my_list[::-1]):
# words which is also reversed will be added to reversed word
#         reversed_word = words[::-1]
#append reversed word to the result
#         result.append(reversed_word)
#return the result
#     return result
#print everything reversed which will print whatever is inside the array there backwards
# print(everything_reversed(["Hi", "there", "example", "one more"]))

# Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.
#
# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
#
# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be  [5, 4, 3, 4], with a length of 4.
#
# An example function call:
#
# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))

def longest_series_of_neighbours(longest_series):
    for number in my_list:
        my_list.append(longest_series)
        print(len(longest_series_of_neighbours(longest_series)))




my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))






