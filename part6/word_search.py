# The exercise template includes the file words.txt, which contains words in English.
#
# Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.
#
# The search term may include lowercase letters and the following wildcard characters:
#
# A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
# An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.
# If there are no wildcard characters in the search term, only words which match the search term exactly are returned.

# write a def called find_words that takes a string as an argument
# get the file words.txt
# get rid of line spaces
# split function to make a list
# ask for an input to ask for a search term
# if the users search term lines up with any words in the file words.txt, then print them out
# startswith() will check if a specified word starts with another word
# startswith() will check if a specified word nds with a specific word


def find_words():
    my_string_list = []
    with open("words.txt") as word_searching:
        what_to_search_with_caitals = input("Search for?:")
        for line in word_searching:
            no_gap = line.replace("\n", "")
            my_string_list = no_gap.split(";")

            # to find a function, you look if a piece of code has() next to it
            for a_word_with_caitals in my_string_list:
                a_word_lower = a_word_with_caitals.lower()
                what_to_search_lower = what_to_search_with_caitals.lower()
                finding_word = a_word_lower.find(what_to_search_lower)
                #if star at start of what_to_search_lower then find result must be 0
                #if star after postion 0 then finding_word must be not == -1 and grater than 0
                if finding_word != -1:
                    print(f"{finding_word} what to search: {what_to_search_lower} what to find from: {a_word_lower}")





                # if finding_word
                # if a_word.lower() == what_to_search.lower():
                #     print(f"Found: {a_word}")





#how will it find angel
#how will it find Ang
# do this by using upper or lower function for angel
# use find function for ang




find_words()



