import pygame
import random
from ui import Score
from entities import Bird, Pipe, Ground, Gap

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
PIPE_WIDTH = 52
PIPE_SPACING = 190  
BACKGROUND_IMAGE = random.choice([
    pygame.image.load("sprites/background-day.png"),
    pygame.image.load("sprites/background-night.png") 
    ])

CONTROL_OVERLAY = pygame.image.load("sprites/message.png")

def mainMenu(screen):
    MAIN_MENU_BACKGROUND = pygame.image.load("sprites/screenshot.png").convert_alpha()
    MAIN_MENU_BACKGROUND.set_alpha(100)
    screen.blit(MAIN_MENU_BACKGROUND, (0,0))
    screen.blit(CONTROL_OVERLAY, (60,100))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and pygame.K_SPACE:
                return


def main(screen):
    pygame.display.set_caption('Flappy')
    clock = pygame.time.Clock()

    playerSprites = pygame.sprite.Group()
    environmentSprites = pygame.sprite.LayeredUpdates()
    hitboxSprites = pygame.sprite.Group()            
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
        
        # Adds pipe and hitboxes into game
        if len(environmentSprites) < 5:
            pipePosYsetA = random.randint(200, 400)
            pipePosYsetB = random.randint(200, 400)

            pipe1 = Pipe(SCREEN_WIDTH + PIPE_WIDTH, pipePosYsetA)
            pipe2 = Pipe(SCREEN_WIDTH + PIPE_WIDTH, pipePosYsetA - 450, True)
            pipe3 = Pipe(SCREEN_WIDTH + PIPE_WIDTH + PIPE_SPACING, pipePosYsetB)
            pipe4 = Pipe(SCREEN_WIDTH + PIPE_WIDTH + PIPE_SPACING, pipePosYsetB - 450, True)
            environmentSprites.add(pipe1, pipe2, pipe3, pipe4, layer=0)
            environmentSprites.add(ground, layer=1)

            gap1 = Gap(SCREEN_WIDTH + PIPE_WIDTH, pipePosYsetA)
            gap2 = Gap(SCREEN_WIDTH + PIPE_WIDTH + PIPE_SPACING, pipePosYsetB)
            hitboxSprites.add(gap1, gap2)

        # Sets background image
        screen.blit(BACKGROUND_IMAGE, (0,0))

        # Sprite updates
        playerSprites.update()
        environmentSprites.update()
        hitboxSprites.update()
        playerSprites.draw(screen)
        environmentSprites.draw(screen)
        # hitboxSprites.draw(screen)                    # We want this invisible so we don't draw

        uiSprites.update()
        uiSprites.draw(screen)

        # When player hits pipe or ground, return to menu
        if pygame.sprite.spritecollide(bird, environmentSprites, False):
            running = False

        # When player enters scoring area, increase the score
        if pygame.sprite.spritecollide(bird, hitboxSprites, True):
            score.increaseScore()

        pygame.display.flip()

        clock.tick(30)  
        

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mainMenu(screen)
    main(screen)



