import pygame
import random
import os
from object_classes import Fighter, HealthBar, IMAGE_SCALE_VALUE
from pygame.mixer import music

from main import terminate, GAME_NAME, ICON_FILE_DIRECTORY, WINDOW_WIDTH, WINDOW_HEIGHT, \
    CONFIGURATION_FILE_DIRECTORY, FONT_DIRECTORY
from image_functions import text_to_surface


# Константы:
FPS = 60

BACKGROUND_DIRECTORIES = {'background1': 'data/backgrounds/background1.jpg'}
MUSIC_DIRECTORIES = ['data/sounds/bg_music/music_one.mp3', 'data/sounds/bg_music/music_two.mp3',
                     'data/sounds/bg_music/music_three.mp3']

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
CONTROL = [{LEFT: pygame.K_a, RIGHT: pygame.K_d, DUCK: pygame.K_s, JUMP: pygame.K_w,
            HIT: pygame.K_g, KICK: pygame.K_h, BLOCK: pygame.K_j},  # Управление первого игрока
           {LEFT: pygame.K_LEFT, RIGHT: pygame.K_RIGHT, DUCK: pygame.K_DOWN, JUMP: pygame.K_UP,
            HIT: pygame.K_KP_1, KICK: pygame.K_KP_2, BLOCK: pygame.K_KP_3}]  # Управление 2го игрока

fighter_width = 63 * IMAGE_SCALE_VALUE
FIGHTERS_X = [WINDOW_WIDTH // 10, WINDOW_WIDTH // 10 * 9 - fighter_width]
FIGHTERS_Y = WINDOW_HEIGHT // 7 * 3

HEALTH_BAR_INDENT = (10, 10)

FIGHT_INFO_TEXT_SIZE = 100  # Размер текста надписей "Fight!", "Player N win!"
FIGHT_INFO_TEXT_COLOR = (255, 0, 51)

music_volume = 0.05


def triggered_keys_processing(event=None, keys_status=None):
    for fighter_num, fighter_dict in enumerate(CONTROL):
        for action in fighter_dict:
            if event:
                if event.key == fighter_dict[action]:
                    if event.type == pygame.KEYDOWN:
                        fighters[fighter_num].new_action(action)
                    elif event.type == pygame.KEYUP:
                        fighters[fighter_num].stop_action(action)
            elif keys_status:
                if (keys_status[fighter_dict[action]] and
                        action not in fighters[fighter_num].get_current_actions()):
                    fighters[fighter_num].new_action(action)


# Считываем информацию из конфига:
with open(CONFIGURATION_FILE_DIRECTORY) as cfg:
    fighter1_char, fighter2_char, bg = (line for line in cfg.read().split('\n') if line.strip())

# Удаляем временный файл конфига(на время разработки отключены):
# if os.path.isfile(CONFIGURATION_FILE_DIRECTORY):
#     os.remove(CONFIGURATION_FILE_DIRECTORY)


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
music.load(random.choice(MUSIC_DIRECTORIES))
music.set_volume(music_volume)
music.play(-1)

# Группы спрайтов:
all_sprites = pygame.sprite.Group()


# Создание персонажей:
fighters = [Fighter(all_sprites, fighter1_char, (FIGHTERS_X[0], FIGHTERS_Y)),
            Fighter(all_sprites, fighter2_char, (FIGHTERS_X[1], FIGHTERS_Y))]
fighter_at_left = fighters[0]  # Персонаж, стоящий слева
fighters[1].revert()  # Поворачиваем второго игрока к центру

# Создание полосок здоровья персонажей(с координатами в данном окне):
hp_bars = [HealthBar(f'Player 1 ({fighter1_char})', True),
           HealthBar(f'Player 2 ({fighter2_char})', False)]
bars_coords = (HEALTH_BAR_INDENT,
               (WINDOW_WIDTH - hp_bars[1].get_size()[0] - HEALTH_BAR_INDENT[0], 10))

# Надпись начала битвы:
fight_info_text, text_width, text_height = text_to_surface('Fight!', FIGHT_INFO_TEXT_COLOR,
                                                           font_size=FIGHT_INFO_TEXT_SIZE,
                                                           text_shadow=True, shadow_shift=4,
                                                           font_directory=FONT_DIRECTORY,
                                                           italic=True)
fight_info_coords = ((WINDOW_WIDTH - text_width) // 2, (WINDOW_HEIGHT - text_height) // 5 * 2)

# Предварительная прорисовка:
window.blit(location, (0, 0))
all_sprites.update()
all_sprites.draw(window)
for num, bar in enumerate(hp_bars):  # Отрисовка полосок со здоровьем
    coords = bars_coords[num]
    window.blit(bar.get_surface(), coords)
window.blit(fight_info_text, fight_info_coords)  # Наложение текста на поверхность
pygame.display.flip()
clock.tick(1)  # Секунда перед началом битвы

running = True
while running:
    window.blit(location, (0, 0))
    # Отрисовка полосок со здоровьем и их обновление
    for num, bar in enumerate(hp_bars):
        coords = bars_coords[num]
        bar.update(fighters[num].get_hp())
        window.blit(bar.get_surface(), coords)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            triggered_keys_processing(event=event)
    keys_status = pygame.key.get_pressed()
    if 1 in keys_status:
        triggered_keys_processing(keys_status=keys_status)
        # Если какая-то кнопка нажата, то, возможно, персонажи двигаются
        # Тогда мы можем проверить, не поменялись ли они местами:
        if fighters[0].get_center_x() <= fighters[1].get_center_x():
            if fighter_at_left == fighters[0]:
                pass  # Персонажи повёрнуты друг к другу
            else:
                fighters[0].revert()
                fighters[1].revert()
                fighter_at_left = fighters[0]
        else:
            if fighter_at_left == fighters[0]:
                fighters[0].revert()
                fighters[1].revert()
                fighter_at_left = fighters[1]
            else:
                pass  # Персонажи повёрнуты друг к другу

    # Перерисовка спрайтов:
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.flip()
    clock.tick(FPS)
