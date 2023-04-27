
#TASK 1

# org_name = input("Enter the full name of the organization: ")
#
# words = org_name.split()
# abbrev = ""
# for word in words:
#     abbrev += word[0].upper()
#
# print("The abbreviation for", org_name, "is", abbrev)


##############################################################################################
#TASK 2

# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def get_day_of_week(date):
#     days_per_month = (31, 28 + is_leap_year(int(date[:4])), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     days_since_jan1st = sum(days_per_month[:int(date[5:7])-1]) + int(date[-2:])
#     day_of_week_index = (days_since_jan1st - 1) % 7
#     days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#     return days_of_week[day_of_week_index]
#
# date = input(" Enter a date (YYYY-MM-DD): ")
# day_of_week = get_day_of_week(date)
# print(f"The day of the week for {date} is {day_of_week}.")


##############################################################################################

#TASK 3


def get_unique_numbers():
    user_input = input("Enter a comma-separated list of items: ")
    items = user_input.split(",")
    unique_numbers = set()

    for item in items:
        if item.isdigit():
            unique_numbers.add(int(item))
        else:
            return "bad data"
    return unique_numbers
##
unique_numbers = get_unique_numbers()
if unique_numbers == "bad data":
    print("bad data")
else:
    unique_numbers = sorted(unique_numbers)
    print("Unique numbers:", end=" ")
    print(*unique_numbers, sep=",")

