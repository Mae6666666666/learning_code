# this basically means i is going up till 100 in 10s like 10 20 30...
# for i in range(0, 100, 10):
# so the 0 is where it starts, the 100 is the cap it goes up to, and the 10 is how many it goes up by

# example_list = [2, 69, 5, 9, 6]
#
# for i in range(len(example_list)):
#     print(i)
#
# for i in range(len(example_list)):
#     print(example_list[i])
#
#
# for i in example_list:
#     print(i)


def doing_a_while_true_loop():
    while True:
        giving_a_number = int(input("Please give a number from 1-100: "))
        if giving_a_number > 0 and giving_a_number <= 100:
            print(f"{giving_a_number} is in the range!")
            break
        # elif len(giving_a_number[0]) == "-":
        #     print("Don't add minus numbers.")
        else:
            print("input is out of range, try again")


my_music_dic = {
    "music_type":[
        {
            "genre0": "alternative",
            "genre1": "rock",
            "genre2": "nu-metal",
            "genre3": "metal",
        }
    ],
    {
    "groups":[
            {
            "band0": "Gorillaz",
            "band1": "MCR",
            "band2": "Slipknot",
            "band3": "Korn"
            }
        ]
    }



}