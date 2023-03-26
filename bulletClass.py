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
        self.dx, self.dy = 0, -1
        self.hasBounced = 0
        self.steps = 0
        self.destroy = False
        if dir == 1:
            self.dx, self.dy = -1, -1
        if dir == 3:
            self.dx, self.dy = 1, -1
        if dir == 4:
            self.dx, self.dy = -1, 0
        if dir == -4:
            self.dx, self.dy = 1, 0
        if dir == -1:
            self.dx, self.dy = -1, 1
        if dir == -3:
            self.dx, self.dy = 1, 1
        if dir == -2:
            self.dx, self.dy = 0, 1
        
    
    def __repr__(self):
        return f'Bullet(cx={self.rect.center[0]}, cy={self.rect.center[1]})'
    
    # def __eq__(self, other):
    #     return (isinstance(other, Bullet) and 
    #             self.rect.center[0] == other.rect.center[0] and 
    #             self.rect.center[1] == other.rect.center[1])
    
    # def __hash__(self):
    #     return hash(str(self))
    
    def move(self, dx, dy):
        self.cx += 20 * dx
        self.cy += 20 * dy
        self.rect.center = [self.cx, self.cy]
    
    def bounce(self, dirCall):
        if self.hasBounced < 2:
            if dirCall == "TB":
                self.dy = -self.dy
            else:
                self.dx = -self.dx
            self.hasBounced += 1
        else:
            pygame.sprite.Sprite.kill(self)
    