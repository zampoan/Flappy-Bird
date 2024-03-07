import pygame

SCORE_START_POS = (144, 50)

class Score(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.sprites = [
            pygame.image.load("sprites/0.png"),
            pygame.image.load("sprites/1.png"),
            pygame.image.load("sprites/2.png"),
            pygame.image.load("sprites/3.png"),
            pygame.image.load("sprites/4.png"),
            pygame.image.load("sprites/5.png"),
            pygame.image.load("sprites/6.png"),
            pygame.image.load("sprites/7.png"),
            pygame.image.load("sprites/8.png"),
            pygame.image.load("sprites/9.png")
        ]
        self.score = 0
        self.scoreIdx = 0

        self.image = self.sprites[self.scoreIdx]
        self.rect = self.image.get_rect()
        self.rect.center = SCORE_START_POS

    def increaseScore(self):
        self.score += 1
        self.scoreIdx += 1
        
        # Double digits
        if self.score > 9:
            self.scoreIdx = 1

        self.image = self.sprites[self.scoreIdx]
       