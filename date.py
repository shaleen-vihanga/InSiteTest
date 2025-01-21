import datetime

def has_friday_13(month, year):
    return datetime.date(year,month,13).weekday() == 4

month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(has_friday_13(month,year))
    