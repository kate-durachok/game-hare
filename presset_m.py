import pygame
from background import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

pygame.mixer.init()
pygame.mixer.music.load('music/menu_s.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1, 0)

BACKGROUND_COLOR = "#90EE90"
BackGround = Background('bg_menu.png', [0, 0])