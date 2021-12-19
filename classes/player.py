import pyganim
from classes.blocks import *

COLOR = "#696969"
ANIMATION_DELAY = 60  # скорость смены кадров

ANIMATION_RIGHT = [[('images/hare/l_1/0/hr1.png'),
                   ('images/hare/l_1/0/hr2.png'),
                   ('images/hare/l_1/0/hr3.png'),
                   ('images/hare/l_1/0/hr4.png')], [('images/hare/l_1/1/hr10.png'),
                                            ('images/hare/l_1/1/hr11.png'),
                                            ('images/hare/l_1/1/hr12.png'),
                                            ('images/hare/l_1/1/hr13.png')], [('images/hare/l_1/2/hr20.png'),
                                                                      ('images/hare/l_1/2/hr21.png'),
                                                                      ('images/hare/l_1/2/hr22.png'),
                                                                      ('images/hare/l_1/2/hr23.png')],
                  [('images/hare/l_2/0/hr1.png'),
                   ('images/hare/l_2/0/hr2.png'),
                   ('images/hare/l_2/0/hr3.png'),
                   ('images/hare/l_2/0/hr4.png')], [('images/hare/l_2/1/hr10.png'),
                                            ('images/hare/l_2/1/hr11.png'),
                                            ('images/hare/l_2/1/hr12.png'),
                                            ('images/hare/l_2/1/hr13.png')], [('images/hare/l_2/2/hr20.png'),
                                                                      ('images/hare/l_2/2/hr21.png'),
                                                                      ('images/hare/l_2/2/hr22.png'),
                                                                      ('images/hare/l_2/2/hr23.png')],
                  [('images/hare/l_3/0/hr1.png'),
                   ('images/hare/l_3/0/hr2.png'),
                   ('images/hare/l_3/0/hr3.png'),
                   ('images/hare/l_3/0/hr4.png')], [('images/hare/l_3/1/hr10.png'),
                                            ('images/hare/l_3/1/hr11.png'),
                                            ('images/hare/l_3/1/hr12.png'),
                                            ('images/hare/l_3/1/hr13.png')], [('images/hare/l_3/2/hr20.png'),
                                                                      ('images/hare/l_3/2/hr21.png'),
                                                                      ('images/hare/l_3/2/hr22.png'),
                                                                      ('images/hare/l_3/2/hr23.png')], [('images/hare/l_3/3/hr30.png'),
                                                                                                 ('images/hare/l_3/3/hr31.png'),
                                                                                                 ('images/hare/l_3/3/hr32.png'),
                                                                                                 ('images/hare/l_3/3/hr33.png')]]
ANIMATION_LEFT = [[('images/hare/l_1/0/hl1.png'),
                  ('images/hare/l_1/0/hl2.png'),
                  ('images/hare/l_1/0/hl3.png'),
                  ('images/hare/l_1/0/hl4.png')], [('images/hare/l_1/1/hl10.png'),
                                            ('images/hare/l_1/1/hl11.png'),
                                            ('images/hare/l_1/1/hl12.png'),
                                            ('images/hare/l_1/1/hl13.png')], [('images/hare/l_1/2/hl20.png'),
                                                                       ('images/hare/l_1/2/hl21.png'),
                                                                       ('images/hare/l_1/2/hl22.png'),
                                                                       ('images/hare/l_1/2/hl23.png')],
                 [('images/hare/l_2/0/hl1.png'),
                  ('images/hare/l_2/0/hl2.png'),
                  ('images/hare/l_2/0/hl3.png'),
                  ('images/hare/l_2/0/hl4.png')], [('images/hare/l_2/1/hl10.png'),
                                            ('images/hare/l_2/1/hl11.png'),
                                            ('images/hare/l_2/1/hl12.png'),
                                            ('images/hare/l_2/1/hl13.png')], [('images/hare/l_2/2/hl20.png'),
                                                                       ('images/hare/l_2/2/hl21.png'),
                                                                       ('images/hare/l_2/2/hl22.png'),
                                                                       ('images/hare/l_2/2/hl23.png')],
                 [('images/hare/l_3/0/hl1.png'),
                  ('images/hare/l_3/0/hl2.png'),
                  ('images/hare/l_3/0/hl3.png'),
                  ('images/hare/l_3/0/hl4.png')], [('images/hare/l_3/1/hl10.png'),
                                            ('images/hare/l_3/1/hl11.png'),
                                            ('images/hare/l_3/1/hl12.png'),
                                            ('images/hare/l_3/1/hl13.png')], [('images/hare/l_3/2/hl20.png'),
                                                                       ('images/hare/l_3/2/hl21.png'),
                                                                       ('images/hare/l_3/2/hl22.png'),
                                                                       ('images/hare/l_3/2/hl23.png')], [('images/hare/l_3/3/hl30.png'),
                                                                                                 ('images/hare/l_3/3/hl31.png'),
                                                                                                 ('images/hare/l_3/3/hl32.png'),
                                                                                                 ('images/hare/l_3/3/hl33.png')]]
ANIMATION_UP = [[('images/hare/l_1/0/hu1.png'),
                ('images/hare/l_1/0/hu1.png'),
                ('images/hare/l_1/0/hu2.png'),
                ('images/hare/l_1/0/hu2.png')], [('images/hare/l_1/1/hu10.png'),
                                          ('images/hare/l_1/1/hu10.png'),
                                          ('images/hare/l_1/1/hu11.png'),
                                          ('images/hare/l_1/1/hu11.png')], [('images/hare/l_1/2/hu20.png'),
                                                                     ('images/hare/l_1/2/hu20.png'),
                                                                     ('images/hare/l_1/2/hu21.png'),
                                                                     ('images/hare/l_1/2/hu21.png')],
               [('images/hare/l_2/0/hu1.png'),
                ('images/hare/l_2/0/hu1.png'),
                ('images/hare/l_2/0/hu2.png'),
                ('images/hare/l_2/0/hu2.png')], [('images/hare/l_2/1/hu10.png'),
                                          ('images/hare/l_2/1/hu10.png'),
                                          ('images/hare/l_2/1/hu11.png'),
                                          ('images/hare/l_2/1/hu11.png')], [('images/hare/l_2/2/hu20.png'),
                                                                     ('images/hare/l_2/2/hu20.png'),
                                                                     ('images/hare/l_2/2/hu21.png'),
                                                                     ('images/hare/l_2/2/hu21.png')],
               [('images/hare/l_3/0/hu1.png'),
                ('images/hare/l_3/0/hu1.png'),
                ('images/hare/l_3/0/hu2.png'),
                ('images/hare/l_3/0/hu2.png')], [('images/hare/l_3/1/hu10.png'),
                                          ('images/hare/l_3/1/hu10.png'),
                                          ('images/hare/l_3/1/hu11.png'),
                                          ('images/hare/l_3/1/hu11.png')], [('images/hare/l_3/2/hu20.png'),
                                                                     ('images/hare/l_3/2/hu20.png'),
                                                                     ('images/hare/l_3/2/hu21.png'),
                                                                     ('images/hare/l_3/2/hu21.png')], [('images/hare/l_3/3/hu30.png'),
                                                                                                ('images/hare/l_3/3/hu30.png'),
                                                                                                ('images/hare/l_3/3/hu31.png'),
                                                                                                ('images/hare/l_3/3/hu31.png')]]
ANIMATION_DOWN = [[('images/hare/l_1/0/hd1.png'),
                   ('images/hare/l_1/0/hd1.png'),
                   ('images/hare/l_1/0/hd2.png'),
                   ('images/hare/l_1/0/hd2.png')], [('images/hare/l_1/1/hd10.png'),
                                             ('images/hare/l_1/1/hd10.png'),
                                             ('images/hare/l_1/1/hd11.png'),
                                             ('images/hare/l_1/1/hd11.png')], [('images/hare/l_1/2/hd20.png'),
                                                                        ('images/hare/l_1/2/hd20.png'),
                                                                        ('images/hare/l_1/2/hd21.png'),
                                                                        ('images/hare/l_1/2/hd21.png')],
                 [('images/hare/l_2/0/hd1.png'),
                  ('images/hare/l_2/0/hd1.png'),
                  ('images/hare/l_2/0/hd2.png'),
                  ('images/hare/l_2/0/hd2.png')], [('images/hare/l_2/1/hd10.png'),
                                            ('images/hare/l_2/1/hd10.png'),
                                            ('images/hare/l_2/1/hd11.png'),
                                            ('images/hare/l_2/1/hd11.png')], [('images/hare/l_2/2/hd20.png'),
                                                                       ('images/hare/l_2/2/hd20.png'),
                                                                       ('images/hare/l_2/2/hd21.png'),
                                                                       ('images/hare/l_2/2/hd21.png')],
                 [('images/hare/l_3/0/hd1.png'),
                  ('images/hare/l_3/0/hd1.png'),
                  ('images/hare/l_3/0/hd2.png'),
                  ('images/hare/l_3/0/hd2.png')], [('images/hare/l_3/1/hd10.png'),
                                            ('images/hare/l_3/1/hd10.png'),
                                            ('images/hare/l_3/1/hd11.png'),
                                            ('images/hare/l_3/1/hd11.png')], [('images/hare/l_3/2/hd20.png'),
                                                                       ('images/hare/l_3/2/hd20.png'),
                                                                       ('images/hare/l_3/2/hd21.png'),
                                                                       ('images/hare/l_3/2/hd21.png')], [('images/hare/l_3/3/hd30.png'),
                                                                                                  ('images/hare/l_3/3/hd30.png'),
                                                                                                  ('images/hare/l_3/3/hd31.png'),
                                                                                                  ('images/hare/l_3/3/hd31.png')]]
ANIMATION_STAY = [(('images/hare/l_1/0/hd1.png'), ANIMATION_DELAY),
                  (('images/hare/l_1/1/hd10.png'), ANIMATION_DELAY),
                  (('images/hare/l_1/2/hd20.png'), ANIMATION_DELAY),
                  (('images/hare/l_2/0/hd1.png'), ANIMATION_DELAY),
                  (('images/hare/l_2/1/hd10.png'), ANIMATION_DELAY),
                  (('images/hare/l_2/2/hd20.png'), ANIMATION_DELAY),
                  (('images/hare/l_3/0/hd1.png'), ANIMATION_DELAY),
                  (('images/hare/l_3/1/hd10.png'), ANIMATION_DELAY),
                  (('images/hare/l_3/2/hd20.png'), ANIMATION_DELAY),
                  (('images/hare/l_3/3/hd30.png'), ANIMATION_DELAY)]


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, borders, width=80, height=60, speed=3, number=0):
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.vx = 0
        self.vy = 0
        self.number = number
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = pg.Surface((width, height))
        self.image.fill(pg.Color(COLOR))
        self.rect = pg.Rect(x, y, width, height)  # прямоугольный объект
        self.borders = borders
        self.image.set_colorkey(pg.Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT[self.number]:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT[self.number]:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        #        Анимация движения вверх
        boltAnim = []
        for anim in ANIMATION_UP[self.number]:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimUp = pyganim.PygAnimation(boltAnim)
        self.boltAnimUp.play()

        #        Анимация движения вниз
        boltAnim = []
        for anim in ANIMATION_DOWN[self.number]:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDown = pyganim.PygAnimation(boltAnim)
        self.boltAnimDown.play()

        self.boltAnimStay = pyganim.PygAnimation([ANIMATION_STAY[self.number]])
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        #self.grass_sound = mixer.Sound(path.join('music/grass.wav'))

    def update(self, left, right, up, down, screen, platforms=[]):

        if left:
            self.vx = -self.speed
            self.image.fill(pg.Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_LEFT[self.number][0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if right:
            self.vx = self.speed
            self.image.fill(pg.Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_RIGHT[self.number][0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if up:
            self.vy = -self.speed
            self.image.fill(pg.Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_UP[self.number][0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if down:
            self.vy = self.speed
            self.image.fill(pg.Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_DOWN[self.number][0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if not (up or down or left or right):
            self.vy = 0
            self.vx = 0
            self.image.fill(pg.Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

        self.rect.x += self.vx
        self.collide(self.vx, 0, platforms)
        self.rect.y += self.vy
        self.collide(0, self.vy, platforms)

        if self.rect.x + self.rect.width >= self.borders[1]:
            self.rect.x = self.borders[1] - self.rect.width

        if self.rect.x <= self.borders[0]:
            self.rect.x = self.borders[0]

        if self.rect.y + self.rect.height >= self.borders[3]:
            self.rect.y = self.borders[3] - self.rect.height

        if self.rect.y <= self.borders[2]:
            self.rect.y = self.borders[2]

    def collide(self, xv, yv, platforms):
        for p in platforms:
            if pg.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xv > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xv < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yv > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.yv = 0  # и энергия падения пропадает

                if yv < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yv = 0  # и энергия прыжка пропадает

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))


