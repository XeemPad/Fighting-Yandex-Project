# This file contains code of game menu
import pygame
from image_functions import load_image, text_to_surface


GAME_NAME = 'Kind of Fighting'
WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 576
FPS = 40

ICON_FILE_DIRECTORY = 'data/icon.ico'
MENU_BACKGROUND_DIRECTORY = 'data/menu_background.png'


def terminate():
    pygame.quit()
    exit()


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fighting')
pygame.display.set_icon(pygame.image.load(ICON_FILE_DIRECTORY))


def game_menu_launch():
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
    title, title_width, title_height = text_to_surface(GAME_NAME, (255, 255, 0),
                                                       font_size=font_size)
    title_x, title_y = (WINDOW_WIDTH - title_width) // 2, (WINDOW_HEIGHT - title_height) // 10
    shadow_for_title, shadow_width, shadow_height = text_to_surface(GAME_NAME, (0, 0, 0),
                                                                    font_size=font_size)
    shadow_x, shadow_y = title_x + 4, title_y + 4
    screen.blit(shadow_for_title, (shadow_x, shadow_y))  # Рисуем тень
    screen.blit(title, (title_x, title_y))  # А теперь и само название

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


game_menu_launch()
