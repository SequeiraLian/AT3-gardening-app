import pygame
import sys
from datetime import datetime, timedelta

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# Font
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Compost Bin Manager")

# button set up

# main screen set up
#TODO: write "Key:"
# add 4 circles next to Key - red, yellow, green, gray 
# under each circle write overdue, due, done, empty
# under key, add + button (create/add new bin)
# add archive button at the bottom

# create new bin function
# schedule function
# track function
# archive function

# Calendar variables
calendar_visible = False
archive_visible = False
calendar_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 150, 300, 300)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
selected_date = None
flip_dates = []
bins = []
archive = []

# Calendar function
def draw_calendar(screen, year, month, flip_dates):
    days = days_in_month[month - 1]
    start_date = datetime(year, month, 1)
    start_day = start_date.weekday()

    # Draw calendar background
    pygame.draw.rect(screen, WHITE, calendar_rect)

    # TODO: write month on top of calendar
    

    # Draw days of the week
    days_of_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for i, day in enumerate(days_of_week):
        text = SMALL_FONT.render(day, True, BLACK)
        screen.blit(text, (calendar_rect.x + 10 + i * 40, calendar_rect.y + 10))

    # Draw days
    for day in range(1, days + 1):
        x = (start_day + day - 1) % 7
        y = (start_day + day - 1) // 7
        date = datetime(year, month, day).strftime("%d-%m-%Y")
        color = GREEN if date in flip_dates else BLACK
        text = SMALL_FONT.render(str(day), True, color)
        screen.blit(text, (calendar_rect.x + 10 + x * 40, calendar_rect.y + 40 + y * 40))

