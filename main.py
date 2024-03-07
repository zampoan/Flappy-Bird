import pygame
from entities import Bird, Pipe, Ground

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
BACKGROUND_IMAGE = pygame.image.load("sprites/background-day.png")

def main():
    pygame.init()
    pygame.display.set_caption('Flappy')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playerSprites = pygame.sprite.Group()
    environmentSprites = pygame.sprite.Group()

    # Sprite Activity
    bird = Bird()
    ground = Ground()
    pipe1 = Pipe(100, 350)
    pipe2 = Pipe(100, -100, True)
    playerSprites.add(bird)
    environmentSprites.add(pipe1, pipe2, ground)

    running = True

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            # Jumping
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                for s in playerSprites: 
                    s.jump = True


        screen.blit(BACKGROUND_IMAGE, (0,0))

        # Sprite updates
        playerSprites.update()
        environmentSprites.update()
        playerSprites.draw(screen)
        environmentSprites.draw(screen)

        # Collision
        for bird in playerSprites:
            if pygame.sprite.spritecollide(bird, environmentSprites, False):
                pass
            else:
                pass
        print(environmentSprites)

        pygame.display.flip()

        clock.tick(30)
        

    pygame.quit()
    

if __name__ == "__main__":
    main()



