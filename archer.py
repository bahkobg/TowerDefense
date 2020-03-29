import pygame
import time

archer_1 = [pygame.image.load('assets/archers/1/' + str(x) + '.png') for x in range(1, 13)]


class Archer:
    """
    Define main archer properties
    """

    def __init__(self, x, y):
        self.img = None
        self.x = x
        self.y = y
        self.width = 45
        self.height = 45
        self.animation_index = 0
        self.flipped = True
        self.imgs = []
        self.timer = time.time()
        self.enemy_in_range = False

    def draw(self, surface):
        if self.animation_index >= 5:
            self.animation_index = 0
        if self.enemy_in_range:
            self.img = pygame.transform.scale(self.imgs[self.animation_index], (self.width, self.height))
        else:
            self.img = pygame.transform.scale(self.imgs[0], (self.width, self.height))

        if self.flipped:  # if the enemy is left
            surface.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))
        else:  # if the enemy is right
            surface.blit(self.img, (self.x, self.y))

        if time.time() - self.timer > 0.15:
            self.animation_index += 1
            self.timer = time.time()

    def attack(self):
        pass

    def set_enemy_in_range(self, x):
        """
        Sets self.enemy_in_rang
        :param x: bool
        :return: None
        """
        if self.enemy_in_range != x:
            self.enemy_in_range = x

    def set_flipped(self, x):
        """
        Sets archer to flip
        :param x: bool
        :return: None
        """
        if self.flipped != x:
            self.flipped = x

class Archer1(Archer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.imgs = archer_1
