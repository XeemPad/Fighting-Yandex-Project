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
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_6.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_7.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_8.png'),
                        pygame.image.load(f'data/img/characters/{self.character}/pygame_right_9.png')]

        self.goLeft = [pygame.image.load(f'data/img/characters/{self.character}/pygame_left_1.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_2.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_3.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_4.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_5.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_6.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_7.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_8.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/pygame_left_9.png')]

        self.stayOn = [pygame.image.load(f'data/img/characters/{self.character}/idle1.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle2.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle3.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle4.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle5.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle6.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle7.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle8.png'),
                       pygame.image.load(f'data/img/characters/{self.character}/idle9.png')]

        self.sitOn = pygame.image.load(f'data/img/characters/{self.character}/sit.png')

    def beat(self):
        pass
