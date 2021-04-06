import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((400, 400))
FPS = 50

YALLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREY = (192, 192, 192)

screen.fill((GREY))

circle(screen, YALLOW, (200, 157), 100)
circle(screen, BLACK, (200, 157, 6)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()