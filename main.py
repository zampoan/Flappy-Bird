import pygame
from entities import Bird, Pipe

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
BIRD_IMAGE = pygame.image.load("sprites/bluebird-downflap.png")
BACKGROUND_IMAGE = pygame.image.load("sprites/background-day.png")
BIRD_START_POS = (100, 100)


def doSprites(sprites):
    """
    Contains all relevant information all sprites
    """
    sprites.add(Bird(BIRD_IMAGE, BIRD_START_POS))

def main():
    pygame.init()
    pygame.display.set_caption('Flappy')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    sprites = pygame.sprite.Group()

    doSprites(sprites)

    running = True

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                for s in sprites:
                    s.jump = True


        screen.blit(BACKGROUND_IMAGE, (0,0))

        sprites.update()
        sprites.draw(screen)

        pygame.display.flip()

        clock.tick(30)
        

    pygame.quit()
    

if __name__ == "__main__":
    main()



