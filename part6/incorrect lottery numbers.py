# The file lottery_numbers.csv containts winning lottery numbers in the following format:
#
# Sample data
# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...
# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.
#
# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):
#
# The week number is incorrect:

# first create a define function ☑️
# open the lottery.csv file ☑️
# use a for loop to loop through each component in the file ☑️
# get rid of linebreaks ☑️
# get rid of semicolons with split ☑️
# print to check if it is working each new line of code ☑️
# create an if statement in for loop to check if each number is between the range of 1 and 39
# if it is between the range, add it to another file called correct
# if its false, add it to the incorrect file

def sorting_the_lottery():
    with open("lottery.csv") as original_lottery:
        for numbers in original_lottery:
            no_linebreaks = numbers.replace("\n", "")
            breaking_up_numbers = no_linebreaks.split(";")
            print(f"breaking_up_numbers: {breaking_up_numbers}")
            print(f"numbers: {numbers}")
            getting_rid_of_week = breaking_up_numbers.pop(0)

            for individuals in breaking_up_numbers:
                print(individuals)
                from_string_to_int = int(individuals)
                print(from_string_to_int)
                if numbers >= 1 and numbers <= 39:
                    with open("correct_numbers.csv", "w") as correct_lottery:
                        correct_lottery.write(numbers)
                        print(numbers)
                else:
                    with open("incorrect_numbers.csv", "w") as incorrect_lottery:
                        incorrect_lottery.write(numbers)
                        print(numbers)

sorting_the_lottery()

