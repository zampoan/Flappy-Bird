import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the display (replace with your desired dimensions)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image after initializing the display
MAIN_MENU_BACKGROUND = pygame.image.load("sprites/screenshot.png").convert_alpha()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the image on the screen
    screen.blit(MAIN_MENU_BACKGROUND, (0, 0))
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
