# Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.
#
# The program should work as follows:
#
# Sample output
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: auto
# The word in English: car
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: roska
# The word in English: garbage
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: laukku
# The word in English: bag
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: bag
# roska - garbage
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: car
# auto - car
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: laukku
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 3
# Bye!

# print add word search quit etc
# input name function

# to do add section:
# ask for a word in French
# ask for the French word in English
# append to the file as a list. e.g if the user put in chat and then cat, it would be stored like chat;cat
# then add a linebreak after. full example below:
# chat;cat\n
# print dictionary added

# to do search function:
# ask for word in file (input) (dictionary.txt), it dont need to be french or english specifically
# then open the file as newfile
# do a for loop
# remove the line break
# split function to get rid of ;
# french should be on the left so you print out the right which is the english version...
# french is part[0] english is part[1]
# make every single one of the words lowercase before u check using a for loop so user can type in lowercase to search...
# and then you can find the same word even in upper
# find function for french so part[0].find(part[1])
# print out the format like this: French - English

# to quit:
# if x == 3:
#     print("Bye!")
#     break

# check every single step with print

def word_searching_and_adding():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function:"))
        if function == 1:
            the_word_in_french = input("The word in French:")
            the_word_in_english = input("The word in English:")
            with open("dictionary.txt", "w") as word_dictionary:
                word_dictionary.write(the_word_in_french)
                word_dictionary.write(the_word_in_english)
                word_dictionary.write("\n")
        elif function == 2:
            ask_for_word = input("Search term:")
            with open("dictionary.txt") as word_dictionary:
                reading_in_the_file = word_dictionary.read()
                if ask_for_word in reading_in_the_file:
                    print(f"{ask_for_word} - other word corresponding")
                else:
                    print(f"{ask_for_word} could not be found")
        else:
            print("Bye!")
            break

word_searching_and_adding()