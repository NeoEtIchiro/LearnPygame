import pygame
import sys

# region Configuration

WIDTH, HEIGHT = 800, 600  # Dimensions de la fenêtre
FPS = 60  # Images par seconde
WHITE = (255, 255, 255)  # Couleur blanche en RGB

# endregion

class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()
        # Création de la fenêtre
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Définition du titre de la fenêtre
        pygame.display.set_caption("Dodge Game - Étape 1")
        # Création de l'horloge pour gérer le FPS
        self.clock = pygame.time.Clock()

    def run(self):
        # Boucle principale du jeu
        running = True
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                    running = False
            # Remplissage de l'écran avec une couleur blanche
            self.screen.fill(WHITE)
            # Mise à jour de l'affichage
            pygame.display.flip()
            # Limitation du FPS
            self.clock.tick(FPS)
            
        # Quitter Pygame et le programme
        pygame.quit()
        sys.exit()


# region Lancement

game = Game()
game.run()

# endregion