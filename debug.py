import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Drop")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the gravity
GRAVITY = 0.5

# Define the sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), 0)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        if self.rect.top > HEIGHT:
            self.kill()

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a sprite to the sprite group when clicked
            new_sprite = Sprite()
            all_sprites.add(new_sprite)
            print("Number of sprites:", len(all_sprites))

    # Update sprites
    all_sprites.update()

    # Draw sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
