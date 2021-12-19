import pygame as pg


class Background(pg.sprite.Sprite):
    """
    класс для удобной работы с фоном и получения его параметров
    """
    def init(self, image_file, location):
        pg.sprite.Sprite.init(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location