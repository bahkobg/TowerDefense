import pygame
import math

enemy_1 = [pygame.image.load('assets/enemies/1/' + str(x) + '.png') for x in range(1, 11)]
enemy_2 = [pygame.image.load('assets/enemies/2/' + str(x) + '.png') for x in range(1, 11)]
enemy_3 = [pygame.image.load('assets/enemies/3/' + str(x) + '.png') for x in range(1, 11)]
enemy_4 = [pygame.image.load('assets/enemies/4/' + str(x) + '.png') for x in range(1, 11)]
enemy_5 = [pygame.image.load('assets/enemies/5/' + str(x) + '.png') for x in range(1, 11)]


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
        self.health_max = 3
        self.health = self.health_max
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
        self.health -= 1

    @property
    def get_position(self):
        return self.x, self.y

    def _health_bar(self, surface):
        """
        Draws enemy health bar.
        :param surface: Surface obj
        :return: None
        """
        length = 42  # Must divide by health_max
        move_by = (round(length // self.health_max))
        health_bar = move_by * self.health

        if self.flipped:
            pygame.draw.rect(surface, (255, 0, 0), (self.x + 16, self.y, length, 8))
            pygame.draw.rect(surface, (0, 255, 0), (self.x + 16, self.y, health_bar, 8))
        else:
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, length, 8))
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, health_bar, 8))

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
            self.y = 701
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
        self._health_bar(surface)
        self._move()


class Enemy1(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_1
        self.path = [(1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]


class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_2
        self.path = [(1100, 100), (470, 100), (384, 240), (639, 444), (603, 509), (469, 562), (479, 690), (475, 699)]


class Enemy3(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_3
        self.path = [(1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]


class Enemy4(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_4
        self.path = [(1100, 100), (470, 100), (384, 240), (639, 444), (603, 509), (469, 562), (479, 690), (475, 699)]


class Enemy5(Enemy):
    def __init__(self):
        super().__init__()
        self.imgs = enemy_5
        self.path = [(1100, 100), (470, 100), (384, 240), (631, 359), (702, 528), (1194, 541), (1242, 541)]
