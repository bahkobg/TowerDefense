import pygame


class Tower:
    """
    Defines main tower class
    """

    def __init__(self):
        self.x = 527
        self.y = 180
        self.width = 85
        self.height = 96
        self.img = None

    def draw(self, surface):
        """
        Draws the tower on the main surface.
        :param surface: Surface obj
        :return: None
        """
        surface.blit(self.img, (self.x, self.y))


class Tower1(Tower):
    def __init__(self):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load('assets/towers/1/1.png'), (self.width, self.height))
