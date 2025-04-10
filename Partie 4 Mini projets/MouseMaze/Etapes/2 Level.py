import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
WALL_COLOR   = BLACK
EXIT_COLOR   = (0, 255, 0)

# --- AJOUTÉ À L'ÉTAPE 2 : Définition de la classe Level avec ses propriétés et méthodes draw ---
class Level:
    def __init__(self, walls, start, exit_rect):
        # walls : liste de pygame.Rect pour représenter les murs du labyrinthe
        # start : position de départ du joueur (tuple)
        # exit_rect : pygame.Rect de la zone de sortie du niveau
        self.walls = walls
        self.start = start
        self.exit_rect = exit_rect

    def draw(self, surface):
        # Dessine tous les murs
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_COLOR, wall)
        # Dessine la zone de sortie
        pygame.draw.rect(surface, EXIT_COLOR, self.exit_rect)

# Même classe Game de l'étape 1 pour tester l'affichage d'un niveau statique
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Mouse Game - Étape 2")
        self.clock = pygame.time.Clock()
        
        # Création d'un niveau de test
        walls = [
            pygame.Rect(100, 100, 600, 20),
            pygame.Rect(100, 100, 20, 400),
            pygame.Rect(100, 480, 600, 20),
        ]
        start = (150, 150)
        exit_rect = pygame.Rect(600, 420, 50, 50)
        self.level = Level(walls, start, exit_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            self.level.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

game = Game()
game.run()