import pygame
class Bullet(pygame.sprite.Sprite):

    bulletList = []
    def __init__(self, width, height, color, cx, cy, dir):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center=[cx, cy]
        self.dir = dir
        self.hasBounced = False
        self.steps = 0
        self.destroy = False
        
    
    def __repr__(self):
        return f'Bullet(cx={self.cx}, cy={self.cy})'
    
    def __eq__(self, other):
        return (isinstance(other, Bullet) and 
                self.cx == other.cx and 
                self.cy == other.cy)
    
    def move(self):
        if self.dir == 1:
            if self.steps % 2:
                self.rect.center[0] -= 1
            else:
                self.rect.center[1] -= 1
        elif self.dir == 2:
            self.rect.center[1] -= 1
        elif self.dir == 3:
            if self.steps % 2:
                self.rect.center[0] += 1
            else:
                self.rect.center[1] -= 1
        elif self.dir == 4:
            self.rect.center[0] -= 1
        elif self.dir == -4:
            self.rect.center[0] += 1
        elif self.dir == -1:
            if self.steps % 2:
                self.rect.center[0] -= 1
            else:
                self.rect.center[1] += 1
        elif self.dir == -2:
            self.rect.center[1] += 1
        else:
            if self.steps % 2:
                self.rect.center[0] += 1
            else:
                self.rect.center[1] += 1
    
    def step(self):
        self.steps += 1
        self.move()
    
    def bounce(self):
        if not self.hasBounced:
            self.dir = -self.dir
            self.hasBounced = True
        else:
            self.destroy = True
    