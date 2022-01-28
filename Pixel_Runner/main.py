import pygame
import sys
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(sound_volume)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = font.render(f'Score:  {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
FPS = 60
sound_volume = 0.1

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ICON_IMG = pygame.image.load('graphics/player/player_walk_1.png')
pygame.display.set_caption('Pixel Runner')
pygame.display.set_icon(ICON_IMG)
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Background music
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops=-1)
bg_music.set_volume(sound_volume)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

SKY_IMG = pygame.image.load('graphics/sky.png').convert()  # .convert makes the program faster
GROUND_IMG = pygame.image.load('graphics/ground.png').convert()

# INTRO SCREEN
PLAYER_STAND_IMG = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
PLAYER_STAND_IMG = pygame.transform.rotozoom(PLAYER_STAND_IMG, 0, 2)
player_stand_rect = PLAYER_STAND_IMG.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

game_name = font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(SCREEN_WIDTH // 2, 80))

game_message = font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70))

# TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# GAME LOOP
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == obstacle_timer:
                # 25% chance of getting a fly, 75% chance of getting a snail
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        game_active = collision_sprite()

        screen.blit(SKY_IMG, (0, 0))
        screen.blit(GROUND_IMG, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
    else:
        score_message = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70))

        screen.fill((94, 129, 162))
        screen.blit(PLAYER_STAND_IMG, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(FPS)
