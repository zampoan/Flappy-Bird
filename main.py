import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BIRD_IMAGE = "sprites/bluebird-downflap.png"

class Bird(pygame.sprite.Sprite):
    def __init__(self, image) -> None:
        super().__init__()
        self.image = image


class Pipe(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

def doSprites(sprites):
    """
    Contains all relevant information all sprites
    """
    sprites.add(Bird(BIRD_IMAGE))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    sprites = pygame.sprite.Group()

    doSprites(sprites)

    running = True

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False


            screen.fill('black')
            pygame.display.flip()

    pygame.quit()
    

if __name__ == "__main__":
    main()



