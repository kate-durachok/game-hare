from pygame import *
from background import *
from buttons import *

BackGroundE = Background('bg/bg_end.png', [0, 0])
ebtn1 = Button(['buttone/be_m_0.png', 'buttone/be_m_1.png', 'buttone/be_m_2.png'], 500, 430, 0)
ebtn2 = Button(['buttone/be_ex_0.png', 'buttone/be_ex_1.png', 'buttone/be_ex_2.png'], 500, 520, 0)

def end(screen, bg):
    bg.blit(BackGroundE.image, BackGroundE.rect)
    finished = False

    pygame.mixer.init()
    pygame.mixer.music.load('music/end_s.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 0)

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pygame.event.get():
            if e.type == QUIT:
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

        pygame.display.update()

    pygame.mixer.music.stop()