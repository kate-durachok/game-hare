from classes.background import *

BackGroundR = Background('images/bg/bg_rules.png', [0, 0])


def rules(screen, bg):
    bg.blit(BackGroundR.image, BackGroundR.rect)
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/menu_s.mp3')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1, 0)

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                finished = True
            if e.type == pg.QUIT:
                raise SystemExit("QUIT")

        pg.display.update()

    pg.mixer.music.stop()