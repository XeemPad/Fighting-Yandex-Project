import pygame


SHADOW_SHIFT = 4
SHADOW_COLOR = (0, 0, 0)


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


def text_to_surface(text, text_color=(255, 255, 255), border_color=None, font_size=50, text_shadow=False,
                    shadow_shift=SHADOW_SHIFT, border_width=1, font_directory=None):
    font = pygame.font.Font(font_directory, font_size)
    text_surface = font.render(text, True, text_color)
    if border_color:
        border_font = pygame.font.Font(font_directory, font_size + border_width)
        border_text = border_font.render(text, True, border_color)
    else:
        border_width = 0
    text_w = border_text.get_width() if border_width else text_surface.get_width() + border_width * 2
    text_h = border_text.get_height() if border_width else text_surface.get_height() + border_width * 2
    if text_shadow:
        shadow_surface = font.render(text, True, SHADOW_COLOR)
        result_surface = pygame.Surface((text_w + shadow_shift, text_h + shadow_shift), pygame.SRCALPHA)
        result_surface.blit(shadow_surface, (shadow_shift, shadow_shift))
    else:
        result_surface = pygame.Surface((text_w, text_h), pygame.SRCALPHA)
    if border_color:
        result_surface.blit(border_text, (0, 0))
    result_surface.blit(text_surface, (0, 0))
    return result_surface, text_w, text_h
