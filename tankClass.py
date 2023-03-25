import pygame

#from https://www.youtube.com/watch?v=hDu8mcAlY4E
class Tank(pygame.sprite.Sprite):
    def __init__(self, width, height, tx, ty, color, lastMove):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [tx, ty]
        self.lastMove = 2

    def moveTank(self, xSpeed, ySpeed):
        self.rect.center += [xSpeed, ySpeed]