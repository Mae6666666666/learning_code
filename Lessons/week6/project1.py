import json

def project1():
    user_input = input("What genre do you want to be quizzed on? rap (r), pop (p), or alternative? (a): ")
    with open("project1_dic.json", "r") as new_file:
        data = json.load(new_file)
        if user_input == "r":
            print("This is your question... what song is this from?: ")
            print(data["genres"]["rap"]["lyric"])
            putting_in_answer = input("Please type in answer here: ")
            if putting_in_answer == "without me":
                print(f"correct!!, this song is by {data["genres"]["rap"]["artist"]}")
                print("thanks for playing!!")
            else:
                print("wrong!!!")
        elif user_input == "p":
            print("This is your question... what song is this from?: ")
            print(data["genres"]["pop"]["lyric"])
            putting_in_answer = input("Please type in answer here: ")
            if putting_in_answer == "feel good inc":
                print(f"correct!!, this song is by {data["genres"]["pop"]["artist"]}")
                print("thanks for playing!!")
            else:
                print("wrong!!!")
        elif user_input == "a":
            print("This is your question... what song is this from?: ")
            print(data["genres"]["alternative"]["lyric"])
            putting_in_answer = input("Please type in answer here: ")
            if putting_in_answer == "sleep":
                print(f"correct!!, this song is by {data["genres"]["alternative"]["artist"]}")
                print("thanks for playing!!")
            else:
                print("wrong!!!")

project1()