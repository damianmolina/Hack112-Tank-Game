import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, width, height, tx, ty, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()