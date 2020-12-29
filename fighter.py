import pygame


class Fighter():
    def __init__(self, character):
        self.width = 104
        self.height = 150
        self.speed = 7
        self.character = character
        self.health = 100

        self.x = 0
        self.y = 720 - self.height - 100

        self.goRight = [pygame.image.load(f'data/img/characters/{self.character}/pygame_right_1.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_2.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_3.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_4.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_5.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_6.png')]

        self.goLeft = [pygame.image.load(f'data/img/characters/{self.character}/pygame_left_1.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_2.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_3.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_4.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_5.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_6.png')]

        self.stayOn = pygame.image.load(f'data/img/characters/{self.character}/stay.png')

    def beat(self):
        pass
