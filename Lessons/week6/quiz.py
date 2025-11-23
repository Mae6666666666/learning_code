def health_and_safety_quiz():
    right = 0
    wrong = 0
    fire_drill = input("Should you run or walk to the nearest exit during a fire?: (W) (R): ").lower
    if fire_drill == "w":
        right += 1
    else:
        wrong += 1
    plugging_in = input("When plugging in devices, is it safe to daisy chain wires?: (Y) (N): ").lower
    if plugging_in == "n":
        right += 1
    else:
        wrong += 1
    importance_of_the_three_rule = input("Is it necessary to always have three backups of data in the three rule?: (Y) (N): ").lower
    if importance_of_the_three_rule == "y":
        right += 1
    else:
        wrong += 1
    print(f"In total, you got {right} right, and {wrong} wrong.")
    if right > wrong:
        print("You got more right than wrong, good job")
    elif wrong > right:
        print("You're not good enough.")
    else:
        print("Your score is even")
health_and_safety_quiz()