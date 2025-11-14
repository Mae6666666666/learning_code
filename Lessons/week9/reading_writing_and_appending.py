
def reading_a_file():
    with open("reading_file.txt", "r") as reading:
        reading_complete = reading.read()
        print(reading_complete)
        return reading_complete

def writing_a_file():
    user_input = input("Give a word please")
    with open("writing_file.txt", "w") as writing:
        writing_complete = writing.write(user_input)
        print(writing_complete)
        return writing_complete

def appending_a_file():
    user_input = input("Give a word please")
    with open("appending_a_file.txt", "a") as appending:
        appending_complete = appending.write(user_input)
        print(appending_complete)
        return appending_complete


reading_a_file()
writing_a_file()
appending_a_file()
