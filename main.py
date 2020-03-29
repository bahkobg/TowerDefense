import pygame
import game_board
import enemy
import time
import random
import tower


class Runtime:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.enemies = []
        self.timer = time.time()
        self.towers = [tower.Tower1(527, 180), tower.Tower1(792, 180), tower.Tower1(1050, 180)]
        self.level = 1
        self.enemies_count = 0
        self.enemies_max = 5 * self.level
        self.first_enemy = None

    def run(self):
        running = True
        while running:
            # Set the game to 30 FPS
            self.clock.tick(30)

            # Spawn enemies based on current game level
            if time.time() - self.timer > 0.8 and self.enemies_count < self.enemies_max:
                self.timer = time.time()
                self.enemies.append(random.choice([enemy.Enemy1(), enemy.Enemy2(), enemy.Enemy3(), enemy.Enemy4(), enemy.Enemy5()]))
                self.first_enemy = self.enemies[0]
                self.enemies_count += 1

            # Check when enemies are in range of a tower act upon
            for t in self.towers:
                if self.first_enemy:
                    if t.get_range_rect.colliderect(self.first_enemy.get_rect):
                        if self.first_enemy.get_rect.centerx > t.get_x:
                            t.set_archer_flipped(False)
                        else:
                            t.set_archer_flipped(True)
                        t.set_archer_attack(True)
                    else:
                        t.set_archer_attack(False)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    for i in range(len(self.towers)):
                        if self.towers[i].get_rect.collidepoint(mouse_pos):
                            self.towers[i].set_toggle_clicked()

            # Draw the background
            self.game_board.draw()

            # Draw the enemies
            for i in range(len(self.enemies) - 1, -1, -1):
                self.enemies[i].draw(self.screen)
                if self.enemies[i].get_position == (1245, 701):
                    self.enemies.remove(self.enemies[i])

            # Draw the towers
            for i in range(len(self.towers)):
                self.towers[i].draw(self.screen)

            # Draw the overlay trees
            self.game_board.draw_trees()


            # Update game display
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.run()
