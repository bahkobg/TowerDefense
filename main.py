import pygame
import game_board
import enemy
import time
import random
import tower
import archer


class Runtime:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.pos = []
        self.enemies = []
        self.timer = time.time()
        self.tower1 = tower.Tower1()
        self.level = 1
        self.enemies_count = 0
        self.enemies_max = 5 * self.level
        self.archer1 = archer.Archer1()

    def run(self):
        running = True
        while running:
            # Set the game to 60 FPS
            self.clock.tick(30)

            # Spawn enemies based on current game level
            if time.time() - self.timer > 0.8 and self.enemies_count < self.enemies_max:
                self.timer = time.time()
                self.enemies.append(random.choice([enemy.Enemy1(), enemy.Enemy2(), enemy.Enemy3(), enemy.Enemy4(), enemy.Enemy5()]))
                self.enemies_count += 1

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.pos.append(mouse_pos)
                    print(self.pos)

            # Draw the background
            self.game_board.draw()

            # Draw the enemies
            for i in range(len(self.enemies)-1, -1, -1):
                self.enemies[i].draw(self.screen)
                if self.enemies[i].get_position == (1245, 701):
                    self.enemies.remove(self.enemies[i])

            # Draw the towers
            self.tower1.draw(self.screen)

            # Draw the archers
            self.archer1.draw(self.screen)

            # Draw the overlay trees
            self.game_board.draw_trees()

            # Update game display
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.run()
