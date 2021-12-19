from presset_l2 import *
from classes.blocks import *
import time

def level2_loop(screen, bg):
    BackGroundL2, hero, hero1, hero2, btn1, btn2, btn3, btn4, btn5, btn11, btn12, btn13, btn14, btn15, btn22, WIN_WIDTH, WIN_HEIGHT, FPS = pressetl2()
    entities = pg.sprite.Group()  # Все объекты
    blocks = []  # то, во что мы будем врезаться или опираться

    entities.add(hero)
    level = [
        ".............-..................",
        ".............-..................",
        ".............-..................",
        ".............-...-..............",
        ".................-..............",
        ".................-..............",
        ".............-...-..............",
        ".............-...-..............",
        "................................",
        "................................",
        "................................",
        ".................-------........",
        "................................",
        "................................",
        "................................",
        "................................",
        "........----....................",
        "................................",
        "................................",
        "................................",
        "................................",
        "......-......................-..",
        "......-......................-..",
        "......-......................-..",
        "......-......................-..",
        "......-......................-..",
        "......-......................-..",
        "......-.........................",
        "......-.........................",
        "......-....-....................",
        "......-....-....................",
        "...........-....................",
        "...........-....................",
        "...........-....................",
        "...........-....................",
        "...........-...................."
    ]

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Block(x, y)
                entities.add(pf)
                blocks.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    bg.blit(BackGroundL2.image, BackGroundL2.rect)
    left = right = up = down = False
    finished = False

    pg.mixer.init()
    pg.mixer.music.load('music/level_2.mp3')
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1, 0)

    while not finished:
        t = time.time()

        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
                left = True
            if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
                right = True

            if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
                right = False
            if e.type == pg.KEYUP and e.key == pg.K_LEFT:
                left = False

            if e.type == pg.KEYDOWN and e.key == pg.K_UP:
                up = True
            if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
                down = True

            if e.type == pg.KEYUP and e.key == pg.K_UP:
                up = False
            if e.type == pg.KEYUP and e.key == pg.K_DOWN:
                down = False

            if e.type == pg.QUIT:
                raise SystemExit("QUIT")

            if e.type == pg.KEYDOWN and e.key == pg.K_RALT:
                finished = True

        screen.blit(bg, (0, 0))

        hero.update(left, right, up, down, screen, blocks)  # передвижение

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

        if btn1.state == 1:
            hero1.update(left1, right1, up1, down1, screen, blocks)

        btn11.checkMePressed(hero1)

        if btn11.state == 1:
            btn12.draw(screen)
            btn13.draw(screen)
            btn14.draw(screen)
            btn15.draw(screen)

            btn22.draw(screen)
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

        if btn11.state == 1:
            hero2.update(left2, right2, up2, down2, screen, blocks)

        btn22.checkMePressed(hero2)

        if btn22.state == 1:
            finished = True

        hero.draw(screen)
        for e in entities:
            state = pg.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT)
            screen.blit(e.image, e.rect.move(state.topleft))

        pg.display.update()

        dt = 1.0 / FPS - (time.time() - t)
        if dt < 0:
            dt = 0
        time.sleep(dt)

    pg.mixer.music.stop()