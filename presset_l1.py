import pygame
from player import *
from buttons import *
from background import *

def pressetl1():
    WIN_WIDTH = 800
    WIN_HEIGHT = 900
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)



    BACKGROUND_COLOR = "#90EE90"
    BackGroundL1 = Background('bg/bg_l1.png', [0, 0])


    hero = Player(800, 800, [0, WIN_WIDTH, 500, WIN_HEIGHT], 80, 60, 3, 0)  # создаем героя по (x,y) координатам
    hero1 = Player(530, 450, [200, 600, 200, 500], 60, 40, 2, 1)
    hero2 = Player(450, 150, [275, 525, 0, 200], 40, 30, 1, 2)

    btn1 = Button(['buttonc/bc0.png', 'buttonc/bc1.png'], 20, 520, 0)

    btn2 = Button(['buttons/bl0.png', 'buttons/bl1.png'], 400, 700, 1)
    btn3 = Button(['buttons/br0.png', 'buttons/br1.png'], 560, 700, 1)
    btn4 = Button(['buttons/bu0.png', 'buttons/bu1.png'], 480, 620, 1)
    btn5 = Button(['buttons/bd0.png', 'buttons/bd1.png'], 480, 700, 1)

    btn11 = Button(['buttonc/bc10.png', 'buttonc/bc11.png'], 220, 220, 0)

    btn12 = Button(['buttons/1/bl10.png', 'buttons/1/bl11.png'], 370, 410, 1)
    btn13 = Button(['buttons/1/br10.png', 'buttons/1/br11.png'], 490, 410, 1)
    btn14 = Button(['buttons/1/bu10.png', 'buttons/1/bu11.png'], 430, 350, 1)
    btn15 = Button(['buttons/1/bd10.png', 'buttons/1/bd11.png'], 430, 410, 1)

    btn22 = Button(['buttonc/bc200.png', 'buttonc/bc201.png'], 290, 20, 0)

    return BackGroundL1, hero, hero1, hero2, btn1, btn2, btn3, btn4, btn5, btn11, btn12, btn13, btn14, btn15, btn22
