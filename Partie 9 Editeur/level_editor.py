import pygame
import os
from config import WIDTH, HEIGHT, SAVE_FILE, GRID_SIZE, CELL_SIZE
from grid import Grid
from button import Button

class LevelEditor:
    def __init__(self):
        pygame.init()
        # Création de la fenêtre principale
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Éditeur de niveau simple")
        self.font = pygame.font.SysFont(None, 32)
        # Création de la grille
        self.grid = Grid()
        # Création des boutons Enregistrer et Charger
        self.save_btn = Button((10, HEIGHT - 50, 140, 40), (70, 200, 70), "Enregistrer", self.font)
        self.load_btn = Button((WIDTH-130, HEIGHT - 50, 120, 40), (70, 70, 200), "Charger", self.font)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quitter l'application
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    # Si clic dans la grille, on bascule l'état de la case
                    if my < GRID_SIZE * CELL_SIZE:
                        x = mx // CELL_SIZE
                        y = my // CELL_SIZE
                        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                            self.grid.toggle(x, y)
                    # Si clic sur le bouton Enregistrer
                    elif self.save_btn.is_clicked((mx, my)):
                        self.grid.save(SAVE_FILE)
                        print("Niveau enregistré.")
                    # Si clic sur le bouton Charger
                    elif self.load_btn.is_clicked((mx, my)):
                        if os.path.exists(SAVE_FILE):
                            self.grid.load(SAVE_FILE)
                            print("Niveau chargé.")

            # Affichage de l'interface
            self.screen.fill((50, 50, 50))
            self.grid.draw(self.screen)
            self.save_btn.draw(self.screen)
            self.load_btn.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    # Lancement de l'éditeur de niveau
    LevelEditor().run()