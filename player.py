from pygame import *
import pyganim
import os

COLOR = "#696969"


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

    def update(self, left, right, up, down, screen):
        if left:
            self.vx = -self.speed

        if right:
            self.vx = self.speed

        if not (left or right):
            self.vx = 0

        if up:
            self.vy = -self.speed

        if down:
            self.vy = self.speed

        if not (up or down):
            self.vy = 0

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
