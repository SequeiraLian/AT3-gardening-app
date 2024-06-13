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
YELLOW = (255, 255, 0)

# Font
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Compost Bin Manager")

# Button setup
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
back_button_rect = pygame.Rect(50, HEIGHT - 50, 100, 30)
archive_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 50, 100, 30)

# Circle settings
circle_radius = 10
circle_spacing = 100
circle_positions = [
    (100, 80),
    (200, 80),
    (300, 80),
    (400, 80),
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

# Calendar function
def draw_calendar(screen, year, month, flip_dates):
    days = days_in_month[month - 1]
    start_date = datetime(year, month, 1)
    start_day = start_date.weekday()

    # Draw calendar background
    pygame.draw.rect(screen, WHITE, calendar_rect)

    # Month label
    month_label = FONT.render(start_date.strftime("%B %Y"), True, BLACK)
    screen.blit(month_label, (calendar_rect.x + 50, calendar_rect.y - 40))

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
    back_label = FONT.render("X", True, BLACK)
    back_rect = back_label.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(back_label, back_rect)

    return back_rect

# Schedule function to get flip dates
def get_seven_dates(initial_date):
    dates = [(initial_date + timedelta(days=i * 2)).strftime("%d-%m-%Y") for i in range(1, 8)]
    return dates

def create_new_bin(bin_number, start_date=None):
    if start_date:
        initial_creation_date = datetime.strptime(start_date, "%d-%m-%Y")
    else:
        initial_creation_date = datetime.now()
    
    initial_creation_date_str = initial_creation_date.strftime("%d-%m-%Y")
    flip_dates = get_seven_dates(initial_creation_date)
    return {'bin_number': bin_number, 'initial_date': initial_creation_date_str, 'flip_dates': flip_dates}

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
                    all_flipped = False
                else:
                    print(f"Bin {bin_number} has been flipped as scheduled.")
        
        if all_flipped and all(datetime.strptime(date, "%d-%m-%Y") < datetime.now() for date in flip_dates):
            archive.append(bin)
            bins.remove(bin)
            print(f"Bin {bin_number} has been completed and moved to the archive.")

def draw_archive(screen, archive):
    screen.fill(WHITE)
    if archive:
        y_offset = 50
        for archived_bin in archive:
            bin_info = f"Bin {archived_bin['bin_number']} (Initial: {archived_bin['initial_date']}, Final: {archived_bin['flip_dates'][-1]})"
            text = SMALL_FONT.render(bin_info, True, BLACK)
            screen.blit(text, (50, y_offset))
            y_offset += 30
            if y_offset > HEIGHT - 100:
                break
    else:
        text = FONT.render("No bins in the archive.", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2))

def draw_key():
    # Draw Key label
    key_label = FONT.render("Key:", True, BLACK)
    screen.blit(key_label, (50, 50))

    # Draw circles and labels
    for i, (color, label) in enumerate(zip([RED, YELLOW, GREEN, GRAY], ["overdue", "due", "done", "empty"])):
        pygame.draw.circle(screen, color, circle_positions[i], circle_radius)
        label_surface = SMALL_FONT.render(label, True, BLACK)
        screen.blit(label_surface, (circle_positions[i][0] - 20, circle_positions[i][1] + 20))

def main():
    global calendar_visible, selected_date, flip_dates, archive_visible
    
    running = True
    year, month = 2024, 6  # For the calendar example, June 2024
    bin_counter = 1
    back_button_rect = None
    
    while running:
        screen.fill(WHITE)

        if archive_visible:
            draw_archive(screen, archive)
            pygame.draw.rect(screen, WHITE, back_button_rect)
            back_text = SMALL_FONT.render("Back", True, BLACK)
            screen.blit(back_text, (back_button_rect.x + 10, back_button_rect.y + 5))
        else:
            # Draw initial screen with create button and archive button
            pygame.draw.rect(screen, BLACK, button_rect, 4)
            create_text = FONT.render("+", True, BLACK)
            screen.blit(create_text, (button_rect.x + 85, button_rect.y + 10))

            pygame.draw.rect(screen, WHITE, archive_button_rect)
            archive_text = SMALL_FONT.render("Archive", True, BLACK)
            screen.blit(archive_text, (archive_button_rect.x + 10, archive_button_rect.y + 5))

            draw_key()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if archive_visible:
                    if back_button_rect and back_button_rect.collidepoint(event.pos):
                        archive_visible = False
                else:
                    if button_rect.collidepoint(event.pos):
                        calendar_visible = True
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

        if calendar_visible:
            back_button_rect = draw_calendar(screen, year, month, flip_dates)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
