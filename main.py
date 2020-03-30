import pygame
import game_board
import enemy
import time
import random
import tower
import button


class Runtime:

    def __init__(self, level):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.timer = time.time()
        self.towers = [tower.Tower(527, 180), tower.Tower(792, 180), tower.Tower(1010, 390)]
        self.level = level
        self.enemies_count = 0
        self.enemies_max = 2 * self.level
        self.enemies_died = []
        self.fps = 30
        self.buttons = [button.Sound(100, 610), button.Play(10, 610), button.Quick(190, 610)]
        self.enemies = [random.choice([enemy.Enemy1(), enemy.Enemy2(), enemy.Enemy3(), enemy.Enemy4(), enemy.Enemy5()]) for i in range(self.enemies_max)]
        self.first_enemy = self.enemies[0]
        self.last_enemy = self.enemies[0]
        self.timer2 = time.time()
        self.game_paused = False
        pygame.mixer.music.load('assets/sounds/music1.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)

    def run(self):
        running = True
        while running:
            # Set the game to 30 FPS
            self.clock.tick(self.fps)
            # Spawn enemies based on current game level
            if time.time() - self.timer > 0.76 and self.enemies_count < self.enemies_max and not self.game_paused:
                self.timer = time.time()
                if self.enemies_count < self.enemies_max:
                    self.enemies[self.enemies_count].set_pause(False)
                    self.enemies_count += 1

            # Check when the first enemy is in range of a tower and act upon
            if not self.game_paused:
                for t in self.towers:
                    if t.enemy_in_range(self.enemies):

                        if self.first_enemy.get_rect.centerx > t.get_x:  # Check if the first enemy is right of the tower
                            t.set_archer_flipped(False)
                        else:  # Check if the first enemy is left of the tower
                            t.set_archer_flipped(True)

                        t.set_archer_attack(True)  # Set the archer of the tower to attack
                        if time.time() - self.timer2 > 0.15:
                            seed = random.randint(0, len(self.enemies) - 1)
                            if not self.enemies[seed].get_dead:
                                self.enemies[seed].set_hit(t.get_damage)
                                self.timer2 = time.time()

                    else:
                        t.set_archer_attack(False)  # Set the archer of the tower to stop attack

                # Check if all enemies died and end the turn
                for enmy in self.enemies:
                    if enmy.get_dead:
                        if enmy not in self.enemies_died:
                            self.enemies_died.append(enmy)

                if len(self.enemies_died) == self.enemies_max or len(self.enemies) == 0:
                    self.set_new_wave()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)

                    for i in range(len(self.towers)):
                        if self.towers[i].get_rect.collidepoint(mouse_pos):
                            self.towers[i].click(mouse_pos)
                    # Check if a button is clicked
                    for i in range(len(self.buttons)):
                        if self.buttons[i].get_rect.collidepoint(mouse_pos):
                            if i == 0:
                                self.buttons[i].set_toggle_clicked()
                                if self.buttons[i].get_clicked:
                                    pygame.mixer.music.pause()
                                else:
                                    pygame.mixer.music.unpause()
                            if i == 1:
                                self.buttons[i].set_toggle_clicked()
                                if self.buttons[i].get_clicked:
                                    self.game_paused = True
                                    for en in self.enemies:
                                        en.set_pause(True)
                                    for twr in self.towers:
                                        twr.set_pause(True)
                                else:
                                    self.game_paused = False
                                    for en in self.enemies:
                                        en.set_pause(False)
                                    for twr in self.towers:
                                        twr.set_pause(False)
                            if i == 2:
                                self.buttons[i].set_toggle_clicked()
                                if self.buttons[i].get_clicked:
                                    self.set_fps(60)
                                else:
                                    self.set_fps(30)

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

            # Draw the buttons
            for i in range(len(self.buttons)):
                self.buttons[i].draw(self.screen)

            # Update game display
            pygame.display.update()
        pygame.quit()

    def set_fps(self, x: int) -> None:
        """
        Sets game FPS
        :param x: int
        :return: None
        """
        self.fps = x

    def set_new_wave(self):
        if self.level <= 10:
            self.__init__(self.level + 1)
        else:
            self.game_paused = True


if __name__ == '__main__':
    g = Runtime(1)
    g.run()
