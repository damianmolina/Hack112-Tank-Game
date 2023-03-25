import pygame, random

class GridSquare(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos):
        super().__init__()
        cX = 50 + 50 * xPos
        cY = 150 + 50 * yPos
        self.width = 50
        self.height = 50
        odds = [0,0,0,0,1]
        if random.choice(odds):
            self.isWall = True
        else: self.isWall = False
        if self.isWall: color = "blue"
        else: color = "red"
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (cX, cY)
