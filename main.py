import pygame
from tankClass import Tank
from board import GridSquare

# Constant stuff
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
tankHeight = 25
tankWidth = 25

def isCollision(tank):
    # Checking if collision with white border
    if (tank.x - tankWidth < 25):
        tank.x = tankWidth + 25
        return True
    elif (tank.x + tankWidth > 575):
        tank.x = 575 - tankWidth
        return True
    elif (tank.y - tankHeight < 125):
        tank.y = 125 + tankHeight
        return True
    elif (tank.y + tankHeight > 575):
        tank.y = 575 - tankHeight
        return True
    else:
        return False



# Creation of tank
tank1 = Tank(50, 50, 200, 200, 2)

tank_group = pygame.sprite.Group()
tank_group.add(tank1)
xSpeed, ySpeed = 10, 10
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

    #move tank from https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not isCollision(tank1):
        tank1.moveTank(xSpeed * -1, 0)
    elif keys[pygame.K_RIGHT] and not isCollision(tank1):
        tank1.moveTank(xSpeed, 0)
    elif keys[pygame.K_UP] and not isCollision(tank1):
        tank1.moveTank(0, ySpeed * -1)
    elif keys[pygame.K_DOWN] and not isCollision(tank1):
        tank1.moveTank(0, ySpeed)

    #draw tank
    screen.fill("red")

    gridSquare_group.draw(screen)
    tank_group.draw(screen)
    pygame.draw.rect(screen, 'white', pygame.Rect(25, 125, 550, 450), 2)
    clock.tick(60)

pygame.quit()