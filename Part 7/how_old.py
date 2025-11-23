from calendar import month
# jan = 31
# feb = 29
# mar = 31
# apr = 30
# may = 31
# jun = 30
# jul = 31
# aug = 31
# sep = 30
# octo = 31
# nov = 30
# dec = 31
#
# def age():
#     date = int(input("date: "))
#     months = int(input("month: "))
#     year = int(input("year: "))


from datetime import datetime
def age():
    dates = int(input("date: "))
    months = int(input("month: "))
    year = int(input("year: "))
    users_dob = datetime(year, months, dates)
    millenium = datetime(2000, 1, 1)
    how_many_days_old = str(millenium - users_dob)
    if how_many_days_old[0] == "-":
        print("You weren't born yet")
    else:
        print(f"You were {how_many_days_old} days old")
age()