from classes.player import *
from classes.buttons import *
from classes.background import *

def pressetl3():
    """
    много всяких штук для 3го уровня, оформлена как функция. чтобы при перезапуске параметры сбрасывались
    :return: параметры начала 3го уровня
    """
    WIN_WIDTH = 800
    WIN_HEIGHT = 900
    FPS = 60
    BackGroundL3 = Background('images/bg/bg_l3.png', [0, 0])

    hero = Player(800, 900, [0, WIN_WIDTH, 600, WIN_HEIGHT], 80, 60, 3, 6)  # создаем героев по (x,y) координатам
    hero1 = Player(650, 600, [150, 650, 350, 593], 60, 40, 2, 7)
    hero2 = Player(600, 350, [200, 600, 150, 343], 40, 30, 1, 8)
    hero3 = Player(510, 115, [250, 550, 0, 140], 30, 20, 1, 9)

    btn1 = Button(['images/buttonc/bc0.png', 'images/buttonc/bc1.png'], 20, 620, 0)  # кнопка для создания hero1 и кнопок на его поле

    btn2 = Button(['images/buttons/bl0.png', 'images/buttons/bl1.png'], 400, 760, 1)  # кнопка движения влево для игрока hero1
    btn3 = Button(['images/buttons/br0.png', 'images/buttons/br1.png'], 560, 760, 1)  # кнопка движения вправо для игрока hero1
    btn4 = Button(['images/buttons/bu0.png', 'images/buttons/bu1.png'], 480, 680, 1)  # кнопка движения вверх для игрока hero1
    btn5 = Button(['images/buttons/bd0.png', 'images/buttons/bd1.png'], 480, 760, 1)  # кнопка движения вниз для игрока hero1

    btn11 = Button(['images/buttonc/bc10.png', 'images/buttonc/bc11.png'], 160, 360, 0)  # кнопка для создания hero2 и кнопок на его поле

    btn12 = Button(['images/buttons/1/bl10.png', 'images/buttons/1/bl11.png'], 370, 500, 1)  # кнопка движения влево для игрока hero2
    btn13 = Button(['images/buttons/1/br10.png', 'images/buttons/1/br11.png'], 490, 500, 1)  # кнопка движения вправо для игрока hero2
    btn14 = Button(['images/buttons/1/bu10.png', 'images/buttons/1/bu11.png'], 430, 440, 1)  # кнопка движения вверх для игрока hero2
    btn15 = Button(['images/buttons/1/bd10.png', 'images/buttons/1/bd11.png'], 430, 500, 1)  # кнопка движения вниз для игрока hero2

    btn21 = Button(['images/buttonc/bc20.png', 'images/buttonc/bc21.png'], 210, 160, 0)  # кнопка для создания hero3 и кнопок на его поле

    btn22 = Button(['images/buttons/2/bl20.png', 'images/buttons/2/bl21.png'], 343, 270, 1)  # кнопка движения влево для игрока hero3
    btn23 = Button(['images/buttons/2/br20.png', 'images/buttons/2/br21.png'], 423, 270, 1)  # кнопка движения вправо для игрока hero3
    btn24 = Button(['images/buttons/2/bu20.png', 'images/buttons/2/bu21.png'], 383, 230, 1)  # кнопка движения вверх для игрока hero3
    btn25 = Button(['images/buttons/2/bd20.png', 'images/buttons/2/bd21.png'], 383, 270, 1)  # кнопка движения вниз для игрока hero3

    btn31 = Button(['images/buttonc/bc200.png', 'images/buttonc/bc201.png'], 260, 10, 0)  # конец уровня и игры

    return BackGroundL3, hero, hero1, hero2, hero3, btn1, btn2, btn3, btn4, btn5, btn11, btn12, btn13, btn14, btn15, btn21, btn22, btn23, btn24, btn25, btn31, FPS

