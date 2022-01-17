import pygame  # ctrl + alt + l - optimizes your code (looks neater)
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Background
background = pygame.image.load('images/background.jpg')

# Background Sound
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load('images/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
max_num_of_enemies = 14
speed_increase = 0

for i in range(max_num_of_enemies):
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)
    if i % 2 == 0:
        enemyIMG.append(pygame.image.load('images/enemy1.png'))
    else:
        enemyIMG.append(pygame.image.load('images/enemy2.png'))

# Bullet
# Ready - you can't see bullet on the screen
# Fire - The bullet is currently moving
bulletIMG = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score Text
score_value = 0
score_font = pygame.font.Font('fonts/arcade.TTF', 32)
scoreX = 10
scoreY = 10

# Game Over
game_over_font = pygame.font.Font('fonts/arcade.TTF', 80)
g_overX = 50
g_overY = 250
death_range = 440
game_is_over = False


def player(x, y):
    WINDOW.blit(playerIMG, (x, y))


def enemy(x, y, enemy_id):
    WINDOW.blit(enemyIMG[enemy_id], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    WINDOW.blit(bulletIMG, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = score_font.render('SCORE:' + str(score_value), True, (255, 255, 255))
    WINDOW.blit(score, (x, y))


def game_over_text(x, y):
    game_over = game_over_font.render('GAME OVER', True, (255, 255, 255))
    WINDOW.blit(game_over, (x, y))
    global game_is_over
    game_is_over = True


FPS = 60
clock = pygame.time.Clock()

# GAME LOOP
running = True
while running:
    clock.tick(FPS)
    # RGB - Red, Green, Blue
    WINDOW.fill((0, 0, 0))
    # Background Image
    WINDOW.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # the keystroke is pressed
            if event.key == pygame.K_ESCAPE:
                running = False
            if not game_is_over:
                if event.key == pygame.K_LEFT:
                    playerX_change = -7
                if event.key == pygame.K_RIGHT:
                    playerX_change = 7
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('sounds/laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # the keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of the player spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > death_range:
            for j in range(num_of_enemies):
                # Enemy disappears out of screen
                enemyY[j] = 2000
            game_over_text(g_overX, g_overY)
            show_score(g_overX + 230, g_overY + 90)
            break
        else:
            player(playerX, playerY)
            show_score(scoreX, scoreY)

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4 + speed_increase
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4 - speed_increase
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            score_value += 1
            # Increases speed value by 1 for every 10 score (adds it to enemy speed)
            if score_value % 15 == 0 and num_of_enemies <= max_num_of_enemies:
                num_of_enemies += 1
            if score_value % 10 == 0:
                speed_increase += 0.8

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= -40:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    pygame.display.update()
