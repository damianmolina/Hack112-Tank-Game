import pygame
from tankClass import Tank
from board import GridSquare
from gameInfo import GameInfo
pygame.font.init()

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

tankHeight = 25
tankWidth = 25
tank1 = Tank(tankWidth, tankHeight, 100, 350, 2)
tank2 = Tank(tankWidth, tankHeight, 500, 350, 2)

tank_group = pygame.sprite.Group()
tank_group.add(tank1)
tank_group.add(tank2)
xSpeed, ySpeed = 3, 3
bgColor = 129,152,156
screen.fill(bgColor)

#Game info text
#Tutorial: https://www.youtube.com/watch?v=ndtFoWWBAoE
gameInfo = GameInfo()
font = pygame.font.SysFont("Arial", 24)
def printText(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

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

    printText("SCORES",font,(0,0,0),253,40)
    printText(f"Player1: {gameInfo.p1score}",font,(0,0,0),250,60)
    printText(f"Player2: {gameInfo.p2score}",font,(0,0,0),250,85)

    pygame.display.flip()

    #move tank from https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and tank2.rect.center[0] - tankWidth >= 20:
        tank2.moveTank(xSpeed * -1, 0)
    if keys[pygame.K_RIGHT] and tank2.rect.center[0] + tankWidth <= 580:
        tank2.moveTank(xSpeed, 0)
    if keys[pygame.K_UP] and tank2.rect.center[1] - tankHeight > 120:
        tank2.moveTank(0, ySpeed * -1)
    if keys[pygame.K_DOWN] and tank2.rect.center[1] + tankHeight < 580:
        tank2.moveTank(0, ySpeed)
    if keys[pygame.K_a] and tank1.rect.center[0] - tankWidth >= 20:
        tank1.moveTank(xSpeed * -1, 0)
    if keys[pygame.K_d] and tank1.rect.center[0] + tankWidth <= 580:
        tank1.moveTank(xSpeed, 0)
    if keys[pygame.K_w] and tank1.rect.center[1] - tankHeight > 120:
        tank1.moveTank(0, ySpeed * -1)
    if keys[pygame.K_s] and tank1.rect.center[1] + tankHeight < 580:
        tank1.moveTank(0, ySpeed)


    #draw tank
    screen.fill(bgColor)

    gridSquare_group.draw(screen)
    tank_group.draw(screen)
    pygame.draw.rect(screen, 'white', pygame.Rect(25, 125, 550, 450), 2)
    clock.tick(60)

pygame.quit()