import json


def print_persons(filename: str):
    with open("handling_json.json") as my_json:
        for component in my_json:
            return component

print_people = print_persons("handling_json.json")
print(print_people["name"])
