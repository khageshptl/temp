import calendar
import datetime
print(calendar.TextCalendar(firstweekday = 0).formatyear(2015))

date = str(input())
month, day, year = date.split()
month = int(month)
day = int(day)
year = int(year)
d = datetime.date(year, month, day)
print(d)

day_of_week = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_of_week]
print(day_name)