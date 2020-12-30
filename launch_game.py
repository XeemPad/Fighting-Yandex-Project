import pygame
from object_classes import Fighter
from pygame.mixer import music

from main import terminate, GAME_NAME, ICON_FILE_DIRECTORY, WINDOW_WIDTH, WINDOW_HEIGHT, \
    CONFIGURATION_FILE_DIRECTORY


# Константы:
FPS = 40

BACKGROUND_DIRECTORIES = {'background1': 'background1.jpg'}
MUSIC_DIRECTORIES = ['data/sounds/bg_music/music_one.mp3', 'data/sounds/bg_music/music_two.mp3']

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
    pass

terminate()
