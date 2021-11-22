import pygame
from pygame import *


WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "yellow"


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Hare")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    finished = False

    while not finished:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
        screen.blit(bg, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
