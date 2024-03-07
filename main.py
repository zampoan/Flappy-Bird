import pygame
from entities import Bird, Pipe, Ground

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
BACKGROUND_IMAGE = pygame.image.load("sprites/background-day.png")
GROUND_IMAGE = pygame.image.load("sprites/base.png")   

def main():
    pygame.init()
    pygame.display.set_caption('Flappy')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playerSprites = pygame.sprite.Group()
    environmentSprites = pygame.sprite.Group()

    # Sprite Activity
    bird = Bird()
    ground = Ground(GROUND_IMAGE, 0, 400)
    playerSprites.add(bird)
    environmentSprites.add(ground)

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

        playerSprites.update()
        environmentSprites.update()
        playerSprites.draw(screen)
        environmentSprites.draw(screen)

        # Collision
        for bird in playerSprites:
            if pygame.sprite.spritecollide(bird, environmentSprites, False):
                print('HIT!')
            else:
                print('NO HIT!')


        pygame.display.flip()

        clock.tick(30)
        

    pygame.quit()
    

if __name__ == "__main__":
    main()



