from random import randint

def lottery_numbers2(amount: int, lower: int, upper: int):
    lottery_draw = []
    while len(lottery_draw) < amount:
        lottery_num = randint(lower, upper)
        if lottery_num not in lottery_draw:
            lottery_draw.append(lottery_num)
        # if lottery_num >= lower and lottery_num <= upper:
    return sorted(lottery_draw)



from random import sample

def lottery_numbers_in_sample(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    weekly_draw = sample(number_pool, amount)
    return sorted(weekly_draw)


for number in lottery_numbers_in_sample(7, 1, 40):
    print(number)
# getting_lottery_numbers = lottery_numbers(5, 1, 7)
# print(getting_lottery_numbers)




