import pygame
import sys
import random

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.reset()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - self.width),
            -self.height,  # démarre juste au-dessus de l'écran
            self.width,
            self.height
        )
        self.speed = random.randint(3, 7)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

def show_text(surface, text, font, color, pos):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, pos)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodge Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        # Initialisation du joueur et des ennemis
        self.player = Player()
        self.enemies = [Enemy() for _ in range(5)]
        self.score = 0
        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()
            self.player.handle_keys(keys)

            for enemy in self.enemies:
                enemy.update()
                if enemy.rect.colliderect(self.player.rect):
                    self.game_over = True

            self.score += 1

            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            show_text(self.screen, "Score: " + str(self.score), self.font, BLACK, (10, 10))
            pygame.display.flip()
            self.clock.tick(FPS)

        # Écran de fin de partie
        self.show_game_over()

    def show_game_over(self):
        self.screen.fill(BLACK)
        game_over_text = self.font.render("Game Over! Score: " + str(self.score), True, YELLOW)
        self.screen.blit(
            game_over_text,
            (WIDTH // 2 - game_over_text.get_width() // 2,
             HEIGHT // 2 - game_over_text.get_height() // 2)
        )
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

game = Game()
game.run()