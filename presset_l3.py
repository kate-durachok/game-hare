import pygame
from player import *
from buttons import *
from background import *


WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)



BACKGROUND_COLOR = "#90EE90"
BackGroundL3 = Background('bg/bg_l3.png', [0, 0])


hero = Player(800, 900, [0, WIN_WIDTH, 600, WIN_HEIGHT], 80, 60, 3, 6)  # создаем героя по (x,y) координатам
hero1 = Player(650, 600, [150, 650, 350, 593], 60, 40, 2, 7)
hero2 = Player(600, 350, [200, 600, 150, 343], 40, 30, 2, 8)
hero3 = Player(550, 150, [250, 550, 0, 140], 30, 20, 2, 8)

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

btn21 = Button(['buttonc/bc200.png', 'buttonc/bc201.png'], 210, 160, 0)

btn22 = Button(['buttons/1/bl10.png', 'buttons/1/bl11.png'], 370, 260, 1)
btn23 = Button(['buttons/1/br10.png', 'buttons/1/br11.png'], 490, 260, 1)
btn24 = Button(['buttons/1/bu10.png', 'buttons/1/bu11.png'], 430, 200, 1)
btn25 = Button(['buttons/1/bd10.png', 'buttons/1/bd11.png'], 430, 260, 1)

btn31 = Button(['buttonc/bc200.png', 'buttonc/bc201.png'], 260, 10, 0)

