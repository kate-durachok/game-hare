from presset_l1 import *


def level1_loop(screen, bg):
    BackGroundL1, hero, hero1, hero2, btn1, btn2, btn3, btn4, btn5, btn11, btn12, btn13, btn14, btn15, btn22 = pressetl1()
    bg.blit(BackGroundL1.image, BackGroundL1.rect)
    left = right = up = down = False
    finished = False

    pygame.mixer.init()
    pygame.mixer.music.load('music/level_1.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 0)

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
            if e.type == KEYDOWN and e.key == K_RALT:
                finished = True

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

        if btn1.state == 1:
            hero1.update(left1, right1, up1, down1, screen)

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
            hero2.update(left2, right2, up2, down2, screen)

        btn22.checkMePressed(hero2)

        if btn22.state == 1:
            finished = True

        hero.draw(screen)

        pygame.display.update()

    pygame.mixer.music.stop()