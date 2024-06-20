# NOTE: Generative AI was used in the creation of this logic

# import modules
from datetime import datetime, timedelta

# class to track multiple bins simultaneously 
class CompostBin:
    def __init__(self, bin_id, start_date):
        self.bin_id = bin_id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.flip_schedule = self.calculate_flip_schedule()
        self.flips = []

    # calculate flip schedule function 
    def calculate_flip_schedule(self):
        # Calculate the flip schedule based on the start date
        schedule = []
        for i in range(1, 8):
            next_flip_date = self.start_date + timedelta(days=2 * i)
            schedule.append(next_flip_date.strftime("%Y-%m-%d"))
        return schedule

    # add flip date function
    def add_flip_date(self, flip_date):
        # Add a flip date to the list of flips
        self.flips.append(flip_date)

    # get flip count function
    def get_flip_count(self):
        #Get the number of flips recorded
        return len(self.flips)

    # flips remaining function
    def flips_remaining(self):
        #Calculate the number of flips remaining to complete 7 flips
        return max(0, 7 - self.get_flip_count())

    # Check if bin has been flipped 7 times function
    def is_completed(self):
        return self.get_flip_count() == 7

    def __str__(self):
        """Return a string representation of the bin."""
        flip_count = self.get_flip_count()
        flips_left = self.flips_remaining()
        flips_str = "\n  Actual flips: " + ", ".join(self.flips) if self.flips else "No flips recorded."
        reminder = f"{flips_left} flips remaining." if flips_left > 0 else "All flips completed."
        return f"Bin {self.bin_id}: {flip_count} flips recorded. {reminder}\n{flips_str}\n  Flip schedule (excluding start date): {self.flip_schedule}"

# class represents an archive of completed compost bins
class BinArchive:
    def __init__(self):
        self.archive = {}

    # add completed bins to archive
    def add_bin(self, compost_bin):
        self.archive[compost_bin.bin_id] = compost_bin

    # retreive archive
    def get_archive(self):
        return self.archive

# main function 
def track_bins():
    bins = {}
    archive = BinArchive()
    
    while True:
        # user input
        action = input("Enter 'a' to add a new bin, 'f' to record a flip, or 'q' to quit: ").lower()
        
        # add new bin
        if action == 'a':
            bin_id = input("Enter bin ID: ")
            start_date = input("Enter the start date of the compost bin (YYYY-MM-DD): ")
            bins[bin_id] = CompostBin(bin_id, start_date)
            print(f"Added Bin {bin_id} with start date {start_date}.")
        
        # record a flip
        elif action == 'f':
            bin_id = input("Enter the bin ID to record a flip: ")
            if bin_id in bins:
                compost_bin = bins[bin_id]
                print(f"Flip Schedule for Bin {bin_id}:\n{compost_bin.flip_schedule}")
                flip_date = input(f"Enter the actual flip date for Bin {bin_id} (YYYY-MM-DD): ")
                try:
                    datetime.strptime(flip_date, "%Y-%m-%d")
                    compost_bin.add_flip_date(flip_date)
                    print(f"Recorded flip for Bin {bin_id} on {flip_date}.")
                    if compost_bin.is_completed():
                        archive.add_bin(compost_bin)
                        print(f"Congratulations! Bin {bin_id} has been flipped 7 times. Moving to archive.")
                        del bins[bin_id]
                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            else:
                print(f"Bin {bin_id} not found.")
        
        # quit
        elif action == 'q':
            break
        
        else:
            print("Invalid action. Please enter 'a', 'f', or 'q'.")

    # view summary of all bins
    print("\nSummary of all bins:")
    for bin_id, compost_bin in bins.items():
        print(compost_bin)

    # view archive
    print("\nArchived bins:")
    for bin_id, compost_bin in archive.get_archive().items():
        print(compost_bin)

# run program
track_bins()


