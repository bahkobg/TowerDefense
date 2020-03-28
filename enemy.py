import pygame
import math
import time

enemy_1 = [pygame.image.load('assets/enemies/1/' + str(x) + '.png') for x in range(1, 11)]
enemy_2 = [pygame.image.load('assets/enemies/2/' + str(x) + '.png') for x in range(1, 11)]


class Enemy:
    """
    Main class for defining enemies.
    """

    def __init__(self):
        self.width = 64
        self.height = 64
        self.path = [(0, 0)]
        self.path_pos = 0
        self.speed = 2
        self.x = 1244
        self.y = 110
        self.path = []
        self.health = 1
        self.animation_index = 0
        self.imgs = []
        self.img = None
        self.change = ()
        self.flipped = None

    def _hit(self):
        """
        Define actions when the enemy is hit.
        :return: None
        """
        pass

    def _move(self):
        """
        Moves the enemy. Called in enemy draw func.
        :return: None
        """

        # Increase the path position index, if the index is last in the list, move the enemy off the board
        x1, y1 = self.x, self.y
        x2, y2 = self.path[self.path_pos][0], self.path[self.path_pos][1]

        # Calculate the slope
        slope = (x2 - x1, y2 - y1)

        # Depending of the slope, change the image orientation
        if slope[0] > 0:
            self.flipped = False
        elif slope[0] < 0:
            self.flipped = True

        # Calculate the distance between the points
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Calculate the steps required, so it maintain constant speed.
        steps = distance // self.speed
        if steps != 0:
            self.change = (slope[0] / steps, slope[1] / steps)
        else:
            self.path_pos += 1

        if self.path_pos + 1 >= len(self.path):
            self.x = 1245
        else:
            self.x += self.change[0]
            self.y += self.change[1]

    def draw(self, surface):
        """
        Draw the enemy.
        :param surface: Surface obj
        :return: None
        """
        if self.animation_index >= len(self.imgs):
            self.animation_index = 0
        self.img = pygame.transform.scale(self.imgs[self.animation_index], (self.width, self.height))

        if self.flipped:  # if the enemy is moving left
            surface.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))
        else:  # if the enemy is moving right
            surface.blit(self.img, (self.x, self.y))

        self.animation_index += 1
        self._move()


class Enemy1(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_1
        self.path = [(1100, 100), (470, 110), (384, 240), (631, 359), (702, 528), (1194, 541), (1240, 541)]


class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_2
        self.path = [(1100, 100), (470, 110), (384, 240), (631, 359), (702, 528), (1194, 541), (1240, 541)]
