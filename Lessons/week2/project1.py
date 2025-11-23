# take three user inputs, username, score, and game
# take high score, average score, and player score vs average
# print the player score on the game they played
# if statement to see if highscore is higher or lower than average
# print how much higher or lower

import random


def taking_a_highscore():
    username = input("Give username: ")
    game = input("Give the game you played: ")
    current_score = int(input("What is your current score?: "))
    print(f"{game}: {current_score}")
    while True:
        average_score = random.randint(1,1000)
        print(average_score)
        highscore = random.randint(1000, 2000)
        print(highscore)
        if average_score >= highscore:
            print("Invalid, please lower your average score")
        if current_score > average_score and current_score > highscore:
            print("Congrats! you beat your highscore and your average!")
            break
        elif current_score < average_score:
            print("Sorry! you'll do better next time!")
            break
        elif current_score < highscore:
            print("So close! you'll get there eventually!")
            break
taking_a_highscore()
