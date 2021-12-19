import pygame as pg


BUTTON_COLOR = "blue"
BUTTON_PRESSED_COLOR = "red"

class Button(pg.sprite.Sprite):
    """
    класс кнопок, используется как в меню так и в самой игре
    """
    def __init__(self, image_files, x, y, bType):
        """
        Конструктор класса Button
        :param image_files: картинки кнопок в разных состояниях
        :param x: координата x верхнего левого угла кнопки
        :param y: координата y верхнего левого угла кнопки
        :param bType: вид кнопки  (0 - создает новое поле, 1 - кнопка передвижения)
        """
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.state = 0
        self.image_files = image_files
        self.image = pg.image.load(image_files[0])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.type = bType

    def checkMePressed(self, hero):
        """
        Провряет нажата ли кнопка
        :param hero: герой, которого проверяют на нажатие кнопки
        :return: 1 - нажата, 0 - ненажата
        """
        hit_box_x = hero.rect.x + hero.rect.width / 6
        hit_box_y = hero.rect.y + hero.rect.height / 2

        if ((-hero.rect.height / 3 <= hit_box_y - self.y <= self.rect.height) and
            (-3 * hero.rect.width / 6 <= hit_box_x - self.x <= self.rect.width)):
            self.state = 1
            self.image = pg.image.load(self.image_files[1])
            return 1
        elif self.type != 0:
            self.state = 0
            self.image = pg.image.load(self.image_files[0])

            return 0

    def press(self):
        """
        Проверяет нажата ли кнопка, сделано для кнопок в меню
        """
        x, y = pg.mouse.get_pos()
        if (self.x <= x <= self.x + self.rect.width) and (self.y <= y <= self.y + self.rect.height):
            if pg.mouse.get_pressed(3)[0]:
                self.image = pg.image.load(self.image_files[2])
                self.state = 1
            else:
                self.image = pg.image.load(self.image_files[1])
        else:
            self.state = 0
            self.image = pg.image.load(self.image_files[0])

    def draw(self, screen):
        """
        Выводит кнопку на экран
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))