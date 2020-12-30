import pygame
from object_classes import Fighter
from pygame.mixer import music

from main import terminate, GAME_NAME, ICON_FILE_DIRECTORY, WINDOW_WIDTH, WINDOW_HEIGHT, \
    CONFIGURATION_FILE_DIRECTORY


# Константы:
FPS = 40

BACKGROUND_DIRECTORIES = {'background1': 'background1.jpg'}
MUSIC_DIRECTORIES = ['data/sounds/bg_music/music_one.mp3', 'data/sounds/bg_music/music_two.mp3']

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
CONTROL = [{LEFT: pygame.K_a, RIGHT: pygame.K_d, DUCK: pygame.K_s, JUMP: pygame.K_w,
            HIT: pygame.K_g, KICK: pygame.K_h, BLOCK: pygame.K_j},  # Управление первого игрока
           {LEFT: pygame.K_LEFT, RIGHT: pygame.K_RIGHT, DUCK: pygame.K_DOWN, JUMP: pygame.K_UP,
            HIT: pygame.K_1, KICK: pygame.K_2, BLOCK: pygame.K_3}]  # Управление второго игрока

music_volume = 0.4


# Считываем информацию из конфига:
with open(CONFIGURATION_FILE_DIRECTORY) as cfg:
    fighter1, fighter2, bg = cfg.readlines()
first_fighter = Fighter(fighter1)
second_fighter = Fighter(fighter2)


# Инициализация:
pygame.init()
size = WINDOW_WIDTH, WINDOW_HEIGHT
window = pygame.display.set_mode(size)
pygame.display.set_caption(GAME_NAME)
pygame.display.set_icon(pygame.image.load(ICON_FILE_DIRECTORY))

# Отрисовка фона:
background = pygame.image.load(BACKGROUND_DIRECTORIES[bg])
location = pygame.Surface(size)
location.blit(background, (0, 0))

# Музыка:
music.load(MUSIC_DIRECTORIES[0])
music.play(-1)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        pygame.MOUSEMOTION

terminate()
