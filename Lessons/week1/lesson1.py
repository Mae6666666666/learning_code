 # print statements:


# print("Hello world!")
#
#
# name = "Mae Azam"
# student_num = "50581602"
# course = "Digital production"
# print(f"Name: {name}, number: {student_num}, course:{course}")
#
#
#
# rating_out_of_10 = 10
# favourite_music_genre = "Alternative"
# print(f"my fave genre is: {favourite_music_genre}")
# print(f"my rating would be: {rating_out_of_10}")
#
#
# putting_in_a_game = input("Put in a game: ")
# putting_in_a_number = int(input("Put in a rating: "))
# print(putting_in_a_game)
# print(putting_in_a_number)

def recapping_the_most_i_know():
    while True:
        give_a_word_or_search = input("Give entry (g) or search (s) or exit (x): ")
        if give_a_word_or_search == "g":
            adding_word = input("Please give the word: ")
            with open("testing.str", "w") as lesson1:
                word = lesson1.write(adding_word)
                # print(word)
        elif give_a_word_or_search == "s":
            search_term = input("Give the word: ")
            with open("testing.str") as lesson1:
                word_search = lesson1.read()
                if search_term in word_search:
                    print(f"The word you searched for is {word_search}")
                else:
                    print("Not found")
        else:
            print("Bye!")
            break
recapping_the_most_i_know()

