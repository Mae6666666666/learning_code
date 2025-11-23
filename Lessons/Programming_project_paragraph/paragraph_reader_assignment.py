
# this class holds functions from returning total words and letters,
# finding the most frequent word, and finding unique words
class ParagraphReader:
    # takes an input from the user as a string
    user_paragraph = input("Please enter a paragraph: ")

    # defines total_words_and_letters with self meaning it can use everything
    # in the class and that its part of the class
    def total_words_and_letters(self):
        # setting letter_count to zero
        letter_count = 0
        # this splits all the words in the user's paragraph into individual words
        words = self.user_paragraph.split()
        # this turns all those single words to numbers to get a total number
        word_count = len(words)

        # loops through each letter in the user's paragraph
        for letter in self.user_paragraph:
            # each time a letter comes through, the number count for letters increases
            letter_count += len(letter)
            # if the letter is a space
            if letter == " ":
                # it is ignored by taking away one from the letter count
                letter_count -= 1
        # returns the total letters and total words when function is called
        return f"total letters: {letter_count} \ntotal words: {word_count}"

    # function is in the class called most_frequent_word
    def most_frequent_word(self):
        # the split thing separates the paragraph into words
        words = self.user_paragraph.lower().split()
        # frequency is an empty dictionary
        frequency = {}

        # loops through every word in the paragraph, now referred to as words
        for word in words:
            # if the word is in the frequency
            if word in frequency:
                # the specific word is added with a one next to it to show how many times it has been typed in
                frequency[word] += 1
            # if it's not in frequency
            else:
                # the frequency for the word will simply be 1
                frequency[word] = 1

        # setting highest_count to one
        highest_count = 1
        # most_frequent is set to an empty string
        most_frequent = ""

        # looping through each word in the frequency
        for word in frequency:
            # if the frequency of the word is higher than the highest_count
            if frequency[word] > highest_count:
                # the highest count will be changed to that word's count
                highest_count = frequency[word]
                # the most frequent will also store that word
                most_frequent = word

        # the most frequent and how often it appeared will be returned when function is called
        return f"The most frequent word is '{most_frequent}' which appears {highest_count} times."

    # unique_words is called as a function and the self states this is part of the class
    def unique_words(self):
        # words is set to the user's paragraph all in lowercase with each word separate
        words = self.user_paragraph.lower().split()
        # counts is set as an empty dictionary
        counts = {}

        # looping through each word in the paragraph
        for word in words:
            # if the word is in counts
            if word in counts:
                # that word will have a plus one and so on associated with it
                counts[word] += 1
            # if not...
            else:
                # the counter for the word will just be set as one since it only occurred once
                counts[word] = 1

        # unique is an empty list
        unique = []
        # for the key (word), and the value (count), in the items of counts which is a dictionary
        for word, count in counts.items():
            # if the count is only equal to one
            if count == 1:
                # the word will be added to the once empty unique list
                unique.append(word)

        # the unique list will be returned when function is called
        return f"Unique words: {unique}"


# setting the class to a variable name so it can be called
getting_paragraph = ParagraphReader()
# print the function that is in the class called total_words_and_letters (in other words make the function actually run)
print(getting_paragraph.total_words_and_letters())
# print the function that is in the class called most_frequent_word (in other words make the function actually run)
print(getting_paragraph.most_frequent_word())
# print the function that is in the class called unique_words (in other words make the function actually run)
print(getting_paragraph.unique_words())

