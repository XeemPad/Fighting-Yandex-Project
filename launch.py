import pygame
from fighter import Fighter
from pygame.mixer import music

if __name__ == '__main__':
    pygame.init()
    size = win_width, win_height = 1280, 720
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Flex Kombat')
    pygame.display.set_icon(pygame.image.load('data/img/pngguru.com.png'))

    bg = pygame.transform.scale(pygame.image.load('data/img/locations/background1.jpg'), (win_width, win_height))
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
    isBlockOne = False

    fighterTwo = Fighter('scorpion')
    print(fighterTwo.health, fighterTwo.speed)
    fighterTwo.x = win_width - fighterTwo.width
    isJumpTwo = False
    jumpCountTwo = 10
    isJumpTwo = False
    isSitTwo = False
    jumpCountTwo = 10
    leftTwo = False
    rightTwo = False
    animIndexTwo = 0
    isBlockTwo = False

    running = True

    FPS = 60
    clock = pygame.time.Clock()

    stayIndexOne = 0
    stayIndexTwo = 0

    punchStandIndexOne = 0
    punchStandIndexTwo = 0


    # def beatHim():
    #     if isSitOne is False:

    def punchStand():
        global punchStandIndexOne
        global punchStandIndexTwo

        window.blit(location, (0, 0))

        if fighterOne.x <= win_width - (fighterOne.width + fighterOne.speed):
            if punchStandIndexOne <= 5:
                fighterOne.x += fighterOne.speed
                window.blit(fighterOne.punchStand[punchStandIndexOne], (fighterOne.x, fighterOne.y))
        else:
            if punchStandIndexOne <= 5:
                window.blit(fighterOne.punchStand[punchStandIndexOne], (fighterOne.x, fighterOne.y))
        punchStandIndexOne += 1

        if fighterTwo.x <= win_width - (fighterTwo.width + fighterTwo.speed):
            if punchStandIndexTwo <= 5:
                fighterTwo.x -= fighterTwo.speed
                window.blit(fighterTwo.punchStand[punchStandIndexTwo], (fighterTwo.x, fighterTwo.y))
        else:
            if punchStandIndexTwo <= 5:
                window.blit(fighterTwo.punchStand[punchStandIndexTwo], (fighterTwo.x, fighterTwo.y))
        punchStandIndexTwo += 1

        pygame.display.update()


    def stayOnSurfaceOne():
        global stayIndexOne
        global stayIndexTwo

        window.blit(location, (0, 0))

        if stayIndexOne + 1 >= 60:
            stayIndexOne = 0
        stayIndexOne += 1
        window.blit(fighterOne.stayOn[animIndexOne // 8], (fighterOne.x, fighterOne.y))

        if stayIndexTwo + 1 >= 60:
            stayIndexTwo = 0
        stayIndexTwo += 1
        window.blit(fighterTwo.stayOn[animIndexTwo // 8], (fighterTwo.x, fighterTwo.y))


    def drawWindow():
        global animIndexOne
        global animIndexTwo
        global isSitOne
        global isSitTwo
        global isBlockOne
        global isBlockTwo

        window.blit(location, (0, 0))

        if isBlockOne:
            window.blit(location, (0, 0))
            window.blit(fighterOne.blockStay[2], (fighterOne.x, fighterOne.y))
            isBlockOne = False
        else:
            if animIndexOne + 1 >= 60:
                animIndexOne = 0
            if leftOne:
                window.blit(fighterOne.goLeft[animIndexOne // 8], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            elif rightOne:
                window.blit(fighterOne.goRight[animIndexOne // 8], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            else:
                window.blit(fighterOne.stayOn[stayIndexOne // 8], (fighterOne.x, fighterOne.y))

        if isBlockTwo:
            window.blit(location, (0, 0))
            window.blit(fighterTwo.blockStay[2], (fighterTwo.x, fighterTwo.y))
            isBlockTwo = False
        else:
            if animIndexTwo + 1 >= 60:
                animIndexTwo = 0
            if leftTwo:
                window.blit(fighterTwo.goLeft[animIndexTwo // 8], (fighterTwo.x, fighterTwo.y))
                animIndexTwo += 1
            elif rightTwo:
                window.blit(fighterTwo.goRight[animIndexTwo // 8], (fighterTwo.x, fighterTwo.y))
                animIndexTwo += 1
            else:
                window.blit(fighterTwo.stayOn[stayIndexTwo // 8], (fighterTwo.x, fighterTwo.y))

        if isSitOne:
            window.blit(fighterOne.sitOn, (fighterOne.x, fighterOne.y))
            isSitOne = False
        else:
            if animIndexOne + 1 >= 60:
                animIndexOne = 0
            if leftOne:
                window.blit(fighterOne.goLeft[animIndexOne // 8], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            elif rightOne:
                window.blit(fighterOne.goRight[animIndexOne // 8], (fighterOne.x, fighterOne.y))
                animIndexOne += 1
            else:
                window.blit(fighterOne.stayOn[stayIndexOne // 8], (fighterOne.x, fighterOne.y))

        if isSitTwo:
            window.blit(fighterTwo.sitOn, (fighterTwo.x, fighterTwo.y))
            isSitTwo = False
        else:
            if animIndexTwo + 1 >= 60:
                animIndexTwo = 0
            if leftTwo:
                window.blit(fighterTwo.goLeft[animIndexTwo // 8], (fighterTwo.x, fighterTwo.y))
                animIndexTwo += 1
            elif rightTwo:
                window.blit(fighterTwo.goRight[animIndexTwo // 8], (fighterTwo.x, fighterTwo.y))
                animIndexTwo += 1
            else:
                window.blit(fighterTwo.stayOn[stayIndexTwo // 8], (fighterTwo.x, fighterTwo.y))

        pygame.display.update()


    while running:

        stayOnSurfaceOne()

        # mixer.music.load('data/sounds/bg_music/mp2.wav')
        # mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        #######################################################################################################################
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

        if keys[pygame.K_c]:
            isBlockOne = True

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
        ################################################################################################################################
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

        if keys[pygame.K_m]:
            isBlockTwo = True

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

        if isSitTwo is False:
            if keys[pygame.K_DOWN]:
                isSitTwo = True

        drawWindow()

        clock.tick(FPS)

pygame.quit()