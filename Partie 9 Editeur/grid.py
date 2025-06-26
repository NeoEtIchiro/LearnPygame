import pygame
import json
from config import *

class Grid:
    def __init__(self):
        # Initialise la grille avec des cases éteintes (0)
        line = [0 for x in range(GRID_WIDTH)]
        self.grid = [line.copy() for y in range(GRID_HEIGHT)]

    def draw(self, screen):
        # Dessine la grille sur l'écran
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-MARGIN, CELL_SIZE-MARGIN)
                color = COLORS[self.grid[y][x]]
                pygame.draw.rect(screen, color, rect)

    def set_tile(self, x, y, tile):
        self.grid[y][x] = tile

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
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    self.grid[y][x] = data[y][x]