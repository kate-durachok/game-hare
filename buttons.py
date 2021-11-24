from pygame import *


BUTTON_COLOR = "blue"
BUTTON_PRESSED_COLOR = "red"
BUTTON_TYPES = ["UP", "DOWN", "LEFT", "RIGHT", "CARROT"]

class Button(sprite.Sprite):
    def __init__(self, image_files, x, y, bType):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.state = 0
        self.image_files = image_files
        self.image = image.load(image_files[0])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.type = bType

    def checkMePressed(self, hero):
        hit_box_x = hero.rect.x + hero.rect.width / 8
        hit_box_y = hero.rect.y + 2 * hero.rect.height / 4

        if self.type == BUTTON_TYPES[0]:
            pass
        elif self.type == BUTTON_TYPES[1]:
            pass

        if ((-hero.rect.height / 3 <= hit_box_y - self.y <= self.rect.height) and
            (-3 * hero.rect.width / 4 <= hit_box_x - self.x <= self.rect.width)):
            self.state = 1
            self.image = image.load(self.image_files[1])
            return 1
        elif self.type != 0:
            self.state = 0
            self.image = image.load(self.image_files[0])
            return 0


    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))