from random import randint

dice_a = [3, 3, 3, 3, 3, 6]
dice_b = [2, 2, 2, 5, 5, 5]
dice_c = [1, 4, 4, 4, 4, 4]

def roll(die: str):
    if die == "A":
        random_number1 = randint(0, len(dice_a)-1)
        return dice_a[random_number1]
    elif die == "B":
        random_number2 = randint(0, 5)
        return dice_b[random_number2]
    elif die == "C":
        random_number3 = randint(0, 5)
        return dice_c[random_number3]

def play(die1: str, die2: str, times: int):
    counting_die1_wins = 0
    counting_die2_wins = 0
    counting_ties = 0
    for i in range(0, times):
        die1_result = roll(die1)
        die2_result = roll(die2)
        if die1_result > die2_result:
            counting_die1_wins += 1
        elif die1_result < die2_result:
            counting_die2_wins += 1
        else:
            counting_ties += 1
            
    return (counting_die1_wins, counting_die2_wins, counting_ties)

# the_result = play("A", "B", 1000)
# print(the_result)

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)




# dices = {
#     "A" : [3, 3, 3, 3, 3, 6],
#     "B" : [2, 2, 2, 5, 5, 5],
#     "C" : [1, 4, 4, 4, 4, 4]
# }
#
# def roll(die: str):
#     random_number = randint(0, len(dices[die])-1)
#     return dices[die][random_number]
#
#
# the_roll = roll("C")
# print(the_roll)


