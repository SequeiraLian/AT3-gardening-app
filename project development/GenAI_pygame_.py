# NOTE: Generative AI was used in the creation of this user interface
# PLEASE BE ADVISED: Interface does not work as pygame crashed on my computer

import pygame
from pygame.locals import *
from datetime import datetime, timedelta

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up fonts
font = pygame.font.SysFont(None, 24)

# Set up screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Compost Bin Tracker")

# Set up clock
clock = pygame.time.Clock()

class CompostBin:
    def __init__(self, bin_id, start_date):
        self.bin_id = bin_id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.flip_schedule = self.calculate_flip_schedule()
        self.flips = []

    def calculate_flip_schedule(self):
        schedule = []
        for i in range(1, 8):
            next_flip_date = self.start_date + timedelta(days=2 * i)
            schedule.append(next_flip_date.strftime("%Y-%m-%d"))
        return schedule

    def add_flip_date(self, flip_date):
        self.flips.append(flip_date)

    def get_flip_count(self):
        return len(self.flips)

    def flips_remaining(self):
        return max(0, 7 - self.get_flip_count())

    def is_completed(self):
        return self.get_flip_count() == 7

class BinArchive:
    def __init__(self):
        self.archive = {}

    def add_bin(self, compost_bin):
        self.archive[compost_bin.bin_id] = compost_bin

    def get_archive(self):
        return self.archive

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_bins(bins, x, y):
    for compost_bin in bins.values():
        bin_text = f"Bin {compost_bin.bin_id}: {compost_bin.get_flip_count()} flips"
        draw_text(bin_text, BLACK, x, y)
        y += 30

def track_bins():
    bins = {}
    archive = BinArchive()

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    bin_id = input("Enter bin ID: ")
                    start_date = input("Enter the start date of the compost bin (YYYY-MM-DD): ")
                    bins[bin_id] = CompostBin(bin_id, start_date)
                    print(f"Added Bin {bin_id} with start date {start_date}.")
                elif event.key == K_f:
                    bin_id = input("Enter the bin ID to record a flip: ")
                    if bin_id in bins:
                        compost_bin = bins[bin_id]
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
                elif event.key == K_q:
                    running = False

        draw_text("Press 'a' to add a new bin, 'f' to record a flip, or 'q' to quit.", BLACK, 20, 20)
        draw_text("Active Bins:", BLACK, 20, 50)
        draw_bins(bins, 20, 80)
        draw_text("Archived Bins:", BLACK, 400, 50)
        draw_bins(archive.get_archive(), 400, 80)

        pygame.display.flip()
        clock.tick(2)

    pygame.quit()

# Example usage
track_bins()
