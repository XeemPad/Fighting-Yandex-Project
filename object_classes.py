import pygame

WINDOW_WIDTH = 1024
STANDARD_BUTTON_COLOR = (242, 72, 34)
STANDARD_SECONDARY_BUTTON_COLOR = (255, 204, 0)
HORIZONTAL_INDENT, VERTICAL_INDENT = 12, 15

IMAGE_SCALE_VALUE = (WINDOW_WIDTH // 1024) * 2


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


class Fighter(pygame.sprite.Sprite):
    def __init__(self, all_sprites, character, position):
        super().__init__(all_sprites)

        self.speed = 7
        self.character = character
        self.health = 100
        self.image_is_reverted = False
        
        self.animation_delay = 7  # Задержка перед следующей картинкой анимации
        self.frames_count = 0

        self.is_idle = True

        idle_images = [pygame.image.load(f'data/sprites/{self.character}/idle1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle3.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle4.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle5.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle6.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle7.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle8.png'),
                       pygame.image.load(f'data/sprites/{self.character}/idle9.png')]
        self.idle = self.scaled_animation(idle_images)
        self.idle_index = 1  # Здесь и далее: указывает на текущий этап анимации данного действия

        walk_images = [pygame.image.load(f'data/sprites/{self.character}/walk1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk3.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk4.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk5.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk6.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk7.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk8.png'),
                       pygame.image.load(f'data/sprites/{self.character}/walk9.png')]
        self.walk = self.scaled_animation(walk_images)

        self.walk_index = 0

        duck_images = [pygame.image.load(f'data/sprites/{self.character}/duck1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/duck2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/duck3.png')]
        self.duck = self.scaled_animation(duck_images)
        self.duck_index = 0

        jump_images = [pygame.image.load(f'data/sprites/{self.character}/jump1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/jump2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/jump3.png')]
        self.jump = self.scaled_animation(jump_images)
        self.duck_index = 0

        self.image = self.idle[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.topleft = position

    @staticmethod
    def scaled_animation(img_list):
        return list(map(lambda img:
                        pygame.transform.scale(img,
                                               (round(img.get_width() * IMAGE_SCALE_VALUE),
                                                round(img.get_height() * IMAGE_SCALE_VALUE))),
                        img_list))

    def update_mask(self):
        self.rect = self.image.get_rect()
        # вычисляем маску:
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.frames_count += 1
        image_changed = False
        if self.is_idle:
            if self.frames_count % self.animation_delay == 0:
                new_image = self.idle[self.idle_index]
                self.idle_index = (self.idle_index + 1) % len(self.idle)
                image_changed = True
        if image_changed:
            if self.image_is_reverted:
                new_image = pygame.transform.flip(new_image, True, False)
            self.image = new_image

    def revert(self):
        if self.image_is_reverted:
            self.image_is_reverted = False
        else:
            self.image_is_reverted = True
