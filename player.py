from pygame import *
import pyganim
import os

COLOR = "#696969"
'''ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/hare/hr1.png' % ICON_DIR),
                   ('%s/hare/hr2.png' % ICON_DIR),
                   ('%s/hare/hr3.png' % ICON_DIR),
                   ('%s/hare/hr4.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/hare/hl1.png' % ICON_DIR),
                  ('%s/hare/hl2.png' % ICON_DIR),
                  ('%s/hare/hl3.png' % ICON_DIR),
                  ('%s/hare/hl4.png' % ICON_DIR)]
ANIMATION_UP = [('%s/hare/hu1.png' % ICON_DIR),
                ('%s/hare/hu2.png' % ICON_DIR)]
ANIMATION_DOWN = [('%s/hare/hd1.png' % ICON_DIR),
                  ('%s/hare/hd2.png' % ICON_DIR)]
ANIMATION_STAY = [('%s/mario/hu1.png' % ICON_DIR, 0.1)]
'''

class Player(sprite.Sprite):
    def __init__(self, x, y, width=80, height=60, speed=3):
        sprite.Sprite.__init__(self)
        self.speed = speed
        self.vx = 0
        self.vy = 0
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((width, height))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, width, height)  # прямоугольный объект
        '''self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
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
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим'''

    def update(self, left, right, up, down, screen):
        if left:
            self.vx = -self.speed
            '''self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))'''

        if right:
            self.vx = self.speed
            '''self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))'''

        if not (left or right):
            self.vx = 0
            '''self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))'''

        if up:
            self.vy = -self.speed
            '''self.image.fill(Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))'''

        if down:
            self.vy = self.speed
            '''self.image.fill(Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))'''

        if not (up or down):
            self.vy = 0
            '''self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))'''

        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x + self.rect.width >= screen.get_width():
            self.rect.x = screen.get_width() - self.rect.width

        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y + self.rect.height >= screen.get_height():
            self.rect.y = screen.get_height() - self.rect.height

        if self.rect.y <= 0:
            self.rect.y = 0

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
