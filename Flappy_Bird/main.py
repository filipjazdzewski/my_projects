import pygame
import sys
import random
from pygame.locals import *

def draw_ground():
    screen.blit(GROUND_IMG, (ground_x, ground_y))
    screen.blit(GROUND_IMG, (ground_x + screen_width, ground_y))

def create_pipe():
    pipe_y = random.randint(350, 700)
    bottom_pipe = PIPE_IMG.get_rect(midtop=(700, pipe_y))
    pipe_gap = 230
    top_pipe = PIPE_IMG.get_rect(midbottom=(700, pipe_y - pipe_gap))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= scroll
    visible_pipes = [pipe for pipe in pipes if pipe.x > -100]
    return visible_pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom > 900:
            screen.blit(PIPE_IMG, pipe)
        else:
            flip_pipe = pygame.transform.flip(PIPE_IMG, False, True)
            screen.blit(flip_pipe, pipe)

def collision():
    for pipe_rect in pipe_list:
        if player_rect.colliderect(pipe_rect):
            HIT_SOUND.play()
            SWOOSH_SOUND.play()
            DEATH_SOUND.play()
            return False
    if player_rect.bottom >= ground_y:
        HIT_SOUND.play()
        SWOOSH_SOUND.play()
        DEATH_SOUND.play()
        return False
    return True

def rotate_player(player):
    if player_movement < 10:
        player_angle = 20
    else:
        player_angle = -(player_movement ** 2) / 2 + 30
    if player_angle < -90:
        player_angle = -90
    rotated_player = pygame.transform.rotozoom(player, player_angle, 1)
    return rotated_player

def gain_score():
    for pipe in pipe_list:
        if pipe.centerx == player_rect.centerx:
            SCORE_SOUND.play()
            return 1
    return 0

def display_score():
    screen_score = font.render(f'{score}', False, (255, 255, 255))
    screen_score_rect = screen_score.get_rect(center=(screen_width // 2, 80))
    screen.blit(screen_score, screen_score_rect)

def display_highest_score(high_score):
    screen_high_score = font.render(f'BEST: {high_score}', False, (255, 255, 255))
    screen_score_rect = screen_high_score.get_rect(center=(screen_width // 2, screen_height - 100))
    screen.blit(screen_high_score, screen_score_rect)

'''  SETUP  '''
pygame.init()
clock = pygame.time.Clock()
score_read = open('score.txt', 'r')
FPS = 120
sound_volume = 0.5
game_active = False
scroll = 2
score = 0
highest_score = int(score_read.read())
font = pygame.font.Font('fonts/04B_19.ttf', 64)

'''  WINDOW  '''
screen_width = 574
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
icon = pygame.image.load('assets/yellowbird-midflap.png')
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

'''  SOUNDS  '''
JUMP_SOUND = pygame.mixer.Sound('sound/sfx_wing.wav')
HIT_SOUND = pygame.mixer.Sound('sound/sfx_hit.wav')
DEATH_SOUND = pygame.mixer.Sound('sound/sfx_die.wav')
SWOOSH_SOUND = pygame.mixer.Sound('sound/sfx_swooshing.wav')
SCORE_SOUND = pygame.mixer.Sound('sound/sfx_point.wav')

JUMP_SOUND.set_volume(sound_volume)
HIT_SOUND.set_volume(sound_volume)
DEATH_SOUND.set_volume(sound_volume)
SCORE_SOUND.set_volume(sound_volume)
SWOOSH_SOUND.set_volume(sound_volume)

'''  LOADING IMAGES  '''
BG_IMG = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())
GROUND_IMG = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
ground_x = 0
ground_y = screen_height - GROUND_IMG.get_height()
GET_READY_SURF = pygame.transform.rotozoom(pygame.image.load('assets/message.png').convert_alpha(), 0, 2)

PIPE_IMG = pygame.transform.rotozoom(pygame.image.load('assets/pipe-green.png').convert_alpha(), 0, 2)
pipe_list = []
SPAWN_PIPE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_PIPE, 1400)

PLAYER_UP_FLAP = pygame.transform.rotozoom(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha(), 0, 2)
PLAYER_MID_FLAP = pygame.transform.rotozoom(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha(), 0, 2)
PLAYER_DOWN_FLAP = pygame.transform.rotozoom(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha(), 0, 2)

player_frames = [PLAYER_UP_FLAP, PLAYER_MID_FLAP, PLAYER_DOWN_FLAP]
player_index = 0
wing_change = 1
PLAYER_IMG = player_frames[player_index]
player_rect = PLAYER_IMG.get_rect(center=(150, 430))

gravity = 0.3
player_movement = player_fall = 0
PLAYER_ANIMATION = pygame.USEREVENT + 2
pygame.time.set_timer(PLAYER_ANIMATION, 100)

while True:
    screen.fill((0, 0, 0))
    screen.blit(BG_IMG, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            score_write = open('score.txt', 'w')
            score_write.write(str(highest_score))
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                score_write = open('score.txt', 'w')
                score_write.write(str(highest_score))
                pygame.quit()
                sys.exit()
        if event.type == PLAYER_ANIMATION:
            PLAYER_IMG = player_frames[player_index]
            player_index += wing_change
            if player_index > 2:
                player_index -= 2
                wing_change = -1
            if player_index < 0:
                player_index += 2
                wing_change = 1
        if game_active:
            if event.type == SPAWN_PIPE:
                pipe_list.extend(create_pipe())
            if (event.type == KEYDOWN and event.key == K_SPACE) or event.type == MOUSEBUTTONDOWN:
                # jump height
                player_movement = -8.5
                JUMP_SOUND.play()
        else:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_active = True
            if event.type == MOUSEBUTTONDOWN:
                game_active = True

    if game_active:
        player_movement += gravity
        player_fall = player_movement
        if player_fall > 7:
            player_fall = 7
        player_rect.centery += player_fall
        if player_rect.centery < -100:
            player_rect.y = -100
        player_rotated = rotate_player(PLAYER_IMG)
        screen.blit(player_rotated, player_rect)
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)
        game_active = collision()
        score += gain_score()
        display_score()
    else:
        score = 0
        pipe_list.clear()
        player_rect.y = 430
        player_movement = 0
        screen.blit(PLAYER_IMG, player_rect)
        screen.blit(GET_READY_SURF, (100, 100))

    # Background has to be rendered last so it covers the pipes
    ground_x -= scroll
    draw_ground()
    if ground_x < -screen_width:
        ground_x = 0
    if score > highest_score:
        highest_score = score
    display_highest_score(highest_score)

    clock.tick(FPS)
    pygame.display.update()
