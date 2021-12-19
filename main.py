from menu import *
import pygame as pg



def main():
    pg.init()
    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption("Hare")

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))

    menu_loop(screen, bg)
    
if __name__ == "__main__":
    main()
