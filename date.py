import datetime

import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

currentdate = datetime.datetime.now()

day = currentdate.day
month = currentdate.month
year = currentdate.year
weekly_day = currentdate.strftime('%A')

print(f"The day is {day}, the month is {month}, the year is {year} and the weekly day is {weekly_day}.")