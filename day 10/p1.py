#
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didnt provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
# formated_string = format_name("AngeLA", "YU")
# print(format_name(f_name = input("What is you first name?\n"), l_name=input("What is your last name?\n")))
#
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    """Check years(including leaps) and months.
     And print  amount of days"""
    if m < 1 or m > 12:
        print("Invalid month")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True :
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[m - 1]
    return month_days[m-1]
# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(y=year, m=month)
print(days)

