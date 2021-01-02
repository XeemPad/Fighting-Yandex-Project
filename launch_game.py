import pygame
from object_classes import Fighter
from pygame.mixer import music
from object_classes import IMAGE_SCALE_VALUE

from main import terminate, GAME_NAME, ICON_FILE_DIRECTORY, WINDOW_WIDTH, WINDOW_HEIGHT, \
    CONFIGURATION_FILE_DIRECTORY


# Константы:
FPS = 40

BACKGROUND_DIRECTORIES = {'background1': 'data/backgrounds/background1.jpg'}
MUSIC_DIRECTORIES = ['data/sounds/bg_music/music_one.mp3', 'data/sounds/bg_music/music_two.mp3']

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
CONTROL = [{LEFT: pygame.K_a, RIGHT: pygame.K_d, DUCK: pygame.K_s, JUMP: pygame.K_w,
            HIT: pygame.K_g, KICK: pygame.K_h, BLOCK: pygame.K_j},  # Управление первого игрока
           {LEFT: pygame.K_LEFT, RIGHT: pygame.K_RIGHT, DUCK: pygame.K_DOWN, JUMP: pygame.K_UP,
            HIT: pygame.K_1, KICK: pygame.K_2, BLOCK: pygame.K_3}]  # Управление второго игрока

fighter_width = 63 * IMAGE_SCALE_VALUE
FIGHTERS_X = [WINDOW_WIDTH // 10, WINDOW_WIDTH // 10 * 9 - fighter_width]
FIGHTERS_Y = WINDOW_HEIGHT // 7 * 3

music_volume = 0.05


def triggered_keys_processing(event):
    for fighter_num, fighter_dict in enumerate(CONTROL):
        for key in fighter_dict:
            if event.key == fighter_dict[key]:
                if event.type == pygame.KEYDOWN:
                    fighters[fighter_num].new_action(key)
                elif event.type == pygame.KEYUP:
                    fighters[fighter_num].stop_action(key)


# Считываем информацию из конфига:
with open(CONFIGURATION_FILE_DIRECTORY) as cfg:
    fighter1, fighter2, bg = (line for line in cfg.read().split('\n') if line.strip())


# Инициализация:
pygame.init()
size = WINDOW_WIDTH, WINDOW_HEIGHT
window = pygame.display.set_mode(size)
pygame.display.set_caption(GAME_NAME)
pygame.display.set_icon(pygame.image.load(ICON_FILE_DIRECTORY))
clock = pygame.time.Clock()

# Загрузка фона:
background = pygame.image.load(BACKGROUND_DIRECTORIES[bg])
location = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Музыка:
music.load(MUSIC_DIRECTORIES[0])
music.set_volume(music_volume)
music.play(-1)

# Группы спрайтов:
all_sprites = pygame.sprite.Group()


# Создание персонажей:
fighters = [Fighter(all_sprites, fighter1, (FIGHTERS_X[0], FIGHTERS_Y)),
            Fighter(all_sprites, fighter2, (FIGHTERS_X[1], FIGHTERS_Y))]

fighters[1].revert()  # Поворачиваем второго игрока к центру


running = True
while running:
    window.blit(location, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            triggered_keys_processing(event)
    # Перерисовка спрайтов:
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.flip()
    clock.tick(FPS)
