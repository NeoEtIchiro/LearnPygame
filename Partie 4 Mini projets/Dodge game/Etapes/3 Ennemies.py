import pygame
import sys
import random

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.speed = 5
        self.rect = pygame.Rect(WIDTH//2 - self.width//2,
                                HEIGHT - self.height - 10,
                                self.width, self.height)

    def handle_keys(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

# Nouvelle classe Enemy ajoutée dans cette étape
class Enemy:
    def __init__(self):
        self.width = 40  # Largeur de l'ennemi
        self.height = 40  # Hauteur de l'ennemi
        self.reset()  # Initialisation de la position et de la vitesse

    def reset(self):
        # Réinitialise la position de l'ennemi au-dessus de l'écran
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - self.width),  # Position horizontale aléatoire
            -self.height,  # Démarre juste au-dessus de l'écran
            self.width,
            self.height
        )
        self.speed = random.randint(3, 10)  # Vitesse aléatoire de l'ennemi

    def update(self):
        # Déplace l'ennemi vers le bas
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:  # Si l'ennemi sort de l'écran
            self.reset()  # Réinitialise sa position

    def draw(self, surface):
        # Dessine l'ennemi sur l'écran
        pygame.draw.rect(surface, RED, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge Game - Étape 3")
        self.clock = pygame.time.Clock()
        self.player = Player()
        # Ajout d'une liste d'ennemis dans cette étape
        self.enemies = [Enemy() for i in range(5)]  # Création de 5 ennemis

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.handle_keys(keys)
            # Mise à jour des ennemis (nouveau dans cette étape)
            for enemy in self.enemies:
                enemy.update()

            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            # Dessin des ennemis (nouveau dans cette étape)
            for enemy in self.enemies:
                enemy.draw(self.screen)
                
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

game = Game()
game.run()