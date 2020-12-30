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

        self.punchStand = [pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/01.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/02.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/03.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/04.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/05.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/06.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/07.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/08.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/09.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/10.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/11.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/12.png'),
                           pygame.image.load(f'data/img/characters/{self.character}/punches/serial_hand/13.png')]

        self.punchFeetFirst = [pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/01.png'),
                               pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/02.png'),
                               pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/03.png'),
                               pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/04.png'),
                               pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/05.png'),
                               pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/first/06.png')]

        self.punchFeetSecond = [pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/01.png'),
                                pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/02.png'),
                                pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/03.png'),
                                pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/04.png'),
                                pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/05.png'),
                                pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/second/06.png')]

        self.roundKick = [pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/round_kick/01.png')]

        self.punchSit = [pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/sitting/01.png'),
                         pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/sitting/02.png'),
                         pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/sitting/03.png'),
                         pygame.image.load(f'data/img/characters/{self.character}/punches/serial_feet/sitting/04.png')]

        self.blockStay = [pygame.image.load(f'data/img/characters/{self.character}/punches/block/staying/01.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/block/staying/02.png'),
                          pygame.image.load(f'data/img/characters/{self.character}/punches/block/staying/03.png')]

        self.blockSit = [pygame.image.load(f'data/img/characters/{self.character}/punches/block/sitting/01.png'),
                         pygame.image.load(f'data/img/characters/{self.character}/punches/block/sitting/02.png'),
                         pygame.image.load(f'data/img/characters/{self.character}/punches/block/sitting/03.png')]



        # self.punchJump = [pygame.image.load(f'data/img/characters/{self.character}/punches/;lf.png')]

    def beat(self):
        pass