import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class MovingSquare(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.size = 100
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, BLACK, (0, 0, self.size, self.size), 2)
        pygame.draw.line(self.image, BLACK, (self.size // 2, 0), (self.size // 2, self.size), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed
        # Reset the square position if it goes off the screen
        if self.rect.right <= 0:
            self.rect.left = 800

def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Square with Line")

    all_sprites = pygame.sprite.Group()
    moving_square = MovingSquare(screen_width, screen_height)
    all_sprites.add(moving_square)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill(WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
