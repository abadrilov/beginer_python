import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.QUIT()
