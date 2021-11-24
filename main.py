import pygame
from player import *
from buttons import *
from background import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#90EE90"
BackGround = Background('bg.png', [0, 0])


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Hare")

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.blit(BackGround.image, BackGround.rect)

    finished = False

    hero = Player(55, 800, [0, WIN_WIDTH, 500, WIN_HEIGHT], 80, 60, 3, 0)  # создаем героя по (x,y) координатам
    left = right = up = down = False  # по умолчанию - стоим
    hero2 = Player(300, 300, [0, WIN_WIDTH, 0, 500], 60, 40, 2, 1)

    btn1 = Button(['buttonc/bc0.png', 'buttonc/bc1.png'], 100, 500, 0)
    btn2 = Button(['buttons/bl0.png', 'buttons/bl1.png'], 400, 700, 1)
    btn3 = Button(['buttons/br0.png', 'buttons/br1.png'], 560, 700, 1)
    btn4 = Button(['buttons/bu0.png', 'buttons/bu1.png'], 480, 620, 1)
    btn5 = Button(['buttons/bd0.png', 'buttons/bd1.png'], 480, 700, 1)

    while not finished:

        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False

            if e.type == QUIT:
                raise SystemExit("QUIT")

        screen.blit(bg, (0, 0))

        hero.update(left, right, up, down, screen)  # передвижение

        btn1.checkMePressed(hero)
        btn2.checkMePressed(hero)
        btn3.checkMePressed(hero)
        btn4.checkMePressed(hero)
        btn5.checkMePressed(hero)

        if btn1.state == 1:
            hero2.draw(screen)

        left2 = right2 = up2 = down2 = False  # по умолчанию - стоим

        if btn2.checkMePressed(hero) == 1:
            left2 = True
        else:
            left2 = False

        if btn3.checkMePressed(hero) == 1:
            right2 = True
        else:
            right2 = False

        if btn4.checkMePressed(hero) == 1:
            up2 = True
        else:
            up2 = False

        if btn5.checkMePressed(hero) == 1:
            down2 = True
        else:
            down2 = False

        hero2.update(left2, right2, up2, down2, screen)

        btn1.draw(screen)
        btn2.draw(screen)
        btn3.draw(screen)
        btn4.draw(screen)
        btn5.draw(screen)

        hero.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
