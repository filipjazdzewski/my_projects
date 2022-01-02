import pygame
import os
import time
import random

pygame.init()

# WINDOW
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')

# LOAD IMAGES
# Player Spaceship
YELLOW_SPACE_SHIP = pygame.image.load('assets/pixel_ship_yellow.png')

# Enemy Spaceships
RED_SPACE_SHIP = pygame.image.load('assets/pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load('assets/pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load('assets/pixel_ship_blue_small.png')

# Lasers
YELLOW_LASER = pygame.image.load('assets/pixel_laser_yellow.png')
RED_LASER = pygame.image.load('assets/pixel_laser_red.png')
GREEN_LASER = pygame.image.load('assets/pixel_laser_green.png')
BLUE_LASER = pygame.image.load('assets/pixel_laser_blue.png')

# Background
BG_IMG = pygame.image.load('assets/background-black.png')
BG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))  # Scales the IMG so it fills the entire screen


class Ship:
    def __init__(self, x, y, color, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0


run = True
FPS = 60
level = 1
lives = 5
main_font = pygame.font.Font('fonts/arcade.ttf', 20)

clock = pygame.time.Clock()


def redraw_window():
    WIN.blit(BG, (0, 0))
    # draw text
    lives_label = main_font.render(f'Lives: {lives}', True, (255, 255, 255))
    level_label = main_font.render(f'Level: {level}', True, (255, 255, 255))

    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    pygame.display.update()


# GAME LOOP
while run:
    clock.tick(FPS)
    redraw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
