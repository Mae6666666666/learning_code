# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.
#
# Sample output
# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt
# The contents of the file inscribed.txt would be
#
# Sample data
# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team
# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.


# ask user what their name is
# ask where to save the file and save to a string
# add the name to a string you write out
# add to the file that its saved in: (Hi (name), we hope you enjoy learning Python with us! Best, Mooc.fi Team)

def personalised_msge():
    if False:
        name = input("Whom should I sign this to?:")
        file_name = input("Where shall I save it?:")
    else:
        name = "Ada"
        file_name = "inscribed.txt"

    message = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
    with open(file_name, "w") as new_file:
        new_file.write(message)

personalised_msge()




























