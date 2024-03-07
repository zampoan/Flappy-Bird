import pygame

JUMP_HEIGHT = 20
PIPE_WIDTH = 52
BIRD_START_POS = (72, 100)
GROUND_IMAGE = pygame.image.load("sprites/base.png")   
PIPE_IMAGE = pygame.image.load("sprites/pipe-green.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.sprites = [
                        pygame.image.load("sprites/bluebird-downflap.png"),
                        pygame.image.load("sprites/bluebird-midflap.png"),
                        pygame.image.load("sprites/bluebird-upflap.png")
                        ]
        self.currentSprite = 0
    
        self.originalImage = self.sprites[self.currentSprite]
        self.rect = self.originalImage.get_rect() 
        self.rect.center = BIRD_START_POS

        self.velocity = 0

        self.jump = False
        
        self.angle = 0


    def update(self):
        # Update sprite animation
        self.currentSprite += 1
        self.originalImage = self.sprites[self.currentSprite]
        if self.currentSprite > len(self.sprites) - 2:
            self.currentSprite = 0

        # Gravity
        self.velocity += 1
        self.rect.y += self.velocity
        
        # Cap fall velocity
        if self.velocity > 10:
            self.velocity = 10

        # When performing a jump
        if self.jump == True:
            self.velocity -= JUMP_HEIGHT
            self.jump = False

        # Sprite rotates forward when falling down, rotates backward when jumping
        if self.velocity > 0:
            if self.angle < -20:
                self.angle = -20
            self.angle -= 2

        elif self.velocity < 0:
            if self.angle > 20:
                self.angle = 20
            self.angle += 2

        self.image = pygame.transform.rotate(self.originalImage, self.angle)
            

class Ground(pygame.sprite.Sprite):
    def __init__(self, x=0, y=400) -> None:
        super().__init__()
        self.image = GROUND_IMAGE
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)


class Pipe(pygame.sprite.Sprite):
    """
    How Pipe Works: 
        - Always max four on screen, two miniumum
        - Have 450 pixels difference
    """
    def __init__(self, x, y, inverted=False) -> None:
        super().__init__()
        self.image = PIPE_IMAGE
        self.invertedImage = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        
        self.speed = 5

        self.rect.topleft = (x, y)

        self.inverted = inverted


    def update(self):
        self.rect.x -= self.speed

        # Invert the image
        if self.inverted:
            self.image = self.invertedImage
        else:
            self.image = PIPE_IMAGE

        # Kill when it gets off screen
        if self.rect.x < -PIPE_WIDTH:
            self.kill()


class Gap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, 150))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < -PIPE_WIDTH:
            self.kill()

