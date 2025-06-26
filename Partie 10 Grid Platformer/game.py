import pygame
import sys
import json
from consts import *
from platform import Platform
from player import Player

class Game:
    def __init__(self):
        # Initialise Pygame et crée la fenêtre du jeu
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Fenêtre principale
        pygame.display.set_caption("Grid Platformer")
        self.clock = pygame.time.Clock()                        # Pour gérer le temps et le FPS

        # Attributs de la caméra
        self.camera_offset = [0, 0]
        self.camera_smooth = 1  # Facteur de lissage (0-1), plus bas = plus lent

        # Chargement du niveau depuis le fichier JSON
        self.load_level("C:\Projets\Tutorat\LearnPygame\Partie 10 Grid Platformer\level.json")
        
        # Création du joueur (objet Player)
        self.player = Player(100, 100, 30, 50)
        self.running = True  # Contrôle la boucle principale du jeu

    def load_level(self, filename):
        # Charge le niveau depuis un fichier JSON
        try:
            print(f"Chargement du niveau depuis {filename}...")
            with open(filename, 'r') as file:
                self.grid = json.load(file)
            print("Niveau chargé avec succès.")
            # Création des plateformes à partir de la grille
            self.platforms = []
            
            # Parcourt chaque cellule de la grille
            for y, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    print(f"Cellule ({x}, {y}): {cell}")  # Affiche la valeur de la cellule
                    # Si la cellule n'est pas vide (différente de 0)
                    if cell != 0 and cell in BLOCK_MAP and BLOCK_MAP[cell] is not None:
                        # Crée une plateforme de la taille d'une case
                    
                        block_type = BLOCK_MAP[cell]
                        
                        block_object = BLOCK_TYPES.get(block_type)
                        
                        if(block_object is None):
                            print(f"Type de bloc inconnu: {block_type}")
                            continue
                        
                        print(f"Type de bloc: {block_type}, Propriétés: {block_object}")  # Affiche le type de bloc et ses propriétés
                        platform = Platform(
                            x * TILE_SIZE,           # Position X
                            y * TILE_SIZE,           # Position Y
                            TILE_SIZE,               # Largeur
                            TILE_SIZE,               # Hauteur
                            block_object          # Type de bloc
                        )
                        self.platforms.append(platform)
                        
        except FileNotFoundError:
            print(f"Erreur: Le fichier {filename} n'a pas été trouvé.")
            # Niveau par défaut si le fichier n'est pas trouvé
            self.platforms = [
                Platform(0, HEIGHT - 40, WIDTH, 40)  # Sol par défaut
            ]
            
    def update_camera(self):
        # Calcule le centre du joueur
        target_x = self.player.rect.centerx - WIDTH // 2
        target_y = self.player.rect.centery - HEIGHT // 2
        
        # Applique un lissage à la caméra pour des mouvements plus fluides
        self.camera_offset[0] += (target_x - self.camera_offset[0]) * self.camera_smooth
        self.camera_offset[1] += (target_y - self.camera_offset[1]) * self.camera_smooth
        
        # Convertit les offsets en entiers pour éviter des problèmes d'affichage
        self.camera_offset[0] = int(self.camera_offset[0])
        self.camera_offset[1] = int(self.camera_offset[1])

    def apply_camera(self, rect):
        # Retourne un nouveau rectangle avec l'offset de la caméra appliqué
        return pygame.Rect(
            rect.x - self.camera_offset[0],
            rect.y - self.camera_offset[1],
            rect.width,
            rect.height
        )
    
    def run(self):
        # Boucle principale du jeu
        while self.running:
            self.handle_events()  # Gère les entrées clavier et la fermeture de la fenêtre
            keys = pygame.key.get_pressed()  # Récupère l'état de toutes les touches du clavier
            self.player.update(self.platforms, keys)  # Met à jour le joueur
            self.update_camera()  # Met à jour la position de la caméra
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
            # Dessine chaque plateforme avec l'offset de la caméra
            camera_rect = self.apply_camera(plat.rect)
            # Vérifie si la plateforme est visible à l'écran avant de la dessiner
            if (camera_rect.right > 0 and camera_rect.left < WIDTH and 
                camera_rect.bottom > 0 and camera_rect.top < HEIGHT):
                pygame.draw.rect(self.screen, plat.properties.get('color'), camera_rect)
        
        # Dessine le joueur avec l'offset de la caméra
        player_camera_rect = self.apply_camera(self.player.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), player_camera_rect)
        
        pygame.display.flip()  # Met à jour l'affichage à l'écran