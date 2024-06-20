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

# key function
def draw_key(screen, visible):
    if visible == True:
        # Draw Key label
        key_label = FONT.render("Key:", True, BLACK)
        screen.blit(key_label, (50, 50))

        # Draw circles and labels aligned with the Key
        circle_labels = ["overdue", "due", "done", "empty"]
        for i, (color, label) in enumerate(zip([RED, YELLOW, GREEN, GRAY], circle_labels)):
            pygame.draw.circle(screen, color, (60 + 90 * (i + 1), 50), circle_radius)
            label_surface = SMALL_FONT.render(label, True, BLACK)
            screen.blit(label_surface, (60 + 90 * (i + 1) - 20, 70))

# create new bin button
def create_new_bint():
    # Draw initial screen with create button and archive button
    pygame.draw.circle(screen, BLACK, button_circle_center, button_circle_radius, 4)
    
    # Create + Button
    create_text = FONT.render("+", True, BLACK)
    create_text_rect = create_text.get_rect(center=(button_circle_center[0], button_circle_center[1]))
    screen.blit(create_text, (button_circle_center[0], button_circle_center[1]))

    # Create New Bin Label
    create_new_bin_label = FONT.render("Create New Bin:", True, BLACK)
    screen.blit(create_new_bin_label, (50, 50))


# Calendar page
def draw_calendar(screen, year, month, flip_dates, bin_number):
    days = (days_in_month[month - 1])
    start_date = datetime(year, month, 1)
    start_day = start_date.weekday()

    # Draw calendar background
    pygame.draw.rect(screen, WHITE, calendar_rect)

    # Month label
    month_label = FONT.render(start_date.strftime("%B %Y"), True, BLACK)
    screen.blit(month_label, (calendar_rect.x + 50, calendar_rect.y - 40))

    # Bin number label
    bin_label = FONT.render(f"Bin {bin_number}", True, BLACK)
    screen.blit(bin_label, (calendar_rect.x + 100, calendar_rect.y - 80))

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

    # Draw the back button
    back_label = FONT.render("x", True, BLACK)
    back_rect = back_label.get_rect(topright=(calendar_rect.x + calendar_rect.width - 10, calendar_rect.y - 40))
    screen.blit(back_label, back_rect)

    return back_rect

def draw_bins(screen, bins):
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

# archive page
def draw_archive(screen, archive):
    screen.fill(WHITE)
    if archive:
        y_offset = 50
        for archived_bin in archive:
            bin_info = f"Bin {archived_bin['bin_number']} (Start Date: {archived_bin['initial_date']}, Final Date: {archived_bin['flip_dates'][-1]})"
            text = SMALL_FONT.render(bin_info, True, BLACK)
            screen.blit(text, (50, y_offset))
            y_offset += 30
            if y_offset > HEIGHT - 100:
                break
    else:
        text = FONT.render("No bins in the archive.", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2))

def main():
    global calendar_visible, selected_date, flip_dates, archive_visible, current_bin_number
    
    running = True
    #TODO: change to update year and month based on imported module
    year, month = 2024, 6 

    bin_counter = 1 # initial bin counter starts at 1
    back_button_rect = None
    key_visible = True  # Initially visible
    
    while running:
        screen.fill(WHITE)

        if archive_visible:
            draw_archive(screen, archive)
            pygame.draw.rect(screen, WHITE, back_button_rect)
            back_text = SMALL_FONT.render("Back", True, BLACK)
            screen.blit(back_text, (back_button_rect.x + 10, back_button_rect.y + 5))
        
        else:
            # Draw initial screen with create button and archive button
            pygame.draw.circle(screen, BLACK, button_circle_center, button_circle_radius, 4)
            
            create_text = FONT.render("+", True, BLACK)
            create_text_rect = create_text.get_rect(center=(button_circle_center[0] - 10, button_circle_center[1] - 10))
            screen.blit(create_text, (button_circle_center[0] - 10, button_circle_center[1] - 10))
            pygame.draw.rect(screen, WHITE, archive_button_rect)
            archive_text = SMALL_FONT.render("Archive", True, BLACK)
            screen.blit(archive_text, (archive_button_rect.x + 10, archive_button_rect.y + 5))

            draw_bins(screen, bins)

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
                        day = y * 7 + x - datetime(year, month, 1).weekday() + 1
                        if 1 <= day <= days_in_month[month - 1]:
                            selected_date = datetime(year, month, day)
                            flip_dates = get_seven_dates(selected_date)
                            bins.append({'bin_number': bin_counter, 'initial_date': selected_date.strftime("%d-%m-%Y"), 'flip_dates': flip_dates})
                            bin_counter += 1
                            calendar_visible = False
                            key_visible = True  # Show key when calendar closes
                    elif calendar_visible and back_button_rect and back_button_rect.collidepoint(event.pos):
                        calendar_visible = False
                        key_visible = True  # Show key when calendar closes

        if calendar_visible:
            back_button_rect = draw_calendar(screen, year, month, flip_dates, current_bin_number)

        draw_key(screen, key_visible)  # Call draw_key() with visibility parameter
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
