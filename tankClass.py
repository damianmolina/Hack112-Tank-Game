import pygame

#from https://www.youtube.com/watch?v=hDu8mcAlY4E
class Tank(pygame.sprite.Sprite):
    def __init__(self, width, height, tx, ty):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("tankBase.png")
        self.rect = self.image.get_rect()
        self.rect.center = [tx, ty]