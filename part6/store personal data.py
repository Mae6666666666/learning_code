# Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.
#
# The tuple contains the following elements:
#
# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format

# write a function
# create a tuple
# write the tuple to people.csv

#HERE IS WHERE WE ADD TO THE BOTTOM OF A FILE
#BECUASE WE USE A FOR APPEND

person = ()
def store_personal_data(person: tuple):
    with open("people.csv", "a") as personal_info:
        string_to_write = f"{person[0]};{person[1]};{person[2]}\n"

        personal_info.write(string_to_write)

    print(string_to_write)
    return 0
store_personal_data(("Paul Paulson2", 37, 175.5))
