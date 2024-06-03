from datetime import datetime, timedelta

# Function to create a new bin
def create_new_bin(bin_number, start_date=None):
    if start_date:
        initial_creation_date = datetime.strptime(start_date, "%d-%m-%Y")
    else:
        initial_creation_date = datetime.now()
    
    initial_creation_date_str = initial_creation_date.strftime("%d-%m-%Y")
    flip_dates = get_seven_dates(initial_creation_date_str)
    print(f"Here are the next 7 flip dates for bin {bin_number}: ", flip_dates)
    return {'bin_number': bin_number, 'initial_date': initial_creation_date_str, 'flip_dates': flip_dates}

# Schedule function to get flip dates
def get_seven_dates(initial_date_str):
    initial_date = datetime.strptime(initial_date_str, "%d-%m-%Y")
    dates = [(initial_date + timedelta(days=i * 2)).strftime("%d-%m-%Y") for i in range(1, 8)]
    return dates

# Function to track bins and automatically archive completed bins
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

# Function to view archived bins
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

    # Create test bins with flip dates starting on 03-06-2024
    test_start_date = "03-06-2024"
    for _ in range(3):  # Create 3 test bins
        bin_data = create_new_bin(bin_counter, test_start_date)
        if bin_data:
            bins.append(bin_data)
            bin_counter += 1

    while True:
        command = input("Enter '1' to create a new bin, '2' to track bins, '3' to view archived bins, or '4' to quit: ").strip().lower()
        if command == '1':
            bin_data = create_new_bin(bin_counter)
            if bin_data:
                bins.append(bin_data)
                bin_counter += 1
        elif command == '2':
            if bins:
                track_bins(bins, archive)
            else:
                print("No bins to track.")
        elif command == '3':
            view_archive(archive)
        elif command == '4':
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
