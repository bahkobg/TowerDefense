import pygame


class Tower:
    """
    Defines main tower class
    """

    def __init__(self, x, y):
        self.x = x  # 527
        self.y = y  # 180
        self.width = 85
        self.height = 96
        self.img = None
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        """
        Draws the tower on the main surface.
        :param surface: Surface obj
        :return: None
        """
        surface.blit(self.img, (self.x, self.y))

    @property
    def get_rect(self):
        """
        Returns tower rect object
        :return:
        """
        return self.rect

    @property
    def get_archer_position(self):
        return self.x+14, self.y-25


class Tower1(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.transform.scale(pygame.image.load('assets/towers/1/1.png'), (self.width, self.height))
