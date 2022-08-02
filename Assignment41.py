# Assignment 41 :  Display calender : Author Tirath

import calendar

year = int(input("Enter year of which calendar you are interested: "))

for i in range(1,13):
    print(calendar.month(year, i))