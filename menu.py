from pygame import *
from pygame.draw import *
from presset_m import *


def menu_loop(screen, bg):

    bg.blit(BackGround.image, BackGround.rect)
    finished = False

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pygame.event.get():

            if e.type == KEYDOWN and e.key == K_ESCAPE:
                finished = True

        pygame.display.update()