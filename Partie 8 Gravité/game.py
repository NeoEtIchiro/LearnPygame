import pygame
import sys
from consts import WIDTH, HEIGHT, FPS
from platform import Platform
from player import Player

class Game:
    def __init__(self):
        # Initialise Pygame et crée la fenêtre du jeu
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Fenêtre principale
        self.clock = pygame.time.Clock()                        # Pour gérer le temps et le FPS

        # Création des plateformes du niveau (liste d'objets Platform)
        self.platforms = [
            Platform(0, HEIGHT - 40, WIDTH, 40),      # Sol
            Platform(200, 450, 200, 20),              # Plateforme 1
            Platform(500, 350, 200, 20),              # Plateforme 2
            Platform(300, 250, 100, 20)               # Plateforme 3
        ]
        # Création du joueur (objet Player)
        self.player = Player(100, 500, 50, 50)
        self.running = True  # Contrôle la boucle principale du jeu

    def run(self):
        # Boucle principale du jeu
        while self.running:
            self.handle_events()  # Gère les entrées clavier et la fermeture de la fenêtre
            keys = pygame.key.get_pressed()  # Récupère l'état de toutes les touches du clavier
            self.player.update(self.platforms, keys)  # Met à jour le joueur (déplacement, gravité, collisions)
            self.draw()  # Affiche tous les éléments à l'écran
            self.clock.tick(FPS)  # Limite la vitesse du jeu à FPS images/seconde

    def handle_events(self):
        # Gère tous les événements (clavier, souris, fermeture, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Si l'utilisateur ferme la fenêtre, on arrête le jeu proprement
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Si une touche est pressée
                if event.key == pygame.K_SPACE:
                    self.player.jump()  # Le joueur tente de sauter

    def draw(self):
        # Dessine le fond, les plateformes et le joueur
        self.screen.fill((135, 206, 235))  # Remplit l'écran avec une couleur bleu ciel
        for plat in self.platforms:
            plat.draw(self.screen)         # Dessine chaque plateforme
        self.player.draw(self.screen)      # Dessine le joueur
        pygame.display.flip()              # Met à jour l'affichage à l'écran