import pygame
from sys import exit
import random

# ctrl + /   - comments

pygame.init()
# GAME
game_active = True

# WINDOW
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Running Dinosaur')

# FONT
font = pygame.font.Font('font/Pixeltype.ttf', 50)
# score_text = font.render('My Game', False, (64, 64, 64))
# score_rect = score_text.get_rect(center=(400, 50))

# LOADING IMAGES
SKY_IMG = pygame.image.load('graphics/sky.png').convert()  # .convert makes the program faster
GROUND_IMG = pygame.image.load('graphics/ground.png').convert()

# ENEMY
SNAIL_IMG = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # add _alpha so the image is transparent
snail_rect = SNAIL_IMG.get_rect(midbottom=(600, 300))

# PLAYER
PLAYER_IMG = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = PLAYER_IMG.get_rect(midbottom=(80, 300))
player_gravity = 0

# FPS
FPS = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        screen.blit(SKY_IMG, (0, 0))
        screen.blit(GROUND_IMG, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_text, score_rect)

        snail_rect.left -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(SNAIL_IMG, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(PLAYER_IMG, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(FPS)
