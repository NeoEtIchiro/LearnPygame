import pygame
import sys
import json
from consts import WIDTH, HEIGHT, FPS, TILE_SIZE, BLOCK_TYPES
from platform import Platform
from player import Player

class Game:
    def __init__(self):
        # Initialise Pygame et crée la fenêtre du jeu
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Fenêtre principale
        pygame.display.set_caption("Grid Platformer")
        self.clock = pygame.time.Clock()                        # Pour gérer le temps et le FPS

        # Chargement du niveau depuis le fichier JSON
        self.load_level("C:\Projets\Tutorat\LearnPygame\Partie 10 Grid Platformer\level.json")
        
        # Création du joueur (objet Player)
        self.player = Player(100, 100, 30, 50)
        self.running = True  # Contrôle la boucle principale du jeu

    def load_level(self, filename):
        # Charge le niveau depuis un fichier JSON
        try:
            with open(filename, 'r') as file:
                self.grid = json.load(file)
                
            # Création des plateformes à partir de la grille
            self.platforms = []
            
            # Parcourt chaque cellule de la grille
            for y, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    # Si la cellule n'est pas vide (différente de 0)
                    if cell != 0 and cell in BLOCK_TYPES and BLOCK_TYPES[cell] is not None:
                        # Crée une plateforme de la taille d'une case
                        block_type = BLOCK_TYPES[cell]
                        print(block_type)
                        platform = Platform(
                            x * TILE_SIZE,           # Position X
                            y * TILE_SIZE,           # Position Y
                            TILE_SIZE,               # Largeur
                            TILE_SIZE,               # Hauteur
                            type=block_type          # Type de bloc
                        )
                        self.platforms.append(platform)
                        
        except FileNotFoundError:
            print(f"Erreur: Le fichier {filename} n'a pas été trouvé.")
            # Niveau par défaut si le fichier n'est pas trouvé
            self.platforms = [
                Platform(0, HEIGHT - 40, WIDTH, 40)  # Sol par défaut
            ]
            
    def run(self):
        # Boucle principale du jeu
        while self.running:
            self.handle_events()  # Gère les entrées clavier et la fermeture de la fenêtre
            keys = pygame.key.get_pressed()  # Récupère l'état de toutes les touches du clavier
            self.player.update(self.platforms, keys)  # Met à jour le joueur
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
                if event.key == pygame.K_ESCAPE:
                    # Si la touche Échap est pressée, on quitte le jeu
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.player.jump()  # Le joueur tente de sauter

    def draw(self):
        # Dessine le fond, les plateformes et le joueur
        self.screen.fill((135, 206, 235))  # Remplit l'écran avec une couleur bleu ciel
        for plat in self.platforms:
            plat.draw(self.screen)         # Dessine chaque plateforme
        self.player.draw(self.screen)      # Dessine le joueur
        pygame.display.flip()              # Met à jour l'affichage à l'écran