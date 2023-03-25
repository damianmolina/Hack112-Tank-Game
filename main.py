import pygame
from tankClass import Tank

pygame.init()

#screen init
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
screen.fill("red")

#tank group
tankWidth, tankHeight = 50, 50
tank1 = Tank(tankWidth, tankHeight, 200, 200, (255,255,255), 2)
tank_group = pygame.sprite.Group()
tank_group.add(tank1)
xSpeed, ySpeed = 10, 10

#from https://www.pygame.org/docs/
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

    #move tank from https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank1.rect.center[0] - tankWidth >= 0:
        tank1.moveTank(xSpeed * -1, 0)
    elif keys[pygame.K_RIGHT] and tank1.rect.center[0] + tankWidth <= width:
        tank1.moveTank(xSpeed, 0)
    elif keys[pygame.K_UP] and tank1.rect.center[1] - tankHeight > 0:
        tank1.moveTank(0, ySpeed * -1)
    elif keys[pygame.K_DOWN] and tank1.rect.center[1] + tankHeight < height:
        tank1.moveTank(0, ySpeed)

    #draw tank
    screen.fill("red")
    tank_group.draw(screen)

    clock.tick(60)

pygame.quit()