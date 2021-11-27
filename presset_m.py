import pygame
from background import *
from buttons import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

pygame.mixer.init()
pygame.mixer.music.load('music/menu_s.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1, 0)

BACKGROUND_COLOR = "#90EE90"
BackGround = Background('bg_menu.png', [0, 0])

mbtn1 = Button(['buttonm/bm_l1_0.png', 'buttonm/bm_l1_1.png', 'buttonm/bm_l1_2.png'], 100, 240, 0)
mbtn2 = Button(['buttonm/bm_l2_0.png', 'buttonm/bm_l2_1.png', 'buttonm/bm_l2_2.png'], 100, 310, 0)
mbtn3 = Button(['buttonm/bm_l3_0.png', 'buttonm/bm_l3_1.png', 'buttonm/bm_l3_2.png'], 100, 380, 0)
mbtn4 = Button(['buttonm/bm_ex_0.png', 'buttonm/bm_ex_1.png', 'buttonm/bm_ex_2.png'], 100, 470, 0)