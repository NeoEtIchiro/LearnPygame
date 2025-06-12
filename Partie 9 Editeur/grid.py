import pygame
import json
from config import GRID_SIZE, CELL_SIZE, MARGIN

class Grid:
    def __init__(self):
        # Initialise la grille avec des cases éteintes (0)
        line = [0 for x in range(GRID_SIZE)]
        self.grid = [line.copy() for y in range(GRID_SIZE)]

    def draw(self, screen):
        # Dessine la grille sur l'écran
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-MARGIN, CELL_SIZE-MARGIN)
                color = (30,30,30)
                match self.grid[y][x]:
                    case 0:
                        color = (30, 30, 30)
                    case 1:
                        color = (255, 255, 0)
                    case 2:
                        color = (0, 255, 0)
                    case 3:
                        color = (255, 0, 0)
                
                pygame.draw.rect(screen, color, rect)

    def toggle(self, x, y):
        # Change l'état (allumé/éteint) de la case (x, y)
        self.grid[y][x] = 1 - self.grid[y][x]

    def save(self, path):
        # Sauvegarde la grille dans un fichier JSON, une ligne par ligne
        with open(path, "w") as f:
            f.write("[\n")
            for i, row in enumerate(self.grid):
                line = json.dumps(row)
                if i < len(self.grid) - 1:
                    f.write(f"  {line},\n")
                else:
                    f.write(f"  {line}\n")
            f.write("]\n")

    def load(self, path):
        # Charge la grille depuis un fichier JSON
        with open(path, "r") as f:
            data = json.load(f)
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    self.grid[y][x] = data[y][x]