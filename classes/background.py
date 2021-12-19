import pygame as pg


class Background():
    """
    класс для удобной работы с фоном и получения его параметров
    """
    def __init__(self, image_file, location):
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
