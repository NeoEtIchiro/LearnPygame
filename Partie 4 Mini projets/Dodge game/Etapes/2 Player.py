import pygame
import sys

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
PLAYER_COLOR = (255, 0, 255)  # Nouvelle couleur pour le joueur

class Player:
    def __init__(self):
        # Ajout d'une classe Player pour gérer le joueur
        self.width = 50  # Largeur du joueur
        self.height = 50  # Hauteur du joueur
        self.speed = 5  # Vitesse de déplacement du joueur
        # Création d'un rectangle représentant le joueur
        self.rect = pygame.Rect(WIDTH//2 - self.width//2,
                                HEIGHT - self.height - 10,
                                self.width, self.height)

    def handle_keys(self, keys):
        # Gestion des touches pour déplacer le joueur
        if keys[pygame.K_LEFT] and self.rect.left > 0:  # Déplacement à gauche
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:  # Déplacement à droite
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:  # Déplacement vers le haut
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:  # Déplacement vers le bas
            self.rect.y += self.speed

    def draw(self, surface):
        # Dessin du joueur sur l'écran
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge Game - Étape 2")
        self.clock = pygame.time.Clock()
        
        self.player = Player()  # Ajout d'une instance de Player dans le jeu

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()  # Récupération des touches pressées
            self.player.handle_keys(keys)  # Gestion des déplacements du joueur

            self.screen.fill(WHITE)
            self.player.draw(self.screen)  # Dessin du joueur sur l'écran
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

game = Game()
game.run()