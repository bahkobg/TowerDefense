import pygame
import game_board
import enemy
import time
import random


class Runtime:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.pos = []
        self.enemies = []
        self.timer = time.time()

    def run(self):
        running = True
        while running:
            # Set the game to 60 FPS
            self.clock.tick(30)

            # Set internal timer
            if time.time() - self.timer > 1:
                self.timer = time.time()
                self.enemies.append(random.choice([enemy.Enemy1(), enemy.Enemy2(), enemy.Enemy3(), enemy.Enemy4(), enemy.Enemy5()]))

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.pos.append(mouse_pos)
                    print(self.pos)

            self.game_board.draw()

            for en in self.enemies:
                en.draw(self.screen)

            self.game_board.draw_trees()
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.run()
