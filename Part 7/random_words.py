from random import sample

def words(n: int, beginning: str):
    with open ("words.txt") as word_text:

        finding_word = []
        for word in word_text:
            no_line = word.replace("\n", "")
            if no_line.startswith(beginning):
                finding_word.append(no_line)

        return sample(finding_word, n)


        # for number in range(0, n):
        #     word_text.startswith(beginning)


# words_calling = words(2, "ca")
# print(words_calling)

word_list = words(3, "ca")
for word in word_list:
    print(word)
