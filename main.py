import pygame
import game_board
import enemy


class Runtime:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_board = game_board.GameBoard()
        self.screen = self.game_board.get_screen
        self.pos = []
        self.enemy_club = enemy.EnemyClub()

    def run(self):
        running = True
        while running:
            # Set the game to 60 FPS
            self.clock.tick(30)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.pos.append(mouse_pos)
                    print(self.pos)

            self.game_board.draw()

            self.enemy_club.draw(self.screen)

            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.run()
