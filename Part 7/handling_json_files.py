import json


# def print_persons(filename: str):
storing_important_parts = []
with open("handling_json.json") as my_json:
    holding_data = my_json.read()


print_people = json.loads(holding_data)
print(print_people[0]["name"]), print(print_people[0]["age"]), print(print_people[0]["hobbies"])
print(print_people[1]["name"]), print(print_people[1]["age"]), print(print_people[1]["hobbies"])

