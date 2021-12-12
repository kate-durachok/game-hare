from pygame import *
from background import *

BackGroundW = Background('bg/bg_win.png', [0, 0])

def win(screen, bg):
    bg.blit(BackGroundW.image, BackGroundW.rect)
    finished = False

    pygame.mixer.init()
    pygame.mixer.music.load('music/win_s.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 0)

    while not finished:

        screen.blit(bg, (0, 0))

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_SPACE:
                finished = True
            if e.type == QUIT:
                raise SystemExit("QUIT")

        pygame.display.update()

    pygame.mixer.music.stop()