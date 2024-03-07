import pygame

JUMP_HEIGHT = 20
BIRD_START_POS = (100, 100) 
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
    def __init__(self, image, x, y) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)

class Pipe(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()