import pygame
import os
from config import *
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
        
        # Création des boutons de couleur
        self.color_btns = [
            Button((WIDTH - 50, i * 50, 40, 40), COLORS[i], str(i), self.font)
            for i in range(len(COLORS))
        ]
        
        self.selected_tile = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quitter l'application
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Clic normal (bouton gauche)
                    if event.button == 1:
                        mx, my = event.pos
                        # Si clic dans la grille
                        if my < GRID_HEIGHT * CELL_SIZE:
                            x = mx // CELL_SIZE
                            y = my // CELL_SIZE
                            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                                self.grid.set_tile(x, y, self.selected_tile)
                        # Si clic sur le bouton Enregistrer
                        elif self.save_btn.is_clicked((mx, my)):
                            self.grid.save(SAVE_FILE)
                            print("Niveau enregistré.")
                        # Si clic sur le bouton Charger
                        elif self.load_btn.is_clicked((mx, my)):
                            if os.path.exists(SAVE_FILE):
                                self.grid.load(SAVE_FILE)
                                print("Niveau chargé.")
                        
                        # Vérifier les clics sur les boutons de couleur
                        for index, btn in enumerate(self.color_btns):
                            # Mettre à jour la position Y du bouton avec l'offset
                            btn_rect = btn.rect.copy()
                            if btn_rect.collidepoint(pygame.mouse.get_pos()):
                                self.selected_tile = index
                                print(f"Couleur sélectionnée : {index}")

            # Affichage de l'interface
            self.screen.fill((50, 50, 50))
            self.grid.draw(self.screen)
            self.save_btn.draw(self.screen)
            self.load_btn.draw(self.screen)
            
            # Zone de défilement pour les boutons de couleur
            color_area = pygame.Rect(WIDTH - 60, 0, 60, HEIGHT - 60)
            pygame.draw.rect(self.screen, (40, 40, 40), color_area)
            
            # Afficher les boutons de couleur avec l'offset
            for index, btn in enumerate(self.color_btns):
                btn.draw(self.screen)
            
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    # Lancement de l'éditeur de niveau
    LevelEditor().run()