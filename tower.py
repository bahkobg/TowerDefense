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
        self.clicked = None
        self.range = 120

    def draw(self, surface):
        """
        Draws the tower on the main surface.
        :param surface: Surface obj
        :return: None
        """
        if self.clicked:
            circle_surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range,self.range), self.range, 0)
            surface.blit(circle_surface, (self.rect.center[0]-self.range, self.rect.center[1]-self.range))
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
        return self.x + 14, self.y - 25

    @property
    def get_clicked(self):
        """
        Check if tower is clicked
        :return:bool
        """
        return self.clicked

    def set_toggle_clicked(self):
        """
        Toggle between clicked and not clicked
        :return: None
        """
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True


class Tower1(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.transform.scale(pygame.image.load('assets/towers/1/1.png'), (self.width, self.height))
