
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
def smallest_average():
    adding_person1 = person1["result1"] + person1["result2"] + person1["result3"]
    adding_person2 = person2["result1"] + person2["result2"] + person2["result3"]
    adding_person3 = person3["result1"] + person3["result2"] + person3["result3"]
    if adding_person1 < adding_person2 and adding_person1 < adding_person3:
        return person1
    elif adding_person2 < adding_person1 and adding_person2 < adding_person3:
        return person2
    else:
        return person3

print(smallest_average())

# def doing_smallest_average():
#     sum_of_person1 = sum(person1["result1"]) + sum(person1["result2"] + person1["result3"])
#     sum_of_person2 = sum(person2["result1"]) + sum(person2["result2"] + person2["result3"])
#     sum_of_person3 = sum(person3["result1"]) + sum(person3["result2"] + person3["result3"])
#     print("The smallest average result is", min(sum_of_person1, sum_of_person3, sum_of_person2))
# doing_smallest_average()
