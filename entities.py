import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, image, pos) -> None:
        super().__init__()
    
        self.image = image
        self.rect = self.image.get_rect(center=pos)

        self.velocity = 0

        self.jump = False

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity
        if self.velocity > 10:
            self.velocity = 10

        

        # if not self.jump:
        #     self.rect.y -= self.velocity



class Pipe(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

class Ground(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()