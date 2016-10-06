"""
This program advances number days from the date of the input. I will comment it
for easier learning
"""

year=int(raw_input('Write a year: '))
month=int(raw_input('Write a month: '))
day=int(raw_input('Write a day: '))
number=int(raw_input('Write a value: '))

#first we declare some useful variables
months_year = 12 #number of months in a year
days_month = 0 #number of days in a month which we don't know yet
leap_year=False #and we have to check if it is leap year

if year%4==0 and year%100!=0 or year%400==0:
    leap_year=True #easy leap year checking

#We have February particular case
if month==2:
    if leap_year:
        days_month = 29
    else:
        days_month = 28
#Now we have the months with 31 days
elif month==1 or month==3 or mmonth==5 or month==7 or month==8 or month==10 or month==12:
    days_month=31
#finally we have all others 30 days months
else:
    days_month=30

#Now that we know the days of the month we advance the number on the days variable
day+=number
#If the final day exceeds the days of the month we advance one month and
#subtract the number of the days in that month
if day > days_month:
    month+=1
    day-=days_month
#If the final month exceeds the months in a year we advance one year and
#subtract the number of months of the year
if month > months_year:
    year+=1
    month-=months_year

#finally we print the days, months and year separated by '\' and converted
#to string
print str(day) + '/' + str(month) + '/' + str(year)
