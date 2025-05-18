import pygame
import sys
import json
import os

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYER_DATA_FILE = "player_data.json"

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.speed = 5
        self.colors = [BLUE, RED, YELLOW, BLACK]
        self.color_index = 0
        # Valeurs par défaut
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        # Charger les données si elles existent
        self.load_data()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_keys(self, keys):
        moved = False
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            moved = True
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            moved = True
        if moved:
            self.save_data()

    def next_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.save_data()

    def draw(self, surface):
        pygame.draw.rect(surface, self.colors[self.color_index], self.rect)

    def save_data(self):
        data = {
            "x": self.rect.x,
            "y": self.rect.y,
            "color_index": self.color_index
        }
        with open(PLAYER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(PLAYER_DATA_FILE):
            try:
                with open(PLAYER_DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.x = data.get("x", self.x)
                    self.y = data.get("y", self.y)
                    self.color_index = data.get("color_index", self.color_index)
            except Exception:
                pass  # Ignore les erreurs de chargement

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.player = Player()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.next_color()
            
            keys = pygame.key.get_pressed()
            self.player.handle_keys(keys)

            self.screen.fill(WHITE)
            self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

game = Game()
game.run()