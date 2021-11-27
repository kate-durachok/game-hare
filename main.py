import pygame
from game import *
from menu import *



def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Hare")

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))

    menu_loop(screen, bg)
    game_loop(screen, bg)
    menu_loop(screen, bg)



if __name__ == "__main__":
    main()
