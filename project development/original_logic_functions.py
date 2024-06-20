# NOTE: Generative AI was used in the creation of this logic

# import
from datetime import datetime, timedelta

# Function to create a new bin
def create_new_bin(bin_number):
    # Take the initial_creation date & format it
    initial_creation_date = datetime.strptime(input("What date did you start the bin?: (dd-mm-yyyy)"),"%d-%m-%Y")
    #initial_creation_date = datetime.now()
    initial_creation_date_str = initial_creation_date.strftime("%d-%m-%Y")
        
    # Input creation date, and get 7 flip dates back
    flip_dates = get_seven_dates(initial_creation_date_str)
    print("Bin ", bin_number, "created")
    print(f"Flip this bin ", bin_number, "on", flip_dates)
        
    # Return a dictionary with bin number and dates
    return {'bin_number': bin_number, 'initial_date': initial_creation_date_str, 'flip_dates': flip_dates}

# Schedule function
def get_seven_dates(initial_date_str):
    # Convert the input string to a datetime object
    initial_date = datetime.strptime(initial_date_str, "%d-%m-%Y")
    
    # Initialize an empty list to store the dates
    dates = []
    
    # Generate 7 dates, each 2 days apart
    for i in range(1, 8):
        new_date = initial_date + timedelta(days=i * 2)
        dates.append(new_date.strftime("%d-%m-%Y"))
    
    return dates



# function to track each bin
def track_bins():
    bin_number = input("Which bin did you flip?")
    return bin_number



'''
# Function to track bins 
def track_bins(bins, archive):
    
    today_str = datetime.now().strftime("%d-%m-%Y")
    for bin in bins[:]:
        bin_number = bin['bin_number']
        flip_dates = bin['flip_dates']
        all_flipped = True

        for j, date in enumerate(flip_dates):
            if date == today_str:
                response = input(f"Have you flipped bin {bin_number} scheduled for today ({date})? (yes/no): ").strip().lower()
                if response == 'no':
                    new_date = (datetime.strptime(date, "%d-%m-%Y") + timedelta(days=1)).strftime("%d-%m-%Y")
                    flip_dates[j] = new_date
                    print(f"Flip date for bin {bin_number} has been rescheduled to {new_date}.")
                    all_flipped = False
                else:
                    print(f"Bin {bin_number} has been flipped as scheduled.")
        
        if all_flipped and all(datetime.strptime(date, "%d-%m-%Y") < datetime.now() for date in flip_dates):
            archive.append(bin)
            bins.remove(bin)
            print(f"Bin {bin_number} has been completed and moved to the archive.")

'''
            
# Archive Function 
def view_archive(archive):
    if archive:
        print("Archived bins:")
        for archived_bin in archive:
            print(f"Bin {archived_bin['bin_number']} with initial date {archived_bin['initial_date']} and flip dates {archived_bin['flip_dates']}")
    else:
        print("No bins in the archive.")

def main():
    bins = []
    archive = []
    bin_counter = 1

    while True:
        command = input("Enter '1' to create a new bin, '2' to track bins, '3' to view archive or '4' to quit: ")
        if command == '1':
            bin_data = create_new_bin(bin_counter)
            if bin_data:
                bins.append(bin_data)
                bin_counter += 1
        
        elif command == '2':
            if bins:
                track_bins()
            else:
                print("No bins to track.")

        elif command == '3':
            view_archive(archive)
        
        elif command == '4':
            break
        else:
            print("Invalid command. Please try again.")

main()
