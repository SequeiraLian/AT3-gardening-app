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

# setting up variables
# month_to_number
month_to_number = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# Calendar variables
calendar_visible = False
archive_visible = False
calendar_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 150, 300, 300)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
selected_date = None
flip_dates = []
bins = []
archive = []
current_bin_number = None


# Main Page
running = True

# Get the current date
current_datetime = datetime.now()

# get current year and month
current_month = current_datetime.month
current_year = current_datetime.year

bin_counter = 1 # initial bin counter starts at 1
back_button_rect = None
key_visible = True  # Initially visible

while running:
    screen.fill(WHITE)

    if archive_visible == False :
            # Key: 4 circles (red, yellow, green, grey) - overdue, due, done, not due
            if key_visible == True:
                # Draw Key label
                key_label = FONT.render("Key:", True, BLACK)
                screen.blit(key_label, (50, 50))

                # Draw circles and labels aligned with the Key
                circle_labels = ["overdue", "due", "done", "empty"]
                for i, (color, label) in enumerate(zip([RED, YELLOW, GREEN, GRAY], circle_labels)):
                    pygame.draw.circle(screen, color, (60 + 90 * (i + 1), 50), circle_radius)
                    label_surface = SMALL_FONT.render(label, True, BLACK)
                    screen.blit(label_surface, (60 + 90 * (i + 1) - 20, 70))

                # Draw initial screen with create button and archive button
                pygame.draw.circle(screen, BLACK, button_circle_center, button_circle_radius, 4)

                create_text = FONT.render("+", True, BLACK)
                create_text_rect = create_text.get_rect(center=(button_circle_center))
                screen.blit(create_text, create_text_rect)
                pygame.draw.rect(screen, WHITE, archive_button_rect)
                archive_text = SMALL_FONT.render("Archive", True, BLACK)
                screen.blit(archive_text, (archive_button_rect.x + 10, archive_button_rect.y + 5))

                # draw bins
                today = datetime.now().strftime("%d-%m-%Y")

                bin_x_start = 100
                bin_y_start = 150
                bin_x_offset = 100
                bin_y_offset = 150
                max_bins_per_row = 4

                for i, bin in enumerate(bins):
                    bin_label = str(bin['bin_number'])
                    bin_x = bin_x_start + (i % max_bins_per_row) * bin_x_offset
                    bin_y = bin_y_start + (i // max_bins_per_row) * bin_y_offset
                    
                    # Scheduled Bin Flips - Bin colour changes if bin needs to be flipped 
                    color = GRAY  # Default color
                    if today in bin['flip_dates']:
                        color = YELLOW if not bin.get('flipped', False) else GREEN

                    pygame.draw.circle(screen, color, (bin_x, bin_y), circle_radius + 10)
                    pygame.draw.circle(screen, BLACK, (bin_x, bin_y), circle_radius + 10, 2)
                    text = SMALL_FONT.render(bin_label, True, BLACK)
                    text_rect = text.get_rect(center=(bin_x, bin_y))
                    screen.blit(text, text_rect)


    else :
            draw_archive(screen, archive)
            pygame.draw.rect(screen, WHITE, back_button_rect)
            back_text = SMALL_FONT.render("Back", True, BLACK)
            screen.blit(back_text, (back_button_rect.x + 10, back_button_rect.y + 5))


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if archive_visible:
                if back_button_rect and back_button_rect.collidepoint(event.pos):
                    archive_visible = False
            else:
                if (event.pos[0] - button_circle_center[0])**2 + (event.pos[1] - button_circle_center[1])**2 <= button_circle_radius**2:
                    calendar_visible = True
                    current_bin_number = bin_counter
                    key_visible = False  # Hide key when calendar pops up
                elif archive_button_rect.collidepoint(event.pos):
                    archive_visible = True
                elif calendar_visible and calendar_rect.collidepoint(event.pos):
                    x, y = event.pos
                    x = (x - calendar_rect.x - 10) // 40
                    y = (y - calendar_rect.y - 40) // 40
                    day = y * 7 + x - datetime(current_year, current_month, 1).weekday() + 1
                    
                    if 1 <= day <= days_in_month[current_month - 1]:
                        selected_date = datetime(current_year, current_month, day)
                        flip_dates = get_seven_dates(selected_date)
                        bins.append({'bin_number': bin_counter, 'initial_date': selected_date.strftime("%d-%m-%Y"), 'flip_dates': flip_dates})
                        bin_counter += 1
                        calendar_visible = False
                        key_visible = True  # Show key when calendar closes
        
                    elif calendar_visible and back_button_rect and back_button_rect.collidepoint(event.pos):
                        calendar_visible = False
                        key_visible = True  # Show key when calendar closes

                    if calendar_visible:
                        back_button_rect = draw_calendar(screen, current_year, current_month, flip_dates, current_bin_number)

        
    pygame.display.flip()

pygame.quit()   
sys.exit()

if __name__ == "__main__":
    main()

# Create a new bin button

# If a new bin is created:
# Open up a new page
# Display a monthly calendar with bin number at the top
# Automatically select today's date - a circle should surround creation date
# Users should be able to select a different date if necessary

# Schedule Flip Dates
## When a date is selected, 7 dates 2 days apart should be circled with a green outline
# User should be able to escape pop up and go back to main page
# when a new bin is created, all dates should be black 

# Display bins based on today's date. If bin is due, it is yellow. If done - green. If not to be flipped - grey
# Bins should be represented as a circle with bin number inside
# If a yellow bin is clicked, bin colour should turn from yellow to green

# Once bin is finished flipping, it should be added to the archive 

# button - archive page
# the archive page presents a rectangle with the bin number, initial date and finish date



