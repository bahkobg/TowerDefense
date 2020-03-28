import pygame


class GameBoard:
    """
    Defines the main screen and background.
    """
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load('assets/backgrounds/bg1.png'), (1244, 700))
        self.screen = pygame.display.set_mode((1244, 700))

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
