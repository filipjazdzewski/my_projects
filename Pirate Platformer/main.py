import pygame, sys
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

FPS = 60
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)
