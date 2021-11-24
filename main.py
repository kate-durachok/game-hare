import pygame
from player import *
from buttons import *
from background import *


WIN_WIDTH = 800
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#90EE90"
BackGround = Background('bg.png', [0,0])


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Hare")

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.blit(BackGround.image, BackGround.rect)

    finished = False

    hero = Player(55, 800)  # создаем героя по (x,y) координатам
    left = right = up = down = False  # по умолчанию - стоим

    btn1 = Button(200, 200, 70, 70)

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
        hero.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
