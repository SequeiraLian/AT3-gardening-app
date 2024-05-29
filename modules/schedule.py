#  This module is given an input date from the user. Every 2 days from the given date, the bin must be flipped. These days must be recorded. 7 dates must be given back to the user. 

# import databases
import datetime 
from datetime import datetime

# current dateTime
now = datetime.now()

# convert date to string
initial_date = now.strftime("%d/%m/%Y")
print('Initial Date:', initial_date)

# TODO: calculate every 2 days from given date


num_of_dates = 7
start = datetime.datetime.today()
date_list = [start.date() + datetime.timedelta(days=x) for x in range(num_of_dates)]
print('Next 3 days starting from today')
print(date_list)



# TODO: repeat 7 times

# TODO: print 7 dates 