import pygame


class Runtime:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            # Set the game to 60 FPS
            self.clock.tick(60)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


if __name__ == '__main__':
    g = Runtime()
    g.run()
