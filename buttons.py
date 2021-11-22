from pygame import *


BUTTON_COLOR = "blue"
BUTTON_PRESSED_COLOR = "red"
BUTTON_TYPES = ["UP", "DOWN", "LEFT", "RIGHT", "CARROT"]

class Button(sprite.Sprite):
    def __init__(self, x, y, width=32, height=32, bType=""):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.state = 0
        self.image = Surface((width, height))
        self.image.fill(Color(BUTTON_COLOR))
        self.rect = Rect(x, y, width, height)
        self.type = bType

    def checkMePressed(self, hero):
        hit_box_x = hero.rect.x + hero.rect.width / 8
        hit_box_y = hero.rect.y + 2 * hero.rect.height / 3

        if ((-hero.rect.height / 3 <= hit_box_y - self.y <= self.rect.height) and
            (-3 * hero.rect.width / 4 <= hit_box_x - self.x <= self.rect.width)):
            self.state = 1
            self.image.fill(Color(BUTTON_PRESSED_COLOR))
        else:
            self.state = 0
            self.image.fill(Color(BUTTON_COLOR))

        if self.type == BUTTON_TYPES[0]:
            pass
        elif self.type == BUTTON_TYPES[1]:
            pass

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))