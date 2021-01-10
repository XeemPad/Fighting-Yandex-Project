import pygame
from main import FPS, WINDOW_WIDTH, sounds_volume
from image_functions import text_to_surface

pygame.init()

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
NON_SKIPPABLE_ACTION, VICTORY = 'non-skip', 'victory_pose'
DAMAGES_DICT = {HIT: 7, DUCK + HIT: 5, KICK: 12, DUCK + KICK: 3}

ANIMATION_DICT = {'scorpion':
                      {'idle': [pygame.image.load(f'data/sprites/scorpion/idle1.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle2.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle3.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle4.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle5.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle6.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle7.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle8.png'),
                                pygame.image.load(f'data/sprites/scorpion/idle9.png')],
                       'walk': [pygame.image.load(f'data/sprites/scorpion/walk1.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk2.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk3.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk4.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk5.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk6.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk7.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk8.png'),
                                pygame.image.load(f'data/sprites/scorpion/walk9.png')],
                       'duck': [pygame.image.load(f'data/sprites/scorpion/duck1.png'),
                                pygame.image.load(f'data/sprites/scorpion/duck2.png'),
                                pygame.image.load(f'data/sprites/scorpion/duck3.png')],
                       'jump': [pygame.image.load(f'data/sprites/scorpion/jump1.png'),
                                pygame.image.load(f'data/sprites/scorpion/jump2.png'),
                                pygame.image.load(f'data/sprites/scorpion/jump3.png'),
                                pygame.image.load(f'data/sprites/scorpion/jump3.png')],
                       'block': [pygame.image.load(f'data/sprites/scorpion/block1.png'),
                                 pygame.image.load(f'data/sprites/scorpion/block2.png'),
                                 pygame.image.load(f'data/sprites/scorpion/block3.png')],
                       'duckblock': [pygame.image.load(f'data/sprites/scorpion/duckblock1.png'),
                                     pygame.image.load(f'data/sprites/scorpion/duckblock2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/duckblock3.png')],
                       'punch': [pygame.image.load(f'data/sprites/scorpion/punch1.png'),
                                 pygame.image.load(f'data/sprites/scorpion/punch2.png'),
                                 pygame.image.load(f'data/sprites/scorpion/punch3.png')],
                       'duckpunch': [pygame.image.load(f'data/sprites/scorpion/duckpunch1.png'),
                                     pygame.image.load(f'data/sprites/scorpion/duckpunch2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/duckpunch3.png')],
                       'jumppunch': [pygame.image.load(f'data/sprites/scorpion/jumppunch1.png'),
                                     pygame.image.load(f'data/sprites/scorpion/jumppunch2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/jumppunch3.png')],
                       'kick': [pygame.image.load(f'data/sprites/scorpion/kick1.png'),
                                pygame.image.load(f'data/sprites/scorpion/kick2.png'),
                                pygame.image.load(f'data/sprites/scorpion/kick3.png'),
                                pygame.image.load(f'data/sprites/scorpion/kick4.png'),
                                pygame.image.load(f'data/sprites/scorpion/kick5.png'),
                                pygame.image.load(f'data/sprites/scorpion/kick6.png')],
                       'duckkick': [pygame.image.load(f'data/sprites/scorpion/duckkick1.png'),
                                    pygame.image.load(f'data/sprites/scorpion/duckkick2.png'),
                                    pygame.image.load(f'data/sprites/scorpion/duckkick3.png')],
                       'jumpkick': [pygame.image.load(f'data/sprites/scorpion/jumpkick1.png'),
                                     pygame.image.load(f'data/sprites/scorpion/jumpkick2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/jumpkick3.png')],
                       # Последняя картинка задерживается на время:
                       'victory': [pygame.image.load(f'data/sprites/scorpion/victory1.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory2.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory3.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory4.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory5.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory5.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory5.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory5.png'),
                                   pygame.image.load(f'data/sprites/scorpion/victory5.png')],
                       # Списки будут сразу с реверсами:
                       'being_hit': [pygame.image.load(f'data/sprites/scorpion/hit1.png'),
                                     pygame.image.load(f'data/sprites/scorpion/hit2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/hit3.png'),
                                     pygame.image.load(f'data/sprites/scorpion/hit2.png'),
                                     pygame.image.load(f'data/sprites/scorpion/hit1.png')],
                       'being_hitdown': [pygame.image.load(f'data/sprites/scorpion/hitdown1.png'),
                                         pygame.image.load(f'data/sprites/scorpion/hitdown2.png'),
                                         pygame.image.load(f'data/sprites/scorpion/hitdown3.png'),
                                         pygame.image.load(f'data/sprites/scorpion/hitdown2.png'),
                                         pygame.image.load(f'data/sprites/scorpion/hitdown1.png')],
                       'being_duckhit': [pygame.image.load(f'data/sprites/scorpion/duckhit1.png'),
                                         pygame.image.load(f'data/sprites/scorpion/duckhit2.png'),
                                         pygame.image.load(f'data/sprites/scorpion/duckhit3.png'),
                                         pygame.image.load(f'data/sprites/scorpion/duckhit2.png'),
                                         pygame.image.load(f'data/sprites/scorpion/duckhit1.png')]},
                  'liukang':
                      {'idle': [pygame.image.load(f'data/sprites/liukang/idle1.png'),
                                pygame.image.load(f'data/sprites/liukang/idle2.png'),
                                pygame.image.load(f'data/sprites/liukang/idle3.png'),
                                pygame.image.load(f'data/sprites/liukang/idle4.png'),
                                pygame.image.load(f'data/sprites/liukang/idle5.png'),
                                pygame.image.load(f'data/sprites/liukang/idle6.png'),
                                pygame.image.load(f'data/sprites/liukang/idle7.png'),
                                pygame.image.load(f'data/sprites/liukang/idle8.png'),
                                pygame.image.load(f'data/sprites/liukang/idle9.png'),
                                pygame.image.load(f'data/sprites/liukang/idle10.png'),
                                pygame.image.load(f'data/sprites/liukang/idle11.png'),
                                pygame.image.load(f'data/sprites/liukang/idle12.png'),
                                pygame.image.load(f'data/sprites/liukang/idle13.png'),
                                pygame.image.load(f'data/sprites/liukang/idle14.png'),
                                pygame.image.load(f'data/sprites/liukang/idle15.png'),
                                pygame.image.load(f'data/sprites/liukang/idle16.png'),
                                pygame.image.load(f'data/sprites/liukang/idle17.png')],
                       'walk': [pygame.image.load(f'data/sprites/liukang/walk1.png'),
                                pygame.image.load(f'data/sprites/liukang/walk2.png'),
                                pygame.image.load(f'data/sprites/liukang/walk3.png'),
                                pygame.image.load(f'data/sprites/liukang/walk4.png'),
                                pygame.image.load(f'data/sprites/liukang/walk5.png'),
                                pygame.image.load(f'data/sprites/liukang/walk6.png'),
                                pygame.image.load(f'data/sprites/liukang/walk7.png'),
                                pygame.image.load(f'data/sprites/liukang/walk8.png')],
                       'duck': [pygame.image.load(f'data/sprites/liukang/duck1.png'),
                                pygame.image.load(f'data/sprites/liukang/duck2.png'),
                                pygame.image.load(f'data/sprites/liukang/duck3.png')],
                       'jump': [pygame.image.load(f'data/sprites/liukang/jump1.png'),
                                pygame.image.load(f'data/sprites/liukang/jump2.png'),
                                pygame.image.load(f'data/sprites/liukang/jump3.png'),
                                pygame.image.load(f'data/sprites/liukang/jump3.png')],
                       'block': [pygame.image.load(f'data/sprites/liukang/block1.png'),
                                 pygame.image.load(f'data/sprites/liukang/block2.png'),
                                 pygame.image.load(f'data/sprites/liukang/block3.png')],
                       'duckblock': [pygame.image.load(f'data/sprites/liukang/duckblock1.png'),
                                     pygame.image.load(f'data/sprites/liukang/duckblock2.png'),
                                     pygame.image.load(f'data/sprites/liukang/duckblock3.png')],
                       'punch': [pygame.image.load(f'data/sprites/liukang/punch1.png'),
                                 pygame.image.load(f'data/sprites/liukang/punch2.png'),
                                 pygame.image.load(f'data/sprites/liukang/punch3.png')],
                       'duckpunch': [pygame.image.load(f'data/sprites/liukang/duckpunch1.png'),
                                     pygame.image.load(f'data/sprites/liukang/duckpunch2.png'),
                                     pygame.image.load(f'data/sprites/liukang/duckpunch3.png')],
                       'jumppunch': [pygame.image.load(f'data/sprites/liukang/jumppunch1.png'),
                                     pygame.image.load(f'data/sprites/liukang/jumppunch2.png'),
                                     pygame.image.load(f'data/sprites/liukang/jumppunch3.png')],
                       'kick': [pygame.image.load(f'data/sprites/liukang/kick1.png'),
                                pygame.image.load(f'data/sprites/liukang/kick2.png'),
                                pygame.image.load(f'data/sprites/liukang/kick3.png'),
                                pygame.image.load(f'data/sprites/liukang/kick4.png'),
                                pygame.image.load(f'data/sprites/liukang/kick5.png'),
                                pygame.image.load(f'data/sprites/liukang/kick6.png')],
                       'duckkick': [pygame.image.load(f'data/sprites/liukang/duckkick1.png'),
                                    pygame.image.load(f'data/sprites/liukang/duckkick2.png'),
                                    pygame.image.load(f'data/sprites/liukang/duckkick3.png')],
                       'jumpkick': [pygame.image.load(f'data/sprites/liukang/jumpkick1.png'),
                                    pygame.image.load(f'data/sprites/liukang/jumpkick2.png'),
                                    pygame.image.load(f'data/sprites/liukang/jumpkick3.png')],
                       # Последняя картинка задерживается на время:
                       'victory': [pygame.image.load(f'data/sprites/liukang/victory1.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory2.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory3.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory4.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory5.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory6.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory7.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory8.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory9.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory10.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory11.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory12.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory13.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory14.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory15.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory15.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory15.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory15.png'),
                                   pygame.image.load(f'data/sprites/liukang/victory15.png')],
                       # Списки будут сразу с реверсами:
                       'being_hit': [pygame.image.load(f'data/sprites/liukang/hit1.png'),
                                     pygame.image.load(f'data/sprites/liukang/hit2.png'),
                                     pygame.image.load(f'data/sprites/liukang/hit3.png'),
                                     pygame.image.load(f'data/sprites/liukang/hit2.png'),
                                     pygame.image.load(f'data/sprites/liukang/hit1.png')],
                       'being_hitdown': [pygame.image.load(f'data/sprites/liukang/hitdown1.png'),
                                         pygame.image.load(f'data/sprites/liukang/hitdown2.png'),
                                         pygame.image.load(f'data/sprites/liukang/hitdown3.png'),
                                         pygame.image.load(f'data/sprites/liukang/hitdown2.png'),
                                         pygame.image.load(f'data/sprites/liukang/hitdown1.png')],
                       'being_duckhit': [pygame.image.load(f'data/sprites/liukang/duckhit1.png'),
                                         pygame.image.load(f'data/sprites/liukang/duckhit2.png'),
                                         pygame.image.load(f'data/sprites/liukang/duckhit3.png'),
                                         pygame.image.load(f'data/sprites/liukang/duckhit2.png'),
                                         pygame.image.load(f'data/sprites/liukang/duckhit1.png')]}
                  }

FIGHT_SOUNDS = {
    HIT: pygame.mixer.Sound('data/sounds/punches_kicks/punch.mp3'),
    KICK: pygame.mixer.Sound('data/sounds/punches_kicks/kick.mp3'),
    BLOCK: pygame.mixer.Sound('data/sounds/punches_kicks/block.mp3'),
    JUMP: pygame.mixer.Sound('data/sounds/punches_kicks/jump.mp3'),
    DUCK: pygame.mixer.Sound('data/sounds/punches_kicks/duck.mp3')
}

STANDARD_BUTTON_COLOR = (242, 72, 34)
STANDARD_SECONDARY_BUTTON_COLOR = (255, 204, 0)
HORIZONTAL_INDENT, VERTICAL_INDENT = 12, 15
BUTTON_SOUNDS_DIRECTORIES = ['data/sounds/ui/btn_hovered.mp3', 'data/sounds/ui/btn_triggered.mp3']
button_sounds = [pygame.mixer.Sound(sound) for sound in BUTTON_SOUNDS_DIRECTORIES]
for sound in button_sounds:
    sound.set_volume(sounds_volume)

IMAGE_SCALE_VALUE = round((WINDOW_WIDTH / 1024) * 2)

PLAYER_NAME_FONT_DIRECTORY = 'data/font2.ttf'
PLAYER_NAME_FONT_SIZE = 28

HEALTH_COLOR = (0, 255, 0)


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
        self.mouse_is_on_btn = False

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
        self.paint()  # Прорисовка элементов кнопки

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
        button_sounds[1].play()  # Звук нажатия
        self.function()

    def check_mouse_position(self, mouse_pos):
        if ((self.position[0] <= mouse_pos[0] <= (self.position[0] + self.width) and
             self.position[1] <= mouse_pos[1] <= (self.position[1] + self.height))):
            # Мышь наведена на данную кнопку
            return True
        return False

    def paint(self):
        if self.mouse_is_on_btn:  # Меняем цвета местами, если на кнопку наведена мышь
            button_color = self.secondary_button_color
            secondary_button_color = self.button_color
        else:
            button_color = self.button_color
            secondary_button_color = self.secondary_button_color
        self.surface.fill(button_color)  # Основной цвет кнопки
        pygame.draw.rect(self.surface, secondary_button_color,
                         (0, 0, self.width, self.height), 1)  # Дополнительный цвет(обводка)
        # Наложение текста на поверхность кнопки:
        self.surface.blit(self.text_surface, ((self.width - self.text_width) // 2,
                                              (self.height - self.text_height) // 2))

    def set_under_mouse_effect(self, mouse_is_on_btn=True):  # Реакция кнопки на наведение мыши
        if self.mouse_is_on_btn is False and mouse_is_on_btn:
            button_sounds[0].play()  # Звук наведения
        self.mouse_is_on_btn = mouse_is_on_btn
        self.paint()

    def set_text(self, new_text_surface):
        text_width, text_height = (new_text_surface.get_rect().width,
                                   new_text_surface.get_rect().height)
        if text_width > self.width or text_height > self.height:
            raise SizeError('Размер нового текста превышает размер кнопки')
        self.text_surface = new_text_surface
        self.text_width, self.text_height = text_width, text_height

        # Перерисовка кнопки:
        self.paint()


class HealthBar:
    def __init__(self, player_name, align_is_left=True):
        self.align_is_left = align_is_left
        self.text = player_name
        self.width, self.height = WINDOW_WIDTH // 5 * 2, 50
        self.hp = 100

        self.font = pygame.font.Font(PLAYER_NAME_FONT_DIRECTORY, PLAYER_NAME_FONT_SIZE)
        self.render_health_bar()
        self.render_text_on_bar()

    def render_health_bar(self):
        self.health_surface = pygame.Surface((self.width, self.height))
        self.health_surface.fill((255, 0, 0))
        pygame.draw.rect(self.health_surface, HEALTH_COLOR,
                         (0, 0, round(self.width * (self.hp / 100)), self.height))

    def render_text_on_bar(self):
        self.text_surface, self.text_w, self.text_h = text_to_surface(self.text, (0, 0, 0),
                                                                      PLAYER_NAME_FONT_SIZE,
                                                                      font_directory=PLAYER_NAME_FONT_DIRECTORY)
        self.text_x = 10 if self.align_is_left else self.width - 10 - self.text_w
        self.text_y = (self.height - self.text_h) // 2 - 2
        self.health_surface.blit(self.text_surface, (self.text_x, self.text_y))

    def update(self, new_hp):
        self.hp = new_hp if new_hp >= 0 else 0
        self.render_health_bar()
        self.render_text_on_bar()

    def get_surface(self):
        return self.health_surface

    def get_size(self):
        return self.width, self.height


class Fighter(pygame.sprite.Sprite):
    def __init__(self, all_sprites, character, position):
        super().__init__(all_sprites)

        self.x_speed = 18 * (WINDOW_WIDTH // 1024)
        self.y_speed = 90 * (WINDOW_WIDTH // 1024)
        self.current_x_speed = 0
        self.current_y_speed = 0  # Отрицательная скорость означает подъём вверх
        self.acceleration = 6
        self.character = character
        self.health = 100
        self.image_is_reverted = False

        self.animation_delay = FPS / 60 * 6  # Задержка перед следующей картинкой анимации
        self.frames_count = 0

        # Списки анимаций:
        self.idle = self.scaled_animation(ANIMATION_DICT[self.character]['idle'])
        self.walk = self.scaled_animation(ANIMATION_DICT[self.character]['walk'])
        self.duck = self.scaled_animation(ANIMATION_DICT[self.character]['duck'])
        self.jump = self.scaled_animation(ANIMATION_DICT[self.character]['jump'])
        self.block = self.scaled_animation(ANIMATION_DICT[self.character]['block'])
        self.duckblock = self.scaled_animation(ANIMATION_DICT[self.character]['duckblock'])
        self.punch = self.scaled_animation(ANIMATION_DICT[self.character]['punch'])
        self.duckpunch = self.scaled_animation(ANIMATION_DICT[self.character]['duckpunch'])
        self.kick = self.scaled_animation(ANIMATION_DICT[self.character]['kick'])
        self.duckkick = self.scaled_animation(ANIMATION_DICT[self.character]['duckkick'])
        self.victory = self.scaled_animation(ANIMATION_DICT[self.character]['victory'])
        self.being_hit = self.scaled_animation(ANIMATION_DICT[self.character]['being_hit'])
        self.being_hitdown = self.scaled_animation(ANIMATION_DICT[self.character]['being_hitdown'])
        self.being_duckhit = self.scaled_animation(ANIMATION_DICT[self.character]['being_duckhit'])

        self.position = position
        self.update_image(self.idle[0])

        self.floor_y = self.rect.bottom

        # Текущая анимация:
        self.current_animation = self.idle
        self.animation_index = 0  # Текущий индекс элемента списка картинок анимации
        self.animation_is_cycled = True

        self.isDamaged = False

        self.current_actions = set()

    def get_hp(self):
        return self.health

    def get_center_x(self):
        return self.rect.centerx

    def get_current_actions(self):
        return self.current_actions

    def get_damage(self, enemy_actions):
        enemy_hit_configuration = ''
        enemy_hit_configuration += DUCK if DUCK in enemy_actions else ''
        enemy_hit_configuration += JUMP if JUMP in enemy_actions else ''
        if HIT in enemy_actions:
            enemy_hit_configuration += HIT
            # Звук удара:
            FIGHT_SOUNDS[HIT].play()
        if KICK in enemy_actions:
            enemy_hit_configuration += KICK
            FIGHT_SOUNDS[KICK].play()
        damage_value = DAMAGES_DICT[enemy_hit_configuration]
        # Если у данного игрока блок, то урон вдвое меньше, кроме подсечки:
        if BLOCK in self.current_actions and enemy_hit_configuration != DUCK + KICK:
            damage_value //= 2
        self.health -= damage_value
        # Ставим анимацию реакции на удар, если у игрока не было блока:
        if BLOCK not in self.current_actions:
            if DUCK in self.current_actions:
                self.set_being_duckhit()
            else:
                if DUCK in enemy_actions:
                    self.set_being_hitdown()
                else:
                    self.set_being_hit()

    def new_action(self, action_name):
        # Метод возвращает, выполнено ли запрашиваемое действие
        if self.current_animation == self.idle:
            if action_name == LEFT or action_name == RIGHT:
                self.set_walk(action_name)
            elif action_name == DUCK:
                self.set_duck()
            elif action_name == BLOCK:
                self.set_block()
            elif action_name == HIT:
                self.set_punch()
            elif action_name == KICK:
                self.set_kick()
            elif action_name == JUMP:
                self.set_jump()
        elif self.current_actions < {LEFT, RIGHT, DUCK}:
            if self.current_actions < {LEFT, RIGHT}:
                if action_name == BLOCK:
                    self.set_block()
                elif action_name == HIT:
                    self.set_idle()
                    self.set_punch()
                elif action_name == KICK:
                    self.set_idle()
                    self.set_kick()
            elif self.current_actions == {DUCK}:
                # Игрок может делать другие действия только, если полностью сел:
                if self.animation_index == len(self.current_animation) - 1:
                    if action_name == BLOCK:
                        self.set_duckblock()
                    elif action_name == HIT:
                        self.set_duckpunch()
                    elif action_name == KICK:
                        self.set_duckkick()
        elif JUMP in self.current_actions:
            if action_name == LEFT or action_name == RIGHT:
                self.set_walk(action_name, is_jumping=True)

    def stop_action(self, key):
        if self.current_animation in [self.walk, self.walk[::-1]] and key in [RIGHT, LEFT]:
            self.set_idle()
        elif self.current_actions & {DUCK, BLOCK} and key in [DUCK, BLOCK]:
            if key == DUCK and DUCK in self.current_actions:
                self.current_actions.add(NON_SKIPPABLE_ACTION)
                self.current_actions.remove(DUCK)
            elif key == BLOCK and BLOCK in self.current_actions:
                self.current_actions.add(NON_SKIPPABLE_ACTION)
            if self.animation_index > 0:
                self.current_animation = self.current_animation[self.animation_index - 1::-1]
                if key == DUCK and BLOCK in self.current_actions:
                    self.current_animation.extend(self.duck[::-1] + [self.idle[0]])
                # Если кнопка сидения отпущена во время удара:
                elif (key == DUCK and self.current_animation in
                      [self.duckpunch, self.duckpunch[len(self.duckpunch) - 2::-1],
                       self.duckkick, self.duckkick[len(self.duckkick) - 2::-1]]):
                    self.current_animation = self.duck[::-1] + [self.idle[0]]
                    if HIT in self.current_actions:
                        self.current_actions.remove(HIT)
                    if KICK in self.current_actions:
                        self.current_actions.remove(KICK)
                self.animation_index = 0
            else:
                if key == DUCK and BLOCK in self.current_actions:
                    self.current_animation = self.duck[::-1] + [self.idle[0]]
                    self.animation_index = 0
                # Если кнопка сидения отпущена во время удара:
                elif (key == DUCK and self.current_animation in
                      [self.duckpunch, self.duckpunch[len(self.duckpunch) - 2::-1],
                       self.duckkick, self.duckkick[len(self.duckkick) - 2::-1]]):
                    self.current_animation = self.duck[::-1] + [self.idle[0]]
                    self.animation_index = 0
                    if HIT in self.current_actions:
                        self.current_actions.remove(HIT)
                    if KICK in self.current_actions:
                        self.current_actions.remove(KICK)
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

    def update(self):
        self.frames_count += 1
        if self.frames_count % self.animation_delay == 0:
            new_image = self.current_animation[self.animation_index]
            if (self.animation_index == len(self.current_animation) - 1) \
                    and not self.animation_is_cycled:
                if NON_SKIPPABLE_ACTION in self.current_actions:
                    if self.current_animation == self.punch:
                        self.set_punch(True)
                    elif self.current_animation == self.duckpunch:
                        self.set_duckpunch(True)
                    elif self.current_animation == self.kick:
                        self.set_kick(True)
                    elif self.current_animation == self.duckkick:
                        self.set_duckkick(True)
                    elif self.current_animation == self.jump:
                        self.set_jump(True)
                    elif DUCK in self.current_actions:  # Это условие должно быть предпоследним
                        self.set_duck(True)
                    else:
                        self.set_idle()
            else:
                self.animation_index = (self.animation_index + 1) % len(self.current_animation)
                if self.current_animation not in (self.punch, self.duckpunch) \
                        and HIT in self.current_actions:
                    self.current_actions.remove(HIT)
                if self.current_animation not in (self.kick, self.duckkick) \
                        and KICK in self.current_actions:
                    self.current_actions.remove(KICK)

            # Разворачиваем картинку, если персонаж должен быть повёрнут, обновляем координаты:
            if self.image_is_reverted:
                new_image = pygame.transform.flip(new_image, True, False)
                self.position = self.rect.bottomright
            else:
                self.position = self.rect.bottomleft

            if JUMP not in self.current_actions:
                self.position = self.position[0], self.floor_y
            else:
                # Изменение вертикальной скорости:
                if self.time_in_air > 0:
                    self.current_y_speed = self.y_speed - self.time_in_air ** 2 * self.acceleration
                self.time_in_air += 1
            self.update_image(new_image)  # Установка новой картинки
        if self.current_x_speed:
            if ((0 < (self.rect.x + round(self.current_x_speed / self.animation_delay))
                 < WINDOW_WIDTH - self.rect.width)):
                self.rect.x += round(self.current_x_speed / self.animation_delay)
        elif self.rect.x <= 0 or self.rect.x >= WINDOW_WIDTH - self.rect.width:
            if self.rect.x <= 0:
                self.rect.x = 1
            else:
                self.rect.right = WINDOW_WIDTH - 2
        if self.current_y_speed:
            dy = round(self.current_y_speed / self.animation_delay)
            self.rect.bottom = self.rect.bottom - dy

    def update_image(self, new_image):
        self.image = new_image
        self.rect = self.image.get_rect()
        if self.image_is_reverted:
            self.rect.bottomright = self.position
        else:
            self.rect.bottomleft = self.position
        self.mask = pygame.mask.from_surface(self.image)

    def revert(self):
        if self.image_is_reverted:
            self.image_is_reverted = False
            self.position = self.rect.topright
        else:
            self.image_is_reverted = True
            self.position = self.rect.topleft

    def check_damage_ability(self):
        if not self.isDamaged:
            if HIT in self.current_actions:
                # Если первая картинка удара уже была установлена
                # Или если удар начал возвращаться, но HIT in self.current_actions
                if (self.animation_index > 0 or
                        self.current_animation in [self.punch[len(self.punch) - 2::-1],
                                                   self.duckpunch[len(self.duckpunch) - 2::-1]]):
                    return True
            elif KICK in self.current_actions:
                if (self.animation_index > 0 or
                        self.current_animation in [self.kick[len(self.kick) - 2::-1],
                                                   self.duckkick[len(self.duckkick) - 2::-1]]):
                    return True
        return False

    def set_idle(self):
        self.current_animation = self.idle
        self.animation_is_cycled = True
        self.animation_index = 0
        self.current_x_speed = 0
        self.current_y_speed = 0

        self.current_actions = set()

    def set_walk(self, direction, is_jumping=False):
        if direction == RIGHT:
            if not is_jumping:
                if self.image_is_reverted:
                    # Персонаж идёт задом:
                    self.current_animation = self.walk[::-1]
                else:
                    self.current_animation = self.walk
            self.current_x_speed = self.x_speed
        else:
            if not is_jumping:
                if self.image_is_reverted:
                    # Персонаж идёт задом:
                    self.current_animation = self.walk
                else:
                    self.current_animation = self.walk[::-1]
            self.current_x_speed = -self.x_speed
        if not is_jumping:
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
        if reversed:
            self.current_animation = self.punch[len(self.punch) - 2::-1]
            self.animation_index = 0
        else:
            self.current_animation = self.punch
            self.animation_is_cycled = False
            self.animation_index = 0
            self.isDamaged = False
            self.current_actions.add(HIT)
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_duckpunch(self, reversed=False):
        if reversed:
            self.current_animation = self.duckpunch[len(self.duckpunch) - 2::-1]
            self.animation_index = 0
        else:
            self.current_animation = self.duckpunch
            self.animation_is_cycled = False
            self.animation_index = 0
            self.isDamaged = False
            self.current_actions.add(HIT)
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_kick(self, reversed=False):
        if reversed:
            self.current_animation = self.kick[len(self.kick) - 2::-1]
            self.animation_index = 0
        else:
            self.current_animation = self.kick
            self.animation_is_cycled = False
            self.animation_index = 0
            self.isDamaged = False
            self.current_actions.add(KICK)
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_duckkick(self, reversed=False):
        if reversed:
            self.current_animation = self.duckkick[len(self.duckkick) - 2::-1]
            self.animation_index = 0
        else:
            self.current_animation = self.duckkick
            self.animation_is_cycled = False
            self.animation_index = 0
            self.isDamaged = False
            self.current_actions.add(KICK)
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_being_hit(self):
        self.current_animation = self.being_hit
        self.animation_is_cycled = False
        self.animation_index = 0
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_being_hitdown(self):
        self.current_animation = self.being_hitdown
        self.animation_is_cycled = False
        self.animation_index = 0
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_being_duckhit(self):
        self.current_animation = self.being_duckhit
        self.animation_is_cycled = False
        self.animation_index = 0
        self.current_actions.add(NON_SKIPPABLE_ACTION)

    def set_victory(self):
        self.set_idle()
        self.current_animation = self.victory
        self.animation_is_cycled = False
        self.animation_index = 0
        self.current_actions.add(NON_SKIPPABLE_ACTION)
        self.current_actions.add(VICTORY)

    def set_jump(self, reversed=False):
        if reversed:
            self.current_animation = self.jump[::-1]
            self.animation_index = 0
        else:
            self.time_in_air = 0
            self.current_animation = self.jump
            self.animation_is_cycled = False
            self.animation_index = 0
            self.current_actions.add(NON_SKIPPABLE_ACTION)
            self.current_actions.add(JUMP)
