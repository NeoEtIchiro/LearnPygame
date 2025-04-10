import pygame
import sys

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE  = (255, 255, 255)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Mouse Game - Étape 1")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

game = Game()
game.run()