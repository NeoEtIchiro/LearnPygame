import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
WALL_COLOR   = BLACK
EXIT_COLOR   = (0, 255, 0)

class Level:
    def __init__(self, walls, start, exit_rect):
        self.walls = walls
        self.start = start
        self.exit_rect = exit_rect

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_COLOR, wall)
        pygame.draw.rect(surface, EXIT_COLOR, self.exit_rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Mouse Game - Étape 3")
        self.clock = pygame.time.Clock()
        
        # --- AJOUTÉ À L'ÉTAPE 3 : Création de plusieurs niveaux ---
        self.levels = self.create_levels()
        self.level_index = 0
        self.current_level = self.levels[self.level_index]

    def create_levels(self):
        levels = []
        # Niveau 1
        walls1 = [
            pygame.Rect(100, 100, 600, 20),
            pygame.Rect(100, 100, 20, 400),
            pygame.Rect(100, 480, 600, 20)
        ]
        start1 = (150, 150)
        exit_rect1 = pygame.Rect(600, 420, 50, 50)
        levels.append(Level(walls1, start1, exit_rect1))
        
        # Niveau 2
        walls2 = [
            pygame.Rect(50, 50, 700, 20),
            pygame.Rect(50, 50, 20, 500),
            pygame.Rect(50, 530, 700, 20),
            pygame.Rect(730, 50, 20, 500)
        ]
        start2 = (100, 100)
        exit_rect2 = pygame.Rect(670, 480, 40, 40)
        levels.append(Level(walls2, start2, exit_rect2))
        
        return levels

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            self.current_level.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

game = Game()
game.run()