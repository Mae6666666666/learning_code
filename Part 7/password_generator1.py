from random import randint
from random import sample
import string
from string import punctuation


# def password_generator(amount):
#     letters = sample(string.ascii_lowercase, amount)
#     turning_letters_into_password = "".join(letters)
#     return turning_letters_into_password
# for i in range(10):
#     print(password_generator(8))






    # letters = string.ascii_lowercase
    # random_letters = randint(letters[amount])


# password_generator(4)

def password_generator2(amount):
    letters = []
    letters_adding = sample(string.ascii_lowercase, amount)
    letters.append(letters_adding)
    punctuation_index = string.punctuation
    letters.append(punctuation_index)
    print(f"punctuation index: {punctuation_index}")
    turning_letters_into_password = "".join(letters_adding)
    return turning_letters_into_password
# for i in range(10):
#     print(password_generator(8))

# password_generator2(2)

def generate_strong_password(amount, numbers, punctuation):
    charcter_pool = string.ascii_lowercase
    if numbers == True:
        charcter_pool += "0123456789"




    if punctuation == True:
        charcter_pool += string.punctuation
    jumbling = sample(charcter_pool, amount)
    return "".join(jumbling)
for i in range(10):
    print(generate_strong_password(8, True, True))

    # print(lowercase)

    # while len(password) < amount:








calling_the_password = generate_strong_password(8, True, True)
print(calling_the_password)