import pygame
from tankClass import Tank
from board import GridSquare

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

tank1 = Tank(25, 25, 200, 200, (255,255,255))
tank_group = pygame.sprite.Group()
tank_group.add(tank1)
screen.fill("red")

gridSquare_group = pygame.sprite.Group()
walls = dict()
for x in range(11):
    for y in range(9):
        currSquare = GridSquare(x, y)
        gridSquare_group.add(currSquare)
        walls[(x,y)] = currSquare.isWall

#from https://www.pygame.org/docs/
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    tank_group.draw(screen)

    gridSquare_group.draw(screen)

    pygame.draw.rect(screen, "white", pygame.Rect(25,125,550,450), 2)

    clock.tick(60)

pygame.quit()