import pygame
from image_functions import load_image


WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 576
FPS = 40

GAME_BACKGROUND_DIRECTORY = 'data/game_test_background.jpg'
STAND_SPRITES_DIRECTORY = 'data/scorpion/stand.png'

FIRST_PLAYER_START_POSITION = WINDOW_WIDTH // 10, WINDOW_HEIGHT // 7 * 3
# Множитель увеличения персонажа:
SCALING_CHARACTER = 2.7

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Test fightingroom')

all_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


bg_image = load_image(GAME_BACKGROUND_DIRECTORY)
background = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
screen.blit(background, (0, 0))

scorp = load_image(STAND_SPRITES_DIRECTORY, (255, 255, 255))
scorp_w, scorp_h = scorp.get_size()
scorp = pygame.transform.scale(scorp, (round(scorp_w * SCALING_CHARACTER),
                                       round(scorp_h * SCALING_CHARACTER)))

x, y = FIRST_PLAYER_START_POSITION
scorpion_sprite = AnimatedSprite(scorp, 7, 1, x, y)

frames_count = 0
while True:
    frames_count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if frames_count % (FPS // 2) == 0:  # Смена изображения раз в полсекунды
        screen.blit(background, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
