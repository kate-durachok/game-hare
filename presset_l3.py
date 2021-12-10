import pygame
from player import *
from buttons import *
from background import *

def pressetl3():
    WIN_WIDTH = 800
    WIN_HEIGHT = 900
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)



    BACKGROUND_COLOR = "#90EE90"
    BackGroundL3 = Background('bg/bg_l3.png', [0, 0])


    hero = Player(800, 900, [0, WIN_WIDTH, 600, WIN_HEIGHT], 80, 60, 3, 6)  # создаем героя по (x,y) координатам
    hero1 = Player(650, 600, [150, 650, 350, 593], 60, 40, 2, 7)
    hero2 = Player(600, 350, [200, 600, 150, 343], 40, 30, 1, 8)
    hero3 = Player(550, 150, [250, 550, 0, 140], 30, 20, 1, 9)

    btn1 = Button(['buttonc/bc0.png', 'buttonc/bc1.png'], 20, 620, 0)

    btn2 = Button(['buttons/bl0.png', 'buttons/bl1.png'], 400, 760, 1)
    btn3 = Button(['buttons/br0.png', 'buttons/br1.png'], 560, 760, 1)
    btn4 = Button(['buttons/bu0.png', 'buttons/bu1.png'], 480, 680, 1)
    btn5 = Button(['buttons/bd0.png', 'buttons/bd1.png'], 480, 760, 1)

    btn11 = Button(['buttonc/bc10.png', 'buttonc/bc11.png'], 160, 360, 0)

    btn12 = Button(['buttons/1/bl10.png', 'buttons/1/bl11.png'], 370, 500, 1)
    btn13 = Button(['buttons/1/br10.png', 'buttons/1/br11.png'], 490, 500, 1)
    btn14 = Button(['buttons/1/bu10.png', 'buttons/1/bu11.png'], 430, 440, 1)
    btn15 = Button(['buttons/1/bd10.png', 'buttons/1/bd11.png'], 430, 500, 1)

    btn21 = Button(['buttonc/bc20.png', 'buttonc/bc21.png'], 210, 160, 0)

    btn22 = Button(['buttons/2/bl20.png', 'buttons/2/bl21.png'], 343, 270, 1)
    btn23 = Button(['buttons/2/br20.png', 'buttons/2/br21.png'], 423, 270, 1)
    btn24 = Button(['buttons/2/bu20.png', 'buttons/2/bu21.png'], 383, 230, 1)
    btn25 = Button(['buttons/2/bd20.png', 'buttons/2/bd21.png'], 383, 270, 1)

    btn31 = Button(['buttonc/bc200.png', 'buttonc/bc201.png'], 260, 10, 0)

    return BackGroundL3, hero, hero1, hero2, hero3, btn1, btn2, btn3, btn4, btn5, btn11, btn12, btn13, btn14, btn15, btn21, btn22, btn23, btn24, btn25, btn31

