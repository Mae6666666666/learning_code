

def testSwitch(lang: str):
    match lang:
        case  "JavaScript":
            print("You can become a web developer.")
        case "Python":
            print("You can become a Data Scientist")
        case "php":
            print("You can become a backend developer")
        case "Solidity":
            print("You can become a Blockchain developer")
        case "Java":
            print("You can become a mobile app developer")
        case _:
            print("The language doesn't matter, what matters is solving problems.")

# testSwitch("php")

from enum import Enum

class Location(Enum):
    Outside = "outside"
    Inside = "inside"


class Genre(Enum):
    Classic = 0
    Indie = 1
    Rock = 2
    Alternative = 3
    Electronic = 4

gorillaz = Genre.Electronic

match gorillaz:
    case Genre.Rock:
        print("is rock")
    case Genre.Electronic:
        print("is electronic")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
 # scope stuff
# test01 = 56
# print(test01)
#
#
# def test():
#     test00 = "hello"
#
# test()
#
# while True:
#     test00 = "world"
#
#
# print(test00)

