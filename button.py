import pygame


class Button:
    def __init__(self, x, y):
        self.img = None
        self.width = 80
        self.height = 80
        self.x = x
        self.y = y
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        """
        Draws the button
        :param surface: Surface() obj
        :return: None
        """
        surface.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def set_toggle_clicked(self):
        """
        Toggle between clicked and not clicked
        :return: None
        """
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True

    @property
    def get_clicked(self):
        """
        Check if tower is clicked
        :return:bool
        """
        return self.clicked

    @property
    def get_rect(self):
        """
        Returns tower rect object
        :return:
        """
        return self.rect


class Quick(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = [pygame.image.load('assets/menus/button_quick.png'), pygame.image.load('assets/menus/button_left.png')]

    def draw(self, surface):
        """
        Draws the button
        :param surface: Surface() obj
        :return: None
        """
        if self.clicked:
            surface.blit(pygame.transform.scale(self.imgs[1], (self.width, self.height)), (self.x, self.y))
        else:
            surface.blit(pygame.transform.scale(self.imgs[0], (self.width, self.height)), (self.x, self.y))


class Play(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = [pygame.image.load('assets/menus/button_play.png'), pygame.image.load('assets/menus/button_pause.png')]

    def draw(self, surface):
        """
        Draws the button
        :param surface: Surface() obj
        :return: None
        """
        if self.clicked:
            surface.blit(pygame.transform.scale(self.imgs[0], (self.width, self.height)), (self.x, self.y))
        else:
            surface.blit(pygame.transform.scale(self.imgs[1], (self.width, self.height)), (self.x, self.y))


class Settings(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.image.load('assets/menus/button_settings.png')


class Sound(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = [pygame.image.load('assets/menus/button_sound.png'), pygame.image.load('assets/menus/button_sound_off.png')]

    def draw(self, surface):
        """
        Draws the button
        :param surface: Surface() obj
        :return: None
        """
        if self.clicked:
            surface.blit(pygame.transform.scale(self.imgs[1], (self.width, self.height)), (self.x, self.y))
        else:
            surface.blit(pygame.transform.scale(self.imgs[0], (self.width, self.height)), (self.x, self.y))





class Music(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.image.load('assets/menus/button_music.png')


class MusicOff(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.image.load('assets/menus/music_off.png')
