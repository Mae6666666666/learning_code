# remember. if you do say an input and stuff. at the end of the round brackets,
# you can add .lower to make the user's input lowercase. so if a user accidentally adds a capital,
# it won't matter because it'll be lowercased
from part4.part3new import user_input


def learning_match_cases():
    a_number = 1
    #Calling a matchcase
    match a_number:
        #If matchcase ==1
        case 1:
            print("Hi")
        #Case _ means else in matchcase language
        case _:
            print("False")
            
# user_input1 = int(input("Give a number:"))
# user_input2 = int(input("Give another number:"))

# if user_input1 < 100:
#     print(f"{user_input1} is less than 100")
# elif user_input1 == 100:
#     print(f"{user_input1} is equal to 100")
#
# if user_input2 < 100:
#     print(f"{user_input2} is less than 100")
# elif user_input2 == 100:
#     print(f"{user_input2} is equal to 100")

# user_input1 = int(input("Give a number:"))
# user_input2 = int(input("Give another number:"))
#
# match user_input1:
#     case
# num1 = int(input("Give number: "))
# num2 = int(input("Give another: "))
# match (num1, num2):
#     #to use an or statement in a match case thing, you use |  no joke, it's literally just |
#     case 10 | 20 | 30:
#         print("Hi")
#     case _:
#         print("Nah")

def doing_dictionaries_with_match_cases():
    my_dic = {}
    user_input = int(input("put in the number 4:"))
    match user_input():
        case 2:
            my_dic = {"number": user_input}
        case _:
            print(f"Add a 4, not {user_input}")
    print(my_dic["number"])
    return my_dic["number"]

doing_dictionaries_with_match_cases()
