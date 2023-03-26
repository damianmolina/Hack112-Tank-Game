import pygame
class Bullet(pygame.sprite.Sprite):

    bulletList = []
    def __init__(self, width, height, cx, cy, dir):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.center=[cx, cy]
        self.cx =  cx
        self.cy = cy
        self.dir = dir
        self.hasBounced = False
        self.steps = 0
        self.destroy = False
        if dir == 1:
            self.image = pygame.transform.rotate(self.image, 45)
        if dir == 3:
            self.image = pygame.transform.rotate(self.image, -45)
        if dir == 4:
            self.image = pygame.transform.rotate(self.image, 90)
        if dir == -4:
            self.image = pygame.transform.rotate(self.image, -90)
        if dir == -1:
            self.image = pygame.transform.rotate(self.image, 135)
        if dir == -3:
            self.image = pygame.transform.rotate(self.image, -135)
        if dir == -2:
            self.image = pygame.transform.rotate(self.image, 180)
        
    
    def __repr__(self):
        return f'Bullet(cx={self.rect.center[0]}, cy={self.rect.center[1]})'
    
    def __eq__(self, other):
        return (isinstance(other, Bullet) and 
                self.rect.center[0] == other.rect.center[0] and 
                self.rect.center[1] == other.rect.center[1])
    
    def __hash__(self):
        return hash(str(self))
    
    def move(self):
        self.steps += 1
        if self.dir == 1:
            if self.steps % 2:
                self.cx -= 1
            else:
                self.cy -= 1
        elif self.dir == 2:
            self.cy -= 1
        elif self.dir == 3:
            if self.steps % 2:
                self.cx += 1
            else:
                self.cy -= 1
        elif self.dir == 4:
            self.cx -= 1
        elif self.dir == -4:
            self.cx += 1
        elif self.dir == -1:
            if self.steps % 2:
                self.cx -= 1
            else:
                self.cy += 1
        elif self.dir == -2:
            self.cy += 1
        else:
            if self.steps % 2:
                self.cx += 1
            else:
                self.cy += 1
        self.rect.center = [self.cx, self.cy]
    

    
    def bounce(self):
        if not self.hasBounced:
            self.dir = -self.dir
            self.hasBounced = True
        else:
            self.destroy = True
        self.image = pygame.Surface([20, 20])
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        if dir == 1:
            self.image = pygame.transform.rotate(self.image, 45)
        if dir == 3:
            self.image = pygame.transform.rotate(self.image, -45)
        if dir == 4:
            self.image = pygame.transform.rotate(self.image, 90)
        if dir == -4:
            self.image = pygame.transform.rotate(self.image, -90)
        if dir == -1:
            self.image = pygame.transform.rotate(self.image, 135)
        if dir == -3:
            self.image = pygame.transform.rotate(self.image, -135)
        if dir == -2:
            self.image = pygame.transform.rotate(self.image, 180)