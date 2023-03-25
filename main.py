import pygame

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


#from https://www.pygame.org/docs/
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()