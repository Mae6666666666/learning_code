
# date = [24, 6, 2020]
# def screentime():
#     how_many_days = int(input("How many days?: "))
#     for i in range(0, how_many_days):
#         screen_time = input(f"Screen time {date}: ")
#
#         with open("late_june.txt", "a") as june_screentime:
#             june_screentime.write("\n")
#             june_screentime.write(screen_time)




from datetime import datetime
from datetime import timedelta

def screentime():
    adding_minutes_as_int = 0
    average_minutes = 0
    dates = []
    time_period = input("give start date:")
    how_many_days = int(input("How many days?: "))
    stripped_start_date = datetime.strptime(time_period,"%d.%m.%Y")
    # formatted_stripped = stripped_start_date.strftime(format="%d.%m.%Y")
    end_date = stripped_start_date + timedelta(days=how_many_days)

    for i in range(0, how_many_days):
        screen_time = input(f"Screen time: ")
        screen_time_with_no_space = screen_time.split(" ")

        dates.append(screen_time)
        for item in screen_time_with_no_space:
            adding_minutes_as_int += int(item)
            print(adding_minutes_as_int)
        average_minutes += adding_minutes_as_int / (how_many_days * 3)

        with open("late_june.txt", "w") as june_screentime:
            june_screentime.write(f"time period: {time_period}-{end_date}")
            june_screentime.write("\n")
            june_screentime.write(f"total minutes: {adding_minutes_as_int}")
            june_screentime.write("\n")
            june_screentime.write(f"average: {average_minutes}")
            june_screentime.write("\n")
            # june_screentime.write(f"dates: {dates}")
            # june_screentime.write("\n")
            # june_screentime.write(screen_time)
            for i in dates:
                june_screentime.write(i)
                june_screentime.write("\n")




screentime()



