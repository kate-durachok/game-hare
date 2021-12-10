from pygame import *
import os
from random import randint

PLATFORM_WIDTH = 25
PLATFORM_HEIGHT = 25
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами
BLOCKS = [('blocks/block0.png'), ('blocks/block1.png'), ('blocks/block2.png'), ('blocks/block3.png'), ('blocks/block4.png'), ('blocks/block5.png')]
 
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load(BLOCKS[randint(0, 5)])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
