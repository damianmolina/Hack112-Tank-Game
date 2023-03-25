import pygame

class GridSquare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.topLeftX = 25
        self.topLeftY = 125
        self.width = 550
        self.height = 450