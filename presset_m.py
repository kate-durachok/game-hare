from classes.background import *
from classes.buttons import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


BACKGROUND_COLOR = "#90EE90"
BackGroundM = Background('images/bg/bg_menu.png', [0, 0])


mbtn1 = Button(['images/buttonm/bm_l1_0.png', 'images/buttonm/bm_l1_1.png', 'images/buttonm/bm_l1_2.png'], 60, 240, 0)  # кнопка для перехода к 1 уровню
mbtn2 = Button(['images/buttonm/bm_l2_0.png', 'images/buttonm/bm_l2_1.png', 'images/buttonm/bm_l2_2.png'], 60, 310, 0)  # кнопка для перехода ко 2 уровню
mbtn3 = Button(['images/buttonm/bm_l3_0.png', 'images/buttonm/bm_l3_1.png', 'images/buttonm/bm_l3_2.png'], 60, 380, 0)  # кнопка для перехода к 3 уровню
mbtn4 = Button(['images/buttonm/bm_ex_0.png', 'images/buttonm/bm_ex_1.png', 'images/buttonm/bm_ex_2.png'], 60, 470, 0)  # кнопка для выхода из игры