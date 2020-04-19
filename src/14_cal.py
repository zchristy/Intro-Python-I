"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


system = sys.argv
today = datetime.now()
month = today.month
year = today.year
error_month = ''
error_year = ''

# function to check if user inputs were made
def index_in_list(a_list, index):
    return(index < len(a_list))

# check to see if input is able to be converted into int
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

# check if user input month value, if so set month to user value
def check_month_input():
    global month, error_month

    if(index_in_list(system, 1)):
        if is_int(system[1]):
            arg1 = int(system[1])
            if arg1 >=1 and arg1 <=12:
                month = arg1
                return True
            else:
                error_month = f'[ {arg1} ]'
                return False
        else:
            error_month = f'[ {system[1]} ]'
            return False
    else:
        return month

# check if user input year value, if so set year to user value
def check_year_input():
    global year, error_year

    if(index_in_list(system, 2)):
        if is_int(system[2]):
            arg2 = int(system[2])
            if arg2 >=1900 and arg2 <=2050:
                year = arg2
                return True
            else:
                error_year = f'[ {arg2} ]'
                return False
        else:
            error_year = f'[ {system[2]} ]'
            return False
    else:
        return year

# if check user input function returns false print error message
if not check_month_input() or not check_year_input():
    error_message = f'Invalid Inputs: {error_month} {error_year} is not an acceptable input.\nPlease use a number 1 through 12 for the month, and the full year ex: 2020 between 1900 - 2050.\nWhen running the program on the command line it should look similar to this: \n\n\'python3 14_cal.py [month] [year]\'\n\nOrder matters when inputing the dates, makes sure you are inputing month before year.'
    print(error_message)
else:
    print(calendar.month(year, month))
