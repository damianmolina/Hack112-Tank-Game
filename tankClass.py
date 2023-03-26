import pygame

#from https://www.youtube.com/watch?v=hDu8mcAlY4E
class Tank(pygame.sprite.Sprite):

    def __init__(self, width, height, tx, ty, lastMove, health):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("tankRight.png")
        self.rect = self.image.get_rect()
        self.x = tx
        self.health = health
        self.y = ty
        self.rect.center = [self.x, self.y]
        self.lastMove = 2

    def moveTank(self, xSpeed, ySpeed):
        if (xSpeed > 0):
            self.image = pygame.image.load("tankRight.png")
        elif (xSpeed < 0):
            self.image = pygame.image.load("tankLeft.png")
        elif (ySpeed > 0):
            self.image = pygame.image.load("tankUp.png")
        elif (ySpeed < 0):
            self.image = pygame.image.load("tankDown.png")
        self.x += xSpeed
        self.y += ySpeed
        self.rect.center = [self.x, self.y]
        pygame.display.update()