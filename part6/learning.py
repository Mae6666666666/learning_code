# Question 1:
# Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.
#
# Have a look at the example of expected behaviour below:
#
# Sample output
# Editor: Emacs
# not good
# Editor: Vim
# not good
# Editor: Word
# awful
# Editor: Atom
# not good
# Editor: Visual Studio Code
# an excellent choice!

# while True:
#     editor = input("Editor:")
#     if editor != "Visual Studio Code":
#         print("not good")
#
#     if editor == "Visual Studio Code":
#         print("an excellent choice!")
#         break

# Question 2
# Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.
#
# An example of expected behaviour:
#
# line(7, "%")
# line(10, "LOL")
# line(3, "")
# Sample output
# %%%%%%%
# LLLLLLLLLL
# ***

# def line(integer , string):
#     print(string)
#
# if __name__ == "__main__":
#     line(5 , "hello")

