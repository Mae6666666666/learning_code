import datetime

def example_code():
    birth_date = input("Enter birth date (dd-mm-yy): ")
    try:
        datetime.datetime.strptime(birth_date, "%d-%m-%Y")
    except:
        print("Date in incorrect format, please try again with the following format: dd-mm-yyyy")


class FormatChecker:
    def time_format(self):
        time_of_day = input("Enter time of day (H:%M:%S): ")
        try:
            datetime.datetime.strptime(time_of_day, "%H:%M:%S")
            print("Time format is correct")
        except:
            print("Time of day not in correct format, please try again in the (%H:%M:%S) format.")

    def date_format(self):
        date = input("Enter date (DD-MM-YYYY): ")
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
            print("Date format is correct")
        except:
            print("Invalid date, please try again in the (DD-MM/YYYY) format.")

    def gimme_an_email(self):
        email = input("Enter email: ")
        while True:
            if email[-3] == "com":
                print("Valid email")
                break
            else:
                print("Invalid email, please try again in the (.com) format.")

        # you can also do this for a more foolproof email checker:
        # if "@" not in email and "." not in email:
        #     print("Invalid email, please try again in the (@) format.")



FormatChecker().time_format()
FormatChecker().date_format()
FormatChecker().gimme_an_email()
