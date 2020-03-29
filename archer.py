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
        self.rect =

    def draw(self, surface):
        if self.animation_index >= 5:
            self.animation_index = 0
        self.img = pygame.transform.scale(self.imgs[self.animation_index], (self.width, self.height))

        if self.flipped:  # if the enemy is moving left
            surface.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))
        else:  # if the enemy is moving right
            surface.blit(self.img, (self.x, self.y))

        if time.time() - self.timer > 0.15:
            self.animation_index += 1
            self.timer = time.time()

    def attack(self):
        pass


class Archer1(Archer):
    def __init__(self):
        super().__init__()
        self.imgs = archer_1
