import pygame
from tankClass import Tank

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

tank1 = Tank(50, 50, 200, 200, (255,255,255))
tank_group = pygame.sprite.Group()
tank_group.add(tank1)

#from https://www.pygame.org/docs/
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    tank_group.draw(screen)

    clock.tick(60)


pygame.quit()