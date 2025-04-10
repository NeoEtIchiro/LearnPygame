import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
WALL_COLOR   = BLACK
EXIT_COLOR   = (0, 255, 0)
PLAYER_COLOR = (255, 0, 255)

class Level:
    def __init__(self, walls, start, exit_rect):
        self.walls = walls
        self.start = start
        self.exit_rect = exit_rect

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_COLOR, wall)
        pygame.draw.rect(surface, EXIT_COLOR, self.exit_rect)

    def check_collision(self, pos):
        for wall in self.walls:
            if wall.collidepoint(pos):
                return True
        return False

    def reached_exit(self, pos):
        return self.exit_rect.collidepoint(pos)
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Mouse Game - Étape 5")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)  # --- AJOUTÉ : Police pour l'écran de fin

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

    def reset_level(self):
        pygame.mouse.set_pos(self.current_level.start)

    def run(self):
        running = True
        self.reset_level()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            player_pos = pygame.mouse.get_pos()

            if self.current_level.check_collision(player_pos):
                self.reset_level()

            if self.current_level.reached_exit(player_pos):
                self.level_index += 1
                if self.level_index >= len(self.levels):
                    self.show_game_complete()
                    running = False
                    continue
                else:
                    self.current_level = self.levels[self.level_index]
                    self.reset_level()

            self.screen.fill(WHITE)
            self.current_level.draw(self.screen)
            pygame.draw.circle(self.screen, PLAYER_COLOR, player_pos, 5)
            pygame.display.flip()
            self.clock.tick(FPS)

        

    # --- AJOUTÉ À L'ÉTAPE 5 : Méthode d'affichage de l'écran de fin ---
    def show_game_complete(self):
        self.screen.fill(BLACK)
        text = self.font.render("Félicitations, vous avez terminé!", True, PLAYER_COLOR)
        self.screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

game = Game()
game.run()