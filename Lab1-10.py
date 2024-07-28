def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year=None):
    month_days = {
        "January": 31, "February": 28, "March": 31, "April": 30,
        "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    

    if month == "February" and year is not None and is_leap_year(year):
        return 29
    return month_days[month]

month = input("Enter the month name: ")
if month == "February":
    year = int(input("Enter the year: "))
    print(f"The number of days in {month} is: {days_in_month(month, year)}")
else:
    print(f"The number of days in {month} is: {days_in_month(month)}")
