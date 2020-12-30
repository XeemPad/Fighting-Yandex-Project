# This file contains code of game menu
import pygame
import subprocess
import sys
from image_functions import load_image, text_to_surface
from object_classes import Button


# Константы:
GAME_NAME = 'Kind of Fighting'
WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 576
FPS = 40

ICON_FILE_DIRECTORY = 'data/icon.ico'
MENU_BACKGROUND_DIRECTORY = 'data/menu_background.png'
MENU_MUSIC_DIRECTORY = 'data/sounds/menu_music.mp3'
CONFIGURATION_FILE_DIRECTORY = 'info.txt'
GAME_LAUNCH_DIRECTORY = 'launch_game.py'

BUTTON_TEXT_COLOR = (51, 255, 51)
BUTTON_TEXT_SIZE = 70
BUTTONS_SIZE = (200, 80)
TITLE_TEXT_COLOR = (255, 255, 0)


music_volume = 0.4


def terminate():
    pygame.quit()
    exit()


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fighting')
pygame.display.set_icon(pygame.image.load(ICON_FILE_DIRECTORY))


def start_game():
    # Данные о поле боя:
    with open(CONFIGURATION_FILE_DIRECTORY, 'w') as cfg:
        first_fighter = 'scorpion'
        second_fighter = 'scorpion'
        background = 'background1'
        for line in [first_fighter, second_fighter, background]:
            cfg.write(line + '\n')
    # Запуск скрипта с игровым процессом:
    subprocess.Popen([sys.executable, GAME_LAUNCH_DIRECTORY])
    terminate()


def game_menu():
    # Загрузка музыки для главного меню:
    pygame.mixer.music.load(MENU_MUSIC_DIRECTORY)
    pygame.mixer.music.set_volume(music_volume)
    pygame.mixer.music.play(-1)
    # Установка фона в меню:
    try:
        bg_image = load_image(MENU_BACKGROUND_DIRECTORY)
    except FileNotFoundError as error:
        print(error)
        terminate()
    background = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(background, (0, 0))

    # Установка названия игры в меню:
    font_size = 96
    title, title_width, title_height = text_to_surface(GAME_NAME, TITLE_TEXT_COLOR,
                                                       font_size=font_size, text_shadow=True)
    title_x, title_y = (WINDOW_WIDTH - title_width) // 2, (WINDOW_HEIGHT - title_height) // 10
    screen.blit(title, (title_x, title_y))  # А теперь и само название

    # Создание кнопок:
    buttons_y = WINDOW_HEIGHT // 5 * 2
    buttons_distance = 30
    btn_w, btn_h = BUTTONS_SIZE
    buttons = []
    # Кнопка запуска игры:
    play_text = text_to_surface('Играть', BUTTON_TEXT_COLOR, BUTTON_TEXT_SIZE,
                                text_shadow=True, shadow_shift=4)[0]
    play_btn = Button(play_text, width=btn_w, height=btn_h, function=start_game)
    play_btn.set_pos(((WINDOW_WIDTH - btn_w) // 2, buttons_y))
    buttons.append(play_btn)
    # Кнопка выхода:
    exit_text = text_to_surface('Выйти', BUTTON_TEXT_COLOR, BUTTON_TEXT_SIZE,
                                text_shadow=True, shadow_shift=4)[0]
    exit_btn = Button(exit_text, width=btn_w, height=btn_h, function=terminate)
    exit_btn.set_pos(((WINDOW_WIDTH - btn_w) // 2, buttons_y + btn_h + buttons_distance))
    buttons.append(exit_btn)

    # Отрисовка кнопок:
    for btn in buttons:
        btn_surface = btn.get_surface()
        btn_pos = btn.get_pos()
        screen.blit(btn_surface, btn_pos)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                for btn in buttons:
                    if btn.check_mouse_position(event.pos):
                        btn.set_under_mouse_effect()
                    else:
                        btn.set_under_mouse_effect(False)
                    # Перерисовка нового вида кнопки:
                    screen.blit(btn.get_surface(), btn.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in buttons:
                    if btn.check_mouse_position(event.pos):
                        btn.trigger()

        pygame.display.flip()
        clock.tick(FPS)


game_menu()
