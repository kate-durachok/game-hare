import pygame
from background import *
from buttons import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


BACKGROUND_COLOR = "#90EE90"
BackGroundM = Background('bg/bg_menu.png', [0, 0])

mbtn1 = Button(['buttonm/bm_l1_0.png', 'buttonm/bm_l1_1.png', 'buttonm/bm_l1_2.png'], 100, 240, 0)
mbtn2 = Button(['buttonm/bm_l2_0.png', 'buttonm/bm_l2_1.png', 'buttonm/bm_l2_2.png'], 100, 310, 0)
mbtn3 = Button(['buttonm/bm_l3_0.png', 'buttonm/bm_l3_1.png', 'buttonm/bm_l3_2.png'], 100, 380, 0)
mbtn4 = Button(['buttonm/bm_ex_0.png', 'buttonm/bm_ex_1.png', 'buttonm/bm_ex_2.png'], 100, 470, 0)