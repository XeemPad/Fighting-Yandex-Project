import pygame
import random
from object_classes import Fighter, HealthBar, Button, IMAGE_SCALE_VALUE
from pygame.mixer import music

from main import terminate, start_game, GAME_NAME, ICON_FILE_DIRECTORY, WINDOW_WIDTH, \
    WINDOW_HEIGHT, CONFIGURATION_FILE_DIRECTORY, FONT_DIRECTORY
from image_functions import text_to_surface


# Константы:
FPS = 60

BACKGROUND_DIRECTORIES = {'background1': 'data/backgrounds/background1.jpg',
                          'background2': 'data/backgrounds/background2.jpg',
                          'background3': 'data/backgrounds/background3.png',
                          'background4': 'data/backgrounds/background4.jpg',
                          'background5': 'data/backgrounds/background5.jpg'}
MUSIC_DIRECTORIES = ['data/sounds/bg_music/music_one.mp3', 'data/sounds/bg_music/music_two.mp3',
                     'data/sounds/bg_music/music_three.mp3']

LEFT, RIGHT, DUCK, JUMP, HIT, KICK, BLOCK = 'left', 'right', 'duck', 'jump', 'hit', 'kick', 'block'
CONTROL = [{LEFT: pygame.K_a, RIGHT: pygame.K_d, DUCK: pygame.K_s, JUMP: pygame.K_w,
            HIT: pygame.K_g, KICK: pygame.K_h, BLOCK: pygame.K_j},  # Управление первого игрока
           {LEFT: pygame.K_LEFT, RIGHT: pygame.K_RIGHT, DUCK: pygame.K_DOWN, JUMP: pygame.K_UP,
            HIT: pygame.K_KP_4, KICK: pygame.K_KP_5, BLOCK: pygame.K_KP_6}]  # Управление 2го игрока

fighter_width = 63 * IMAGE_SCALE_VALUE
FIGHTERS_X = [WINDOW_WIDTH // 10, WINDOW_WIDTH // 10 * 9 - fighter_width]
FIGHTERS_Y = WINDOW_HEIGHT // 7 * 3

PLAYERNAMES = ('Player 1', 'Player 2')

HEALTH_BAR_INDENT = (10, 10)

FIGHT_INFO_TEXT_SIZE = 100  # Размер текста надписей "Fight!", "Player N win!"
FIGHT_INFO_TEXT_COLOR = (255, 0, 51)

PAUSE_BTN_TEXT_COLOR = (63, 37, 18)
PAUSE_BTN_TEXT_SIZE = round(36 * (WINDOW_WIDTH / 1024))
PAUSE_BTN_COLOR = (255, 43, 43)
PAUSE_BTN_SECONDARY_COLOR = (247, 148, 60)

RESTART_BTN_TEXT_COLOR = (63, 37, 18)
RESTART_BTN_TEXT_SIZE = round(36 * (WINDOW_WIDTH / 1024))
RESTART_BTN_COLOR = (247, 148, 60)
RESTART_BTN_SECONDARY_COLOR = (255, 43, 43)

fightSound = pygame.mixer.Sound('data/sounds/fight.mp3')

buttons = []
music_volume = 0.05
is_paused = False


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


def pause_or_unpause(paused_by_button=True):  # Функция для установки или сброса паузы
    global is_paused
    if is_paused:
        is_paused = False
        if paused_by_button:  # Если пауза была вызвана кнопкой
            pause_btn.set_text(text_to_surface('Pause', PAUSE_BTN_TEXT_COLOR, PAUSE_BTN_TEXT_SIZE,
                                               font_directory=FONT_DIRECTORY)[0])
    else:
        is_paused = True
        if paused_by_button:  # Если пауза была вызвана кнопкой
            pause_btn.set_text(text_to_surface('Unpause', PAUSE_BTN_TEXT_COLOR, PAUSE_BTN_TEXT_SIZE,
                                               font_directory=FONT_DIRECTORY)[0])


def game_over(winner=None):
    pause_or_unpause(False)
    if not winner:  # Ничья
        result_text = 'Draw'
    else:
        result_text = PLAYERNAMES[fighters.index(winner)] + '  ' + 'wins!'
    # Надпись результатов:
    fight_info_text, text_width, text_height = text_to_surface(result_text, FIGHT_INFO_TEXT_COLOR,
                                                               font_size=FIGHT_INFO_TEXT_SIZE,
                                                               text_shadow=True, shadow_shift=4,
                                                               font_directory=FONT_DIRECTORY,
                                                               italic=True)
    fight_info_coords = ((WINDOW_WIDTH - text_width) // 2, (WINDOW_HEIGHT - text_height) // 7 * 2)

    window.blit(fight_info_text, fight_info_coords)  # Наложение текста на поверхность

    # Создание кнопки перезапуска игры:
    restart_btn_text = text_to_surface('Play again', RESTART_BTN_TEXT_COLOR, RESTART_BTN_TEXT_SIZE,
                                       font_directory=FONT_DIRECTORY)[0]
    restart_btn = Button(restart_btn_text, RESTART_BTN_COLOR, RESTART_BTN_SECONDARY_COLOR,
                         WINDOW_WIDTH // 4, WINDOW_HEIGHT // 10, function=start_game)
    restart_btn_coords = ((WINDOW_WIDTH - restart_btn.get_size()[0]) // 2,
                          fight_info_coords[1] + text_height + 30)
    restart_btn.set_pos(restart_btn_coords)
    buttons.append(restart_btn)


# Считываем информацию из конфига:
with open(CONFIGURATION_FILE_DIRECTORY) as cfg:
    fighter1_char, fighter2_char, bg = (line for line in cfg.read().split('\n') if line.strip())


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
hp_bars = [HealthBar(f'{PLAYERNAMES[0]} ({fighter1_char})', True),
           HealthBar(f'{PLAYERNAMES[1]} ({fighter2_char})', False)]
bars_coords = (HEALTH_BAR_INDENT,
               (WINDOW_WIDTH - hp_bars[1].get_size()[0] - HEALTH_BAR_INDENT[0], 10))

# Создание кнопки паузы:
pause_btn_text = text_to_surface('Pause', PAUSE_BTN_TEXT_COLOR, PAUSE_BTN_TEXT_SIZE,
                                 font_directory=FONT_DIRECTORY)[0]
pause_btn = Button(pause_btn_text, PAUSE_BTN_COLOR, PAUSE_BTN_SECONDARY_COLOR,
                   WINDOW_WIDTH // 6, hp_bars[0].get_size()[1], function=pause_or_unpause)
pause_btn_coords = ((WINDOW_WIDTH - pause_btn.get_size()[0]) // 2, HEALTH_BAR_INDENT[1])
pause_btn.set_pos(pause_btn_coords)
buttons.append(pause_btn)

# Надпись начала битвы:
fight_info_text, text_width, text_height = text_to_surface('Fight!', FIGHT_INFO_TEXT_COLOR,
                                                           font_size=FIGHT_INFO_TEXT_SIZE,
                                                           text_shadow=True, shadow_shift=4,
                                                           font_directory=FONT_DIRECTORY,
                                                           italic=True)
fight_info_coords = ((WINDOW_WIDTH - text_width) // 2, (WINDOW_HEIGHT - text_height) // 7 * 2)

# Предварительная прорисовка:
window.blit(location, (0, 0))
all_sprites.update()
all_sprites.draw(window)
for num, bar in enumerate(hp_bars):  # Отрисовка полосок со здоровьем
    coords = bars_coords[num]
    window.blit(bar.get_surface(), coords)
window.blit(pause_btn.get_surface(), pause_btn_coords)  # Отрисовка кнопки паузы
window.blit(fight_info_text, fight_info_coords)  # Наложение текста на поверхность

fightSound.play()  # Звук Начала боя

pygame.display.flip()
pause_or_unpause(False)  # Ставим игру на паузу
frames_on_pause_count = 0

running = True
while running:
    while is_paused:  # Во время паузы ставим изменённый цикл
        if frames_on_pause_count == FPS:  # Если с момента паузы прошла 1 секунда
            pause_or_unpause(False)  # Снимаем с паузы игру
        # Обработка событий:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                for btn in buttons:
                    # Эффект наведения мыши на кнопку:
                    btn.set_under_mouse_effect(btn.check_mouse_position(event.pos))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in buttons:
                    # Проверка нажатия на кнопку:
                    if btn.check_mouse_position(event.pos):
                        btn.trigger()

        # Отрисовка кнопок:
        for btn in buttons:
            window.blit(btn.get_surface(), btn.get_pos())

        pygame.display.flip()
        clock.tick(FPS)
        frames_on_pause_count += 1
    window.blit(location, (0, 0))

    # Обработка событий:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            triggered_keys_processing(event=event)
        elif event.type == pygame.MOUSEMOTION:
            for btn in buttons:
                # Эффект наведения мыши на кнопку:
                btn.set_under_mouse_effect(btn.check_mouse_position(event.pos))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for btn in buttons:
                # Проверка нажатия на кнопку:
                if btn.check_mouse_position(event.pos):
                    btn.trigger()

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

    if pygame.sprite.collide_mask(fighters[0], fighters[1]):
        if fighters[0].check_damage_ability() is True:
            if fighters[1].check_damage_ability() is True:
                if fighters[0].animation_index > fighters[1].animation_index:
                    fighters[0].isDamaged = True
                    fighters[1].get_damage(fighters[0].get_current_actions())
                elif fighters[0].animation_index < fighters[1].animation_index:
                    fighters[1].isDamaged = True
                    fighters[0].get_damage(fighters[1].get_current_actions())
                else:
                    fighters[0].isDamaged = True
                    fighters[1].get_damage(fighters[0].get_current_actions())
                    fighters[1].isDamaged = True
                    fighters[0].get_damage(fighters[1].get_current_actions())
            else:
                fighters[0].isDamaged = True
                fighters[1].get_damage(fighters[0].get_current_actions())
        elif fighters[1].check_damage_ability() is True:
            fighters[1].isDamaged = True
            fighters[0].get_damage(fighters[1].get_current_actions())

    # Отрисовка полосок со здоровьем и их обновление
    for num, bar in enumerate(hp_bars):
        coords = bars_coords[num]
        bar.update(fighters[num].get_hp())
        window.blit(bar.get_surface(), coords)
    # Отрисовка кнопок:
    for btn in buttons:
        window.blit(btn.get_surface(), pause_btn_coords)

    # Проверка здоровья персонажей и объявление результатов при необходимости:
    if not fighters[0].get_hp() > 0 < fighters[1].get_hp():
        if fighters[0].get_hp() <= 0:
            if fighters[1].get_hp() <= 0:
                game_over()
            else:
                game_over(winner=fighters[1])
        else:
            if fighters[1].get_hp() <= 0:
                game_over(winner=fighters[0])

    # Перерисовка спрайтов:
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.flip()
    clock.tick(FPS)
