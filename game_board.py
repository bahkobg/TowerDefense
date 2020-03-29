import pygame


class GameBoard:
    """
    Defines the main screen and background.
    """

    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/bg1.png'), (1244, 700))
        self.tree = pygame.transform.scale(pygame.image.load('assets/backgrounds/1/tree.png'), (67, 105))
        self.screen = pygame.display.set_mode((1244, 700), pygame.SRCALPHA)

    def draw(self):
        """
        Draws the main screen.
        :return: None
        """
        self.screen.blit(self.img, (0, 0))

    @property
    def get_screen(self):
        """
        Returns the main surface object.
        :return:Surface obj
        """
        return self.screen

    def draw_trees(self):
        """
        Draws some trees separately, so they can appear on top of other images.
        :return: None
        """
        self.screen.blit(self.tree, (716, 576))
        self.screen.blit(self.tree, (1123, 571))
        self.screen.blit(self.tree, (1184, 557))
        self.screen.blit(self.tree, (1155, 601))
        self.screen.blit(self.tree, (1186, 627))
