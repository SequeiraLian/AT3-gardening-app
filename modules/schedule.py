#  This module is given an input date from the user. Every 2 days from the given date, the bin must be flipped. These days must be recorded. 7 dates must be given back to the user. 

# import
import datetime 
from datetime import date

# ask user for first date
initial_date = int(input("Enter initial date in the format YYYY-MM-DD: "))

# TODO: test/check that date is given in correct format

# TODO: calculate every 2 days from given date
scheduled_date = date(initial_date) + datetime.day(2)
print (scheduled_date)


# TODO: repeat 7 times

# TODO: print 7 dates 