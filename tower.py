import pygame
import archer


class Tower:
    """
    Defines main tower class
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 85
        self.height = 96
        self.img = None
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = None
        self.range = 120
        self.range_rect = pygame.Rect(self.x - (self.range - self.width // 2), self.y - (self.range - self.height / 2), self.range * 2, self.range * 2)
        self.archer = archer.Archer1(self.get_archer_position[0], self.get_archer_position[1])

    def draw(self, surface):
        """
        Draws the tower on the main surface.
        :param surface: Surface obj
        :return: None
        """
        if self.clicked:
            circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
            surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
        surface.blit(self.img, (self.x, self.y))
        self.archer.draw(surface)

    @property
    def get_rect(self):
        """
        Returns tower rect object
        :return:
        """
        return self.rect

    @property
    def get_x(self):
        """
        Returns tower s position
        :return: int
        """
        return self.x

    @property
    def get_range_rect(self):
        """
        Return the range object of the tower
        :return:Rect() obj
        """
        return self.range_rect

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

    def set_archer_attack(self, x):
        """
        Sets archer to attack
        :param x: bool
        :return: None
        """
        self.archer.set_enemy_in_range(x)

    def set_archer_flipped(self, x):
        """
        Sets archer to flip
        :param x: bool
        :return: None
        """
        self.archer.set_flipped(x)


class Tower1(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = pygame.transform.scale(pygame.image.load('assets/towers/1/1.png'), (self.width, self.height))
