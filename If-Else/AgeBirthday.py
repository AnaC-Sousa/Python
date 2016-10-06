"""
I made this program on 7/10/2016 so feel free to change the numbers
This will give you your age base on your day, month and year of birthday
"""
year = int(raw_input('Year of Birthday: '))
month = int(raw_input('Month of Birthday: '))
day = int(raw_input('Day of Birthday: '))

year_today = 2016
month_today = 10
day_today = 7

if month > month_today or day > day_today and month == month_today :
    print "You are",(year_today-year)-1, "years old."
else:
    if year_today - year == 1:
        print "You are 1 year old"
    else:
        print "You are", year_today-year, "years old."
