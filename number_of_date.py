"""
This program converts date to number.
For example, 4 February is the 35th day.
Here, i use Gregorian Calendar and the definition of leap year follows
"""

#Standard input for date
day = int(input('Enter day in Integer: '))
month = int(input('Enter month in Integer: '))
year = int(input('Enter year in Integer: '))

#Years list
normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]

#Leap year criteria
if (year %400 == 0):
    year = leap_year
else:
    if(year %4 == 0):
        year = leap_year
    else:
        year = normal_year

#Convert month to number of days
for i in range(0,month-1):
    day = day + year[i]

#Result
print('It is: ', day)


