import pygame
import sys

# Configuration globale
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
PLAYER_COLOR = (255, 0, 255)  # Couleur du joueur
WALL_COLOR   = BLACK          # Couleur des murs
EXIT_COLOR   = (0, 255, 0)      # Couleur de la zone de sortie

class Level:
    def __init__(self, walls, start, exit_rect):
        # walls : liste de pygame.Rect représentant les murs du labyrinthe
        # start : position initiale du joueur (tuple x, y)
        # exit_rect : pygame.Rect représentant la zone de sortie du niveau
        self.walls = walls
        self.start = start
        self.exit_rect = exit_rect

    def draw(self, surface):
        # Dessine les murs
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_COLOR, wall)
        # Dessine la zone de sortie
        pygame.draw.rect(surface, EXIT_COLOR, self.exit_rect)

    def check_collision(self, pos):
        # Vérifie si le point pos (tuple x, y) touche l'un des murs
        for wall in self.walls:
            if wall.collidepoint(pos):
                return True
        return False

    def reached_exit(self, pos):
        # Vérifie si le joueur a atteint la sortie
        return self.exit_rect.collidepoint(pos)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Mouse Game")
        self.clock = pygame.time.Clock()

        # Définition de quelques niveaux
        self.levels = self.create_levels()
        self.level_index = 0
        self.current_level = self.levels[self.level_index]

    def create_levels(self):
        levels = []

        # Niveau 1
        walls1 = [
            pygame.Rect(100, 100, 600, 20),
            pygame.Rect(100, 100, 20, 400),
            pygame.Rect(100, 480, 600, 20),
            pygame.Rect(680, 100, 20, 400),
            pygame.Rect(200, 200, 400, 20),
            pygame.Rect(200, 200, 20, 200),
        ]
        start1 = (150, 150)
        exit_rect1 = pygame.Rect(600, 420, 50, 50)
        level1 = Level(walls1, start1, exit_rect1)
        levels.append(level1)

        # Niveau 2
        walls2 = [
            pygame.Rect(50, 50, 700, 20),
            pygame.Rect(50, 50, 20, 500),
            pygame.Rect(50, 530, 700, 20),
            pygame.Rect(730, 50, 20, 500),
            pygame.Rect(150, 150, 500, 20),
            pygame.Rect(150, 150, 20, 300),
            pygame.Rect(150, 430, 500, 20),
            pygame.Rect(630, 150, 20, 300),
            pygame.Rect(300, 250, 200, 20),
            pygame.Rect(300, 250, 20, 150),
        ]
        start2 = (100, 100)
        exit_rect2 = pygame.Rect(670, 480, 40, 40)
        level2 = Level(walls2, start2, exit_rect2)
        levels.append(level2)

        return levels

    def reset_level(self):
        # Replace le curseur à la position de départ du niveau courant
        pygame.mouse.set_pos(self.current_level.start)

    def run(self):
        running = True
        self.reset_level()  # Place le curseur au début du niveau
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Récupère la position actuelle de la souris (le joueur)
            player_pos = pygame.mouse.get_pos()

            # Si le joueur touche un mur, on réinitialise le niveau
            if self.current_level.check_collision(player_pos):
                self.reset_level()

            # Si le joueur atteint la zone de sortie, on passe au niveau suivant
            if self.current_level.reached_exit(player_pos):
                self.level_index += 1
                if self.level_index >= len(self.levels):
                    # Tous les niveaux ont été complétés
                    running = False
                    continue
                else:
                    self.current_level = self.levels[self.level_index]
                    self.reset_level()

            # Rendu
            self.screen.fill(WHITE)
            self.current_level.draw(self.screen)
            # Dessine le joueur comme un petit cercle
            pygame.draw.circle(self.screen, PLAYER_COLOR, player_pos, 5)
            pygame.display.flip()
            self.clock.tick(FPS)

        self.show_game_complete()

    def show_game_complete(self):
        # Affichage d'un écran de fin indiquant la réussite du jeu
        self.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 48)
        text = font.render("Félicitations, vous avez terminé!", True, PLAYER_COLOR)
        self.screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

game = Game()
game.run()