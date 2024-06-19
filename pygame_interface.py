# import modules
import pygame
import sys
from datetime import datetime, timedelta
from pygame_functions import *

# initialise pygame
pygame.init()

# screen dimensions
WIDTH, HEIGHT = 800, 600

# colours 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# font
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# screen set up
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Compost Bin Manager")

# Button setup
button_circle_center = (100, HEIGHT - 100)
button_circle_radius = 25  # Half the original size
archive_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 50, 100, 30)

# Circle settings
circle_radius = 10
circle_spacing = 200
circle_positions = [
    (100, 80),
    (300, 80),
    (500, 80),
    (700, 80),
]

# Main Page
# Key: 4 circles (red, yellow, green, grey) - overdue, due, done, not due
draw_key(screen, visible=True)

# Create a new bin button

# If a new bin is created:
# Open up a new page
# Display a monthly calendar with bin number at the top
# Automatically select today's date - a circle should surround creation date
# Users should be able to select a different date if necessary

# Schedule Flip Dates
## When a date is selected, 7 dates 2 days apart should be circled with a green outline
# User should be able to escape pop up and go back to main page

# Display bins based on today's date. If bin is due, it is yellow. If done - green. If not to be flipped - grey
# Bins should be represented as a circle with bin number inside
# If bin is clicked, bin should turn from yellow to green

# Once bin is finished flipping, it should be added to the archive 

# button - archive page
# the archive page presents a rectangle with the bin number, initial date:, and finish date


