import pygame
from player import *
from buttons import *
from background import *

WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#90EE90"
BackGround = Background('bg.png', [0, 0])

pygame.mixer.init()
pygame.mixer.music.load('music/game_s.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Hare")

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.blit(BackGround.image, BackGround.rect)

    finished = False

    hero = Player(800, 800, [0, WIN_WIDTH, 500, WIN_HEIGHT], 80, 60, 3, 0)  # создаем героя по (x,y) координатам
    left = right = up = down = False  # по умолчанию - стоим
    hero1 = Player(530, 450, [200, 600, 200, 500], 60, 40, 2, 1)
    left1 = right1 = up1 = down1 = False  # по умолчанию - стоим
    hero2 = Player(350, 100, [275, 525, 0, 200], 40, 30, 1, 2)
    left2 = right2 = up2 = down2 = False  # по умолчанию - стоим


    btn1 = Button(['buttonc/bc0.png', 'buttonc/bc1.png'], 100, 520, 0)

    btn2 = Button(['buttons/bl0.png', 'buttons/bl1.png'], 400, 700, 1)
    btn3 = Button(['buttons/br0.png', 'buttons/br1.png'], 560, 700, 1)
    btn4 = Button(['buttons/bu0.png', 'buttons/bu1.png'], 480, 620, 1)
    btn5 = Button(['buttons/bd0.png', 'buttons/bd1.png'], 480, 700, 1)

    btn11 = Button(['buttonc/bc10.png', 'buttonc/bc11.png'], 220, 220, 0)

    btn12 = Button(['buttons/1/bl10.png', 'buttons/1/bl11.png'], 380, 410, 1)
    btn13 = Button(['buttons/1/br10.png', 'buttons/1/br11.png'], 500, 410, 1)
    btn14 = Button(['buttons/1/bu10.png', 'buttons/1/bu11.png'], 440, 350, 1)
    btn15 = Button(['buttons/1/bd10.png', 'buttons/1/bd11.png'], 440, 410, 1)

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
        btn1.draw(screen)

        if btn1.state == 1:
            btn2.draw(screen)
            btn3.draw(screen)
            btn4.draw(screen)
            btn5.draw(screen)

        btn2.checkMePressed(hero)
        btn3.checkMePressed(hero)
        btn4.checkMePressed(hero)
        btn5.checkMePressed(hero)



        if btn2.checkMePressed(hero) == 1:
            left1 = True
        else:
            left1 = False

        if btn3.checkMePressed(hero) == 1:
            right1 = True
        else:
            right1 = False

        if btn4.checkMePressed(hero) == 1:
            up1 = True
        else:
            up1 = False

        if btn5.checkMePressed(hero) == 1:
            down1 = True
        else:
            down1 = False

        hero1.update(left1, right1, up1, down1, screen)

        btn11.checkMePressed(hero1)

        if btn11.state == 1:
            btn12.draw(screen)
            btn13.draw(screen)
            btn14.draw(screen)
            btn15.draw(screen)

            hero2.draw(screen)


        if btn1.state == 1:
            btn11.draw(screen)
            hero1.draw(screen)

        btn12.checkMePressed(hero1)
        btn13.checkMePressed(hero1)
        btn14.checkMePressed(hero1)
        btn15.checkMePressed(hero1)


        if btn12.checkMePressed(hero1) == 1:
            left2 = True
        else:
            left2 = False

        if btn13.checkMePressed(hero1) == 1:
            right2 = True
        else:
            right2 = False

        if btn14.checkMePressed(hero1) == 1:
            up2 = True
        else:
            up2 = False

        if btn15.checkMePressed(hero1) == 1:
            down2 = True
        else:
            down2 = False

        hero2.update(left2, right2, up2, down2, screen)


        hero.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
