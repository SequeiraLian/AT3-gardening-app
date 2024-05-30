# this module tracks whether the bin has been flipped on the scheduled date.

# import databases 
from datetime import datetime, timedelta

# import modules
from schedule import create_new_bin, get_seven_dates

# Tracking function
def track_bins(bins):
    today_str = datetime.now().strftime("%d-%m-%Y")
    for bin in bins:
        bin_number = bin['bin_number']
        for j, date in enumerate(bin['flip_dates']):
            if date == today_str:
                response = input(f"Have you flipped bin {bin_number} scheduled for today ({date})? (yes/no): ").strip().lower()
                if response == 'no':
                    new_date = (datetime.strptime(date, "%d-%m-%Y") + timedelta(days=1)).strftime("%d-%m-%Y")
                    bin['flip_dates'][j] = new_date
                    print(f"Flip date for bin {bin_number} has been rescheduled to {new_date}.")
                else:
                    print(f"Bin {bin_number} has been flipped as scheduled.")