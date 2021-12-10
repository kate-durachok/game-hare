from pygame import *
from pygame.draw import *
from presset_m import *
from time import sleep
from level1 import *
from level2 import *
from level3 import *


def menu_loop(screen, bg):

    bg.blit(BackGroundM.image, BackGroundM.rect)
    finished = False

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                finished = True
                pygame.mixer.music.stop()
            if e.type == QUIT:
                raise SystemExit("QUIT")

        mbtn1.press()
        mbtn2.press()
        mbtn3.press()
        mbtn4.press()

        if mbtn1.state == 1:
            level1_loop(screen, bg)
            pygame.mixer.music.stop()
            mbtn1.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)


        if mbtn2.state == 1:
            level2_loop(screen, bg)
            pygame.mixer.music.stop()
            mbtn2.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)

        if mbtn3.state == 1:
            level3_loop(screen, bg)
            pygame.mixer.music.stop()
            mbtn3.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)

        if mbtn4.state == 1:
            raise SystemExit("QUIT")

        mbtn1.draw(screen)
        mbtn2.draw(screen)
        mbtn3.draw(screen)
        mbtn4.draw(screen)

        pygame.display.update()
