# This file contains code of game menu
import pygame


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 40


def terminate():
    pygame.quit()
    exit()


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fighting')
pygame.display.set_icon(pygame.image.load('data/icon.ico'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
