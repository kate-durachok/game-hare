from classes.background import *
from classes.buttons import *

BackGroundE = Background('images/bg/bg_end.png', [0, 0])
ebtn1 = Button(['images/buttone/be_m_0.png', 'images/buttone/be_m_1.png', 'images/buttone/be_m_2.png'], 500, 430, 0)  # кнопка для возвращения в меню
ebtn2 = Button(['images/buttone/be_ex_0.png', 'images/buttone/be_ex_1.png', 'images/buttone/be_ex_2.png'], 500, 520, 0)  # кнопка выхода из игры


def end(screen, bg):
    """
    показывает при завершении 3 уровня картинку с авторами и звучит умиротворяющая музыка
    :param screen: screen
    :param bg: картинка png
    """
    bg.blit(BackGroundE.image, BackGroundE.rect)
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/end_s.mp3')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1, 0)

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise SystemExit("QUIT")

        ebtn1.press()
        ebtn2.press()

        if ebtn1.state == 1:
            finished = True
            ebtn1.state = 0

        if ebtn2.state == 1:
            raise SystemExit("QUIT")

        ebtn1.draw(screen)
        ebtn2.draw(screen)

        pg.display.update()

    pg.mixer.music.stop()
