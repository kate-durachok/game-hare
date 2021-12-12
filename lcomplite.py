from pygame import *
from background import *

BackGroundLC = Background('bg/bg_lc.png', [0, 0])

def levelc(screen, bg):
    bg.blit(BackGroundLC.image, BackGroundLC.rect)
    finished = False

    pygame.mixer.init()
    pygame.mixer.music.load('music/lc_s.mp3')
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