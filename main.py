import pygame
import random
from ui import Score
from entities import Bird, Pipe, Ground, Gap

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
PIPE_WIDTH = 52
PIPE_SPACING = 190
BACKGROUND_IMAGE = pygame.image.load("sprites/background-day.png")

def main():
    pygame.init()
    pygame.display.set_caption('Flappy')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playerSprites = pygame.sprite.Group()
    environmentSprites = pygame.sprite.Group()
    uiSprites = pygame.sprite.Group()

    # Sprite Activity
    bird = Bird()
    ground = Ground()
    score = Score()
    playerSprites.add(bird)
    uiSprites.add(score)

    running = True

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            # Jumping
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                for s in playerSprites: 
                    s.jump = True
        
        # Adds pipe into game
        if len(environmentSprites) < 5:
            pipePosYsetA = random.randint(200, 400)
            pipePosYsetB = random.randint(200, 400)
            pipe1 = Pipe(SCREEN_WIDTH + PIPE_WIDTH, pipePosYsetA)
            pipe2 = Pipe(SCREEN_WIDTH + PIPE_WIDTH, pipePosYsetA - 450, True)
            pipe3 = Pipe(SCREEN_WIDTH + PIPE_WIDTH + PIPE_SPACING, pipePosYsetB)
            pipe4 = Pipe(SCREEN_WIDTH + PIPE_WIDTH + PIPE_SPACING, pipePosYsetB - 450, True)
            environmentSprites.add(pipe1, pipe2, pipe3, pipe4, ground)
            
        
        screen.blit(BACKGROUND_IMAGE, (0,0))

        # Player and Environment Sprite updates
        playerSprites.update()
        environmentSprites.update()
        playerSprites.draw(screen)
        environmentSprites.draw(screen)

        # UI Sprites
        uiSprites.update()
        uiSprites.draw(screen)

        # Collision
        for bird in playerSprites:
            if pygame.sprite.spritecollide(bird, environmentSprites, False):
                # running = False
                pass

        pygame.display.flip()

        clock.tick(30)  
        

    pygame.quit()


if __name__ == "__main__":
    main()



