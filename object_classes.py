import pygame

STANDARD_BUTTON_COLOR = (242, 72, 34)
STANDARD_SECONDARY_BUTTON_COLOR = (255, 204, 0)
HORIZONTAL_INDENT, VERTICAL_INDENT = 12, 15


pygame.init()


class SizeError(ValueError):
    pass


class Button:
    def __init__(self, text_surface, button_color=STANDARD_BUTTON_COLOR,
                 secondary_button_color=STANDARD_SECONDARY_BUTTON_COLOR,
                 width=None, height=None, function=None):
        self.position = 0, 0
        self.position_set = False

        self.text_surface = text_surface
        self.button_color = button_color
        self.secondary_button_color = secondary_button_color
        self.function = function

        self.text_width, self.text_height = (self.text_surface.get_rect().width,
                                             self.text_surface.get_rect().height)
        if width is None:
            width = self.text_width + HORIZONTAL_INDENT
        if height is None:
            height = self.text_height + VERTICAL_INDENT
        if self.text_width > width or self.text_height > height:
            raise SizeError('Введённый размер кнопки меньше размера текста')
        self.width, self.height = width, height
        self.surface = pygame.Surface((self.width, self.height))  # Поверхность кнопки
        self.surface.fill(self.button_color)  # Основной цвет кнопки
        pygame.draw.rect(self.surface, self.secondary_button_color,
                         (0, 0, self.width, self.height), 1)  # Дополнительный цвет(обводка)
        # Наложение текста на поверхность кнопки:
        self.surface.blit(self.text_surface, ((self.width - self.text_width) // 2,
                                              (self.height - self.text_height) // 2))

    def get_pos(self):
        return self.position

    def get_size(self):
        return self.width, self.height

    def get_surface(self):
        if not self.position_set:
            print(f'\nВнимание! Позиция кнопки {self} не была установлена вручную!')
        return self.surface

    def set_pos(self, position):
        self.position = position
        self.position_set = True

    def trigger(self):
        self.function()

    def check_mouse_position(self, mouse_pos):
        if ((self.position[0] <= mouse_pos[0] <= (self.position[0] + self.width) and
             self.position[1] <= mouse_pos[1] <= (self.position[1] + self.height))):
            # Мышь наведена на данную кнопку
            return True
        return False

    def set_under_mouse_effect(self, mouse_is_on_btn=True):  # Реакция кнопки на наведение мыши
        if mouse_is_on_btn:
            # Перерисовка кнопки с обратными цветами:
            self.surface.fill(self.secondary_button_color)
            pygame.draw.rect(self.surface, self.button_color, (0, 0, self.width, self.height), 1)
            self.surface.blit(self.text_surface, ((self.width - self.text_width) // 2,
                                                  (self.height - self.text_height) // 2))
        else:
            # Отрисовка кнопки со стандартными цветами
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(self.button_color)
            pygame.draw.rect(self.surface, self.secondary_button_color,
                             (0, 0, self.width, self.height), 1)
            self.surface.blit(self.text_surface, ((self.width - self.text_width) // 2,
                                                  (self.height - self.text_height) // 2))


class Fighter:
    def __init__(self, character):
        self.speed = 7
        self.character = character
        self.health = 100

        self.walk = [pygame.image.load(f'data/sprites/{self.character}/walk1.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk2.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk3.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk4.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk5.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk6.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk7.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk8.png'),
                     pygame.image.load(f'data/sprites/{self.character}/walk9.png')]

        self.idle = [pygame.image.load(f'data/sprites/{self.character}/idle1.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle2.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle3.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle4.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle5.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle6.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle7.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle8.png'),
                     pygame.image.load(f'data/sprites/{self.character}/idle9.png')]

        self.duck = [pygame.image.load(f'data/sprites/{self.character}/duck1.png'),
                     pygame.image.load(f'data/sprites/{self.character}/duck2.png'),
                     pygame.image.load(f'data/sprites/{self.character}/duck3.png')]
