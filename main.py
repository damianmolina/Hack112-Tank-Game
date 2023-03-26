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
tank1 = Tank(50, 50, 200, 200, 2)

tank_group = pygame.sprite.Group()
tank_group.add(tank1)
xSpeed, ySpeed = 10, 10
screen.fill("red")

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

    gridSquare_group.draw(screen)
    tank_group.draw(screen)
    pygame.draw.rect(screen, 'white', pygame.Rect(25, 125, 550, 450), 2)
    clock.tick(60)

pygame.quit()