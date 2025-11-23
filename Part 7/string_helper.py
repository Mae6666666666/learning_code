from curses.ascii import isupper
import string

# user_words = input("Please give a mix of lower and uppercase words in one: ")
def change_case(orig_string: str):
    upper_to_lower = ""
    lower_to_upper = ""

    for word in orig_string:
        if isupper(word):
            upper_to_lower += word.lower()
        else:
            lower_to_upper += word.upper()
    print(f"The order and lowercase have changed. this is the new one: {upper_to_lower}{lower_to_upper}")

change_case("HeLLo")


def split_in_half(orig_string: str):
    first_half, second_half = orig_string[:len(orig_string)//2 + len(orig_string)%2], orig_string[len(orig_string)//2 + len(orig_string)%2:]
    print(first_half)
    print(second_half)

split_in_half("Hell")

#
# def remove_special_characters(orig_string: str):
#     clean_without_punctuation = ""
#     punctuation_characters = [string.punctuation]
#     for character in orig_string:
#         for special_characters in punctuation_characters:
#             if character != special_characters:
#                 clean_without_punctuation += character
#     print(clean_without_punctuation)

# remove_special_characters("Hello!?")

def remove_special_characters(orig_string: str):
    clean_without_punctuation = ""
    for character in orig_string:
        if string.punctuation.find(character) == -1:
            clean_without_punctuation += character
    return clean_without_punctuation

