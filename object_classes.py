import pygame
from main import FPS, WINDOW_WIDTH

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
NON_SKIPPABLE_ACTION = 'non-skip'

STANDARD_BUTTON_COLOR = (242, 72, 34)
STANDARD_SECONDARY_BUTTON_COLOR = (255, 204, 0)
HORIZONTAL_INDENT, VERTICAL_INDENT = 12, 15

IMAGE_SCALE_VALUE = (WINDOW_WIDTH // 1024) * 2
fighter_width = 63 * IMAGE_SCALE_VALUE

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

        self.x_speed = 18 * (WINDOW_WIDTH // 1024)
        self.y_speed = 36 * (WINDOW_WIDTH // 1024)
        self.gravity_acceleration = 4 * (WINDOW_WIDTH // 1024) ** 2
        self.current_x_speed = 0
        self.current_y_speed = 0  # Отрицательная скорость означает подъём вверх
        self.character = character
        self.health = 100
        self.image_is_reverted = False

        self.animation_delay = FPS / 60 * 10  # Задержка перед следующей картинкой анимации
        self.frames_count = 0

        self.isDamaged = False

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

        duck_images = [pygame.image.load(f'data/sprites/{self.character}/duck1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/duck2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/duck3.png')]
        self.duck = self.scaled_animation(duck_images)

        jump_images = [pygame.image.load(f'data/sprites/{self.character}/jump1.png'),
                       pygame.image.load(f'data/sprites/{self.character}/jump2.png'),
                       pygame.image.load(f'data/sprites/{self.character}/jump3.png')]
        self.jump = self.scaled_animation(jump_images)

        block_images = [pygame.image.load(f'data/sprites/{self.character}/block1.png'),
                        pygame.image.load(f'data/sprites/{self.character}/block2.png'),
                        pygame.image.load(f'data/sprites/{self.character}/block3.png')]
        self.block = self.scaled_animation(block_images)

        duckblock_images = [pygame.image.load(f'data/sprites/{self.character}/duckblock1.png'),
                            pygame.image.load(f'data/sprites/{self.character}/duckblock2.png'),
                            pygame.image.load(f'data/sprites/{self.character}/duckblock3.png')]
        self.duckblock = self.scaled_animation(duckblock_images)

        punch_images = [pygame.image.load(f'data/sprites/{self.character}/punch1.png'),
                        pygame.image.load(f'data/sprites/{self.character}/punch2.png'),
                        pygame.image.load(f'data/sprites/{self.character}/punch3.png')]
        self.punch = self.scaled_animation(punch_images)

        self.position = position
        self.update_image(self.idle[0])
        self.rect.topleft = self.position

        self.floor_y = self.rect.bottom

        # Текущая анимация:
        self.current_animation = self.idle
        self.animation_index = 0  # Текущий индекс элемента списка картинок анимации
        self.animation_is_cycled = True

        self.current_actions = set()

    def get_center_x(self):
        return self.rect.centerx

    def get_current_actions(self):
        return self.current_actions

    def new_action(self, action_name):
        # Метод возвращает, выполнено ли запрашиваемое действие
        if self.current_animation == self.idle:
            if action_name == LEFT or action_name == RIGHT:
                self.set_walk(action_name)
                return True
            elif action_name == DUCK:
                self.set_duck()
                return True
            elif action_name == BLOCK:
                self.set_block()
                return True
            elif action_name == HIT:
                self.set_punch()
                return True
        elif self.current_actions < {LEFT, RIGHT, DUCK}:
            if action_name == BLOCK:
                if self.current_actions < {LEFT, RIGHT}:
                    self.set_block()
                    return True
                elif self.current_actions == {DUCK}:
                    if self.animation_index == len(self.current_animation) - 1:
                        self.set_duckblock()
                        return True
            else:
                # Позже сидя можно будет биться и ставить блок
                pass
        return False

    def stop_action(self, key):
        if self.current_animation in [self.walk, self.walk[::-1]] and key in [RIGHT, LEFT]:
            self.set_idle()
        elif (self.current_animation in [self.duck, self.block, self.duckblock, self.punch] and
              key in [DUCK, BLOCK, HIT]):  # Список неполный
            if key == DUCK and DUCK in self.current_actions:
                self.current_actions.add(NON_SKIPPABLE_ACTION)
                self.current_actions.remove(DUCK)
            elif key == BLOCK and BLOCK in self.current_actions:
                self.current_actions.add(NON_SKIPPABLE_ACTION)
            elif key == HIT and HIT in self.current_actions:
                self.current_actions.add(NON_SKIPPABLE_ACTION)
            if self.animation_index > 0:
                self.current_animation = self.current_animation[self.animation_index - 1::-1]
                if key == DUCK and BLOCK in self.current_actions:
                    self.current_animation.extend(self.duck[::-1] + [self.idle[0]])
                self.animation_index = 0
            else:
                if key == DUCK and BLOCK in self.current_actions:
                    self.current_animation = self.duck[::-1] + [self.idle[0]]
                    self.animation_index = 0
                elif key == BLOCK and DUCK in self.current_actions:
                    self.set_duck(True)
                else:
                    self.current_animation = [self.idle[0]]
                    self.animation_index = 0

    @staticmethod
    def scaled_animation(img_list):
        return list(map(lambda img:
                        pygame.transform.scale(img,
                                               (round(img.get_width() * IMAGE_SCALE_VALUE),
                                                round(img.get_height() * IMAGE_SCALE_VALUE))),
                        img_list))

    def get_damage(self):
        self.health -= 7
        print(self.health)

    def update(self):
        self.frames_count += 1
        if self.frames_count % self.animation_delay == 0:
            new_image = self.current_animation[self.animation_index]
            if (self.animation_index == len(self.current_animation) - 1) \
                    and not self.animation_is_cycled:
                if NON_SKIPPABLE_ACTION in self.current_actions:
                    if DUCK in self.current_actions:
                        self.set_duck(True)
                    elif HIT in self.current_actions:
                        self.set_punch(True)
                    else:
                        self.set_idle()
            else:
                self.animation_index = (self.animation_index + 1) % len(self.current_animation)
            # Разворачиваем картинку, если персонаж должен быть повёрнут:
            if self.image_is_reverted:
                new_image = pygame.transform.flip(new_image, True, False)
            self.update_image(new_image)  # Установка новой картинки

            if JUMP not in self.current_actions:
                self.rect.bottom = self.floor_y
        if self.current_x_speed:
            if ((0 < (self.rect.x + round(self.current_x_speed / self.animation_delay))
                 < WINDOW_WIDTH - fighter_width)):
                self.rect.x += round(self.current_x_speed / self.animation_delay)

            self.position = self.rect.topleft

    def update_image(self, new_image):
        self.image = new_image
        self.rect = self.image.get_rect()
        if self.image_is_reverted:
            self.rect.topright = self.position
        else:
            self.rect.topleft = self.position
        self.mask = pygame.mask.from_surface(self.image)

    def revert(self):
        if self.image_is_reverted:
            self.image_is_reverted = False
        else:
            self.image_is_reverted = True

    def check_damage_ability(self):
        if self.isDamaged:
            return False
        elif not self.isDamaged and self.punch in self.current_animation:
            return True

    def set_idle(self):
        self.current_animation = self.idle
        self.animation_is_cycled = True
        self.animation_index = 0
        self.current_x_speed = 0
        self.current_y_speed = 0

        self.current_actions = set()

    def set_walk(self, direction):
        if direction == RIGHT:
            if self.image_is_reverted:
                # Персонаж идёт задом:
                self.current_animation = self.walk[::-1]
            else:
                self.current_animation = self.walk
            self.current_x_speed = self.x_speed
        else:
            if self.image_is_reverted:
                # Персонаж идёт задом:
                self.current_animation = self.walk
            else:
                self.current_animation = self.walk[::-1]
            self.current_x_speed = -self.x_speed
        self.animation_is_cycled = True
        self.animation_index = 0

        self.current_actions.add(direction)

    def set_duck(self, last_anim=False):
        self.current_animation = self.duck
        self.animation_is_cycled = False
        self.animation_index = len(self.duck) - 1 if last_anim else 0

        self.current_actions = {DUCK}

    def set_block(self):
        self.set_idle()
        self.current_animation = self.block
        self.animation_is_cycled = False

        self.current_actions.add(BLOCK)

    def set_duckblock(self):
        self.current_animation = self.duckblock
        self.animation_index = 0

        self.current_actions.add(BLOCK)

    def set_punch(self, reversed=False):
        self.current_animation = self.punch
        self.animation_is_cycled = False
        self.animation_index = 0
        self.isDamaged = False
        self.current_actions.add(HIT)
        self.current_actions.add(NON_SKIPPABLE_ACTION)
        if reversed:
            self.current_animation = self.punch[len(self.current_animation) - 1::-1]
            self.current_actions.remove(HIT)
