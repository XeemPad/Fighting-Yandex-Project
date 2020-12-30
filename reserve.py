import pygame
from fighter import Fighter
from pygame.mixer import music

if __name__ == '__main__':
    pygame.init()
    size = win_width, win_height = 1280, 720
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Flex Kombat')
    pygame.display.set_icon(pygame.image.load('data/img/pngguru.com.png'))

    bg = pygame.image.load('data/img/locations/background1.jpg')
    location = pygame.Surface(size)
    location.blit(bg, (0, 0))

    music.load('data/sounds/bg_music/music_two.mp3')
    music.play(-1)

    fighterOne = Fighter('scorpion')
    print(fighterOne.health, fighterOne.speed)
    isJumpOne = False
    jumpCountOne = 10
    isJumpOne = False
    isSitOne = False
    jumpCountOne = 10
    leftOne = False
    rightOne = False
    animIndexOne = 0

    fighterTwo = Fighter('obama')
    print(fighterTwo.health, fighterTwo.speed)
    isJumpTwo = False
    jumpCountTwo = 10
    isJumpTwo = False
    isSitTwo = False
    jumpCountTwo = 10
    leftTwo = False
    rightTwo = False
    animIndexTwo = 0

    running = True

    FPS = 60
    clock = pygame.time.Clock()


    def drawWindow():
        global animIndexOne
        global animIndexTwo
        global isSitOne

        window.blit(location, (0, 0))

        if isSitOne:
            window.blit(fighterOne.sitOn, (fighterOne.x, fighterOne.y))
            isSitOne = False
        else:
            if animIndexOne + 1 >= 30:
                animIndexOne = 0
            if leftOne:
                window.blit(fighterOne.goLeft[animIndexOne // 5], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            elif rightOne:
                window.blit(fighterOne.goRight[animIndexOne // 5], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            else:
                window.blit(fighterOne.stayOn, (fighterOne.x, fighterOne.y))

        if animIndexTwo + 1 >= 30:
            animIndexTwo = 0
        if leftTwo:
            window.blit(fighterTwo.goLeft[animIndexTwo // 5], (fighterTwo.x, fighterTwo.y))
            animIndexTwo += 1
        elif rightTwo:
            window.blit(fighterTwo.goRight[animIndexTwo // 5], (fighterTwo.x, fighterTwo.y))
            animIndexTwo += 1
        else:
            window.blit(fighterTwo.stayOn, (fighterTwo.x, fighterTwo.y))

        pygame.display.update()


    while running:

        # mixer.music.load('data/sounds/bg_music/mp2.wav')
        # mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and fighterOne.x >= fighterOne.speed:
            fighterOne.x -= fighterOne.speed
            leftOne = True
            rightOne = False
        elif keys[pygame.K_d] and fighterOne.x <= win_width - (fighterOne.width + fighterOne.speed):
            fighterOne.x += fighterOne.speed
            rightOne = True
            leftOne = False
        else:
            leftOne = False
            rightOne = False
            animIndexOne = 0

        if isJumpOne is False:
            # if keys[pygame.K_UP] and y >= speed:
            #     y -= speed
            # if keys[pygame.K_DOWN] and y <= win_height - (height + speed):
            #     y += speed
            if keys[pygame.K_w]:
                isJumpOne = True
        else:
            if jumpCountOne >= -10:
                if jumpCountOne <= 0:
                    fighterOne.y += (jumpCountOne ** 2) / 2
                else:
                    fighterOne.y -= (jumpCountOne ** 2) / 2
                jumpCountOne -= 1
            else:
                isJumpOne = False
                jumpCountOne = 10

        if isSitOne is False:
            if keys[pygame.K_s]:
                isSitOne = True

        if keys[pygame.K_LEFT] and fighterTwo.x >= fighterTwo.speed:
            fighterTwo.x -= fighterTwo.speed
            leftTwo = True
            rightTwo = False
        elif keys[pygame.K_RIGHT] and fighterTwo.x <= win_width - (fighterTwo.width + fighterTwo.speed):
            fighterTwo.x += fighterTwo.speed
            rightTwo = True
            leftTwo = False
        else:
            leftTwo = False
            rightTwo = False
            animIndexTwo = 0

        if isJumpTwo is False:
            # if keys[pygame.K_UP] and y >= speed:
            #     y -= speed
            # if keys[pygame.K_DOWN] and y <= win_height - (height + speed):
            #     y += speed
            if keys[pygame.K_UP]:
                isJumpTwo = True
        else:
            if jumpCountTwo >= -10:
                if jumpCountTwo <= 0:
                    fighterTwo.y += (jumpCountTwo ** 2) / 2
                else:
                    fighterTwo.y -= (jumpCountTwo ** 2) / 2
                jumpCountTwo -= 1
            else:
                isJumpTwo = False
                jumpCountTwo = 10

        drawWindow()

        clock.tick(FPS)

pygame.quit()
