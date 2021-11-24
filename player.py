from pygame import *
import pyganim
import os

COLOR = "#696969"
ANIMATION_DELAY = 30  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('hare/hr1.png'),
                   ('hare/hr2.png'),
                   ('hare/hr3.png'),
                   ('hare/hr4.png')]
ANIMATION_LEFT = [('hare/hl1.png'),
                  ('hare/hl2.png'),
                  ('hare/hl3.png'),
                  ('hare/hl4.png')]
ANIMATION_UP = [('hare/hu1.png'),
                ('hare/hu1.png'),
                ('hare/hu2.png'),
                ('hare/hu2.png')]
ANIMATION_DOWN = [('hare/hd1.png'),
                  ('hare/hd1.png'),
                  ('hare/hd2.png'),
                  ('hare/hd2.png')]
ANIMATION_STAY = [(('hare/hd1.png'), ANIMATION_DELAY)]


class Player(sprite.Sprite):
    def __init__(self, x, y, borders, width=80, height=60, speed=3,):
        sprite.Sprite.__init__(self)
        self.speed = speed
        self.vx = 0
        self.vy = 0
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((width, height))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, width, height)  # прямоугольный объект
        self.borders = borders
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        #        Анимация движения вверх
        boltAnim = []
        for anim in ANIMATION_UP:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimUp = pyganim.PygAnimation(boltAnim)
        self.boltAnimUp.play()
        #        Анимация движения вниз
        boltAnim = []
        for anim in ANIMATION_DOWN:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDown = pyganim.PygAnimation(boltAnim)
        self.boltAnimDown.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

    def update(self, left, right, up, down, screen):
        if left:
            self.vx = -self.speed
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_LEFT[0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if right:
            self.vx = self.speed
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_RIGHT[0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if up:
            self.vy = -self.speed
            self.image.fill(Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_UP[0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if down:
            self.vy = self.speed
            self.image.fill(Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))
            self.boltAnimStay = pyganim.PygAnimation([(ANIMATION_DOWN[0], ANIMATION_DELAY)])
            self.boltAnimStay.play()

        if not (up or down or left or right):
            self.vy = 0
            self.vx = 0
            self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x + self.rect.width >= self.borders[1]:
            self.rect.x = self.borders[1] - self.rect.width

        if self.rect.x <= self.borders[0]:
            self.rect.x = self.borders[0]

        if self.rect.y + self.rect.height >= self.borders[3]:
            self.rect.y = self.borders[3] - self.rect.height

        if self.rect.y <= self.borders[2]:
            self.rect.y = self.borders[2]

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
