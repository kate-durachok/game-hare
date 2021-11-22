from pygame import *
import pyganim
import os

MOVE_SPEED = 4
WIDTH = 80
HEIGHT = 60
COLOR = "#696969"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.vx = 0
        self.vy = 0
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, down):
        if left:
            self.vx = -MOVE_SPEED

        if right:
            self.vx = MOVE_SPEED

        if not (left or right):
            self.vx = 0

        if up:
            self.vy = -MOVE_SPEED

        if down:
            self.vy = MOVE_SPEED

        if not (up or down):
            self.vy = 0

        self.rect.x += self.vx
        self.rect.y += self.vy

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))