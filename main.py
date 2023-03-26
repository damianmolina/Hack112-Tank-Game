import pygame
from tankClass import Tank
from board import GridSquare
from gameInfo import GameInfo
from bulletClass import Bullet
pygame.font.init()

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

second = 0
steps = 0
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

bullet_group = pygame.sprite.Group()
tank1BulletCount = 0
tank2BulletCount = 0
#Game info text
#Tutorial: https://www.youtube.com/watch?v=ndtFoWWBAoE
gameInfo = GameInfo()
font = pygame.font.SysFont("Arial", 24)
def printText(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

def step(steps):
    steps += 1
    return steps

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
    steps = step(steps)
    if steps % 60 == 0:
        second += 1
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
    if keys[pygame.K_LSHIFT] and tank1BulletCount < 3 and steps % 10:
        if tank1BulletCount == 0:
            bullet0 = Bullet(20, 20, tank1.x, tank1.y, 2)
            tank1Second = second
            bullet_group.add(bullet0)
            tank1BulletCount += 1
        elif second != tank1Second:
            bullet1 = Bullet(20, 20, tank1.x, tank1.y, 2)
            bullet_group.add(bullet1)
            tank1BulletCount += 1
    if keys[pygame.K_RSHIFT] and tank2BulletCount < 3:
        if tank2BulletCount == 0:
            bullet2 = Bullet(20, 20, tank2.x, tank2.y, 2)
            bullet_group.add(bullet2)
            tank2BulletCount += 1
            tank2Second = second
        elif second != tank2Second:
            bullet3 = Bullet(20, 20, tank2.x, tank2.y, 2)
            bullet_group.add(bullet3)
            tank2BulletCount += 1
    if steps % 5 == 0:
        for bullet in bullet_group:
            bullet.move()



    #draw tank
    screen.fill(bgColor)
    gridSquare_group.draw(screen)
    tank_group.draw(screen)
    pygame.draw.rect(screen, 'white', pygame.Rect(25, 125, 550, 450), 2)
    bullet_group.draw(screen)
    clock.tick(60)

pygame.quit()