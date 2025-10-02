import json

my_dic = {
    "people":
        {
            "mom":
                {
                    "name": "kim",
                    "age": 42,
                    "nationality": "white"

                },
            "mae":
                {
                    "name": "mae",
                    "age": 16,
                    "nationality": "white"
                }
        }
}

with open("junk.json", "w") as random_file:
    random_file.write(my_dic)
