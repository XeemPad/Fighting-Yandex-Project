import pygame


def load_image(directory_name, colorkey=None):
    import os

    if not os.path.isfile(directory_name):
        raise FileNotFoundError(f"Файл с изображением '{directory_name}' не найден")
    image = pygame.image.load(directory_name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def text_to_surface(text, text_color=(255, 255, 255), font_size=50):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_w = text_surface.get_width()
    text_h = text_surface.get_height()
    return text_surface, text_w, text_h
