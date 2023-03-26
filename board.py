import pygame, random

class GridSquare(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos):
        super().__init__()
        cX = 50 + 50 * xPos
        cY = 150 + 50 * yPos
        self.xPos = xPos
        self.yPos = yPos
        self.width = 50
        self.height = 50
        odds = [0,0,0,1]
        if random.choice(odds) and (xPos,yPos)!=(1,4) and (xPos,yPos)!=(9,4):
            self.isWall = True
        else: self.isWall = False
        if self.isWall:
            self.image = pygame.image.load('bighole.jpg')
        else: 
            self.image = pygame.image.load("grass.jpg")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (cX, cY)
    
    def __eq__ (self, other):
        if not isinstance(other, GridSquare): return False
        else:
            return self.xPos == other.xPos and self.yPos == other.yPos
        
    def __repr__(self):
        return f"Square at ({self.xPos}, {self.yPos})"
    
    def __hash__(self):
        return hash(repr(self))