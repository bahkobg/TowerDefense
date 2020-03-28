import pygame
import math
import time

enemy_club_imgs = [pygame.image.load('assets/enemies/1/' + str(x) + '.png') for x in range(1, 6)]


class Enemy:
    """
    Main class for defining enemies.
    """

    def __init__(self):
        self.width = 64
        self.height = 64
        self.path = [(0, 0)]
        self.path_pos = 0
        self.speed = 3
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
        if slope[0] >= 0:
            self.flipped = False
        else:
            self.flipped = True
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        steps = distance // self.speed
        if steps != 0:
            self.change = (slope[0] // steps, slope[1] // steps)
        else:
            self.path_pos += 1

        if self.path_pos + 1 >= len(self.path):
            self.x = 1245
        else:
            self.x += self.change[0]
            self.y += self.change[1]

        print("X:{}, y:{}, CHANGE;{}".format(self.x, self.y, self.change))

        # print('SLOPE: {}, DISTANCE: {}, CHANGE_X:{}, CHANGE_Y: {}'.format(slope, distance, change_x, change_y))

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


class EnemyClub(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_club_imgs
        self.path = [(1100, 110), (529, 110), (384, 240), (546, 372), (702, 528), (1194, 541), (1240, 541)]
