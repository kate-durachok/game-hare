from pygame import *
from os import path


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
        #self.button_sound = mixer.Sound(path.join('music/button.ogg'))

    def checkMePressed(self, hero):
        hit_box_x = hero.rect.x + hero.rect.width / 6
        hit_box_y = hero.rect.y + 2 * hero.rect.height / 4

        if ((-hero.rect.height / 3 <= hit_box_y - self.y <= self.rect.height) and
            (-3 * hero.rect.width / 6 <= hit_box_x - self.x <= self.rect.width)):
            self.state = 1
            self.image = image.load(self.image_files[1])
            #self.button_sound.play()
            return 1
        elif self.type != 0:
            self.state = 0
            self.image = image.load(self.image_files[0])
            return 0

    def Press(self):
        x, y = mouse.get_pos()
        if (self.x <= x <= self.x + self.rect.width) and (self.y <= y <= self.y + self.rect.height):
            if mouse.get_pressed(3)[0]:
                self.image = image.load(self.image_files[2])
                self.state = 1
            else:
                self.image = image.load(self.image_files[1])
        else:
            self.state = 0
            self.image = image.load(self.image_files[0])

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))