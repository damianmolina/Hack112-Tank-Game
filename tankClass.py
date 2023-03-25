import pygame

#from https://www.youtube.com/watch?v=hDu8mcAlY4E
class Tank(pygame.sprite.Sprite):
    def __init__(self, width, height, tx, ty, color, lastMove):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = tx
        self.y = ty
        self.rect.center = [self.x, self.y]
        self.lastMove = 2

    def moveTank(self, xSpeed, ySpeed):
        self.x += xSpeed
        self.y += ySpeed
        self.rect.center = [self.x, self.y]
        pygame.display.update()