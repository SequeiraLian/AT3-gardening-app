# this module takes an initial date (given by the user) and outputs 7 dates (when the bins need to be flipped). 

# This code was initially created by CHAT-GPT, but I have altered it to be more effective and efficient

# import databases 
from datetime import datetime, timedelta

# Function to create a new bin
def create_new_bin(bin_number):
    # Ask the user if they would like to create a new bin
    response = input("Would you like to create a new compost bin? (yes/no): ").strip().lower()
    
    if response == 'yes':
        # Take the initial_creation date & format it
        initial_creation_date = datetime.now()
        initial_creation_date_str = initial_creation_date.strftime("%d-%m-%Y")
        
        # Input creation date, and get 7 flip dates back
        flip_dates = get_seven_dates(initial_creation_date_str)
        print(f"Here are the next 7 flip dates for bin {bin_number}: ", flip_dates)
        
        # Return a dictionary with bin number and dates
        return {'bin_number': bin_number, 'initial_date': initial_creation_date_str, 'flip_dates': flip_dates}
    else:
        print("No new compost bin created.")
        return None

# schedule function
def get_seven_dates(initial_date_str):
    # Convert the input string to a datetime object
    initial_date = datetime.strptime(initial_date_str, "%d-%m-%Y")
    
    # Initialize an empty list to store the dates
    dates = []
    
    # Generate 7 dates, each 2 days apart
    for i in range(1,8):
        new_date = initial_date + timedelta(days=i * 2)
        dates.append(new_date.strftime("%d-%m-%Y"))
    
    return dates

# Run the function
create_new_bin(bin_number=1)