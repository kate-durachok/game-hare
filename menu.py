from presset_m import *
from level1 import *
from level2 import *
from level3 import *
from rules import *
from win import *
from lcomplite import *
from end import *
import pygame as pg


def menu_loop(screen, bg):

    bg.blit(BackGroundM.image, BackGroundM.rect)
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/menu_s.mp3')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1, 0)

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pg.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                finished = True
            if e.type == QUIT:
                raise SystemExit("QUIT")

        mbtn1.press()
        mbtn2.press()
        mbtn3.press()
        mbtn4.press()

        if mbtn1.state == 1:
            rules(screen, bg)
            level1_loop(screen, bg)
            levelc(screen, bg)
            mbtn1.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)
            pg.mixer.music.load('music/menu_s.mp3')
            pg.mixer.music.play(-1, 0)

        if mbtn2.state == 1:
            level2_loop(screen, bg)
            levelc(screen, bg)
            mbtn2.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)
            pg.mixer.music.load('music/menu_s.mp3')
            pg.mixer.music.play(-1, 0)

        if mbtn3.state == 1:
            level3_loop(screen, bg)
            win(screen, bg)
            end(screen, bg)
            mbtn3.state = 0
            bg.blit(BackGroundM.image, BackGroundM.rect)
            pg.mixer.music.load('music/menu_s.mp3')
            pg.mixer.music.play(-1, 0)

        if mbtn4.state == 1:
            raise SystemExit("QUIT")

        mbtn1.draw(screen)
        mbtn2.draw(screen)
        mbtn3.draw(screen)
        mbtn4.draw(screen)

        pg.display.update()

    pg.mixer.music.stop()