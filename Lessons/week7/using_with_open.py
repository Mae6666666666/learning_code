from random import randint


def opening_a_random_file():
    f = open("lesson7_example", "r")
    for line in f:
        print(line)

def writing_gorillaz():
    write = open("Helloooo.txt", "w")
    write.write("Hellooooo")
    write.close()

# this is how u do the files without with open as x, instead putting it into a variable
# make sure to close the file after its done. its just ediquite
def appending_gorillaz():
    appending = open("is_anyone_there.txt", "a")
    appending.write("is anyone there??")
    appending.write("\n")
    appending.write("M1A1, thousand miles an hour...")
    appending.close()

def selecting_a_random_file():
    random_number_int = []
    random_number_str = ""
    random_file = randint(1, 2)
    random_number_int.append(randint(1, 100))
    for number in random_number_int:
        random_number_str += str(number)
        if random_file == 1:
            file = open("is_anyone_there.txt", "a")
            file.write(random_number_str)
            print(random_number_str)
            file.close()
        else:
            file = open("Helloooo.txt", "a")
            file.write(random_number_str)
            print(random_number_str)
            file.close()

selecting_a_random_file()