from datetime import date

def list_of_years(dates):
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)
    dates = [date1, date2, date3]
    return min(dates).year

print(list_of_years(dates))
