import calendar

month = int(input("Enter month: "))
year = int(input("Enter year: "))

print(calendar.calendar(year, month, w=0, l=0))
