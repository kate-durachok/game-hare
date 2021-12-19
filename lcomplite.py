from background import *

BackGroundLC = Background('bg/bg_lc.png', [0, 0])

def levelc(screen, bg):
    bg.blit(BackGroundLC.image, BackGroundLC.rect)
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/lc_s.mp3')
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