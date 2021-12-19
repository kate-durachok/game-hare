from classes.background import *

BackGroundW = Background('images/bg/bg_win.png', [0, 0])


def win(screen, bg):
    """
    показывaет при завершении 3 уровня на экране картинку вы победили, звучат победные фанфары
    :param screen: screen
    :param bg: картинка png
    """
    bg.blit(BackGroundW.image, BackGroundW.rect)
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/win_s.mp3')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1, 0)

    while not finished:
        screen.blit(bg, (0, 0))
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:  # при нажатии на пробел переходим к финальным титрам
                finished = True
            if e.type == pg.QUIT:
                raise SystemExit("QUIT")
        pg.display.update()

    pg.mixer.music.stop()
