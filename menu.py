from pygame import *
from pygame.draw import *
from presset_m import *
from time import sleep


def menu_loop(screen, bg):

    bg.blit(BackGround.image, BackGround.rect)
    finished = False

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                finished = True
                pygame.mixer.music.stop()
            if e.type == QUIT:
                raise SystemExit("QUIT")

        mbtn1.Press()
        mbtn2.Press()
        mbtn3.Press()
        mbtn4.Press()

        if mbtn2.state == 1:
            finished = True
            pygame.mixer.music.stop()

        if mbtn4.state == 1:
            raise SystemExit("QUIT")

        mbtn1.draw(screen)
        mbtn2.draw(screen)
        mbtn3.draw(screen)
        mbtn4.draw(screen)

        pygame.display.update()