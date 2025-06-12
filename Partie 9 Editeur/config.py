import os

# Taille de la grille (nombre de cases par côté)
GRID_SIZE = 15

# Taille d'une case en pixels
CELL_SIZE = 40

# Marge entre les cases
MARGIN = 2

# Dimensions de la fenêtre
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE + 60  # espace pour les boutons

# Chemin du fichier de sauvegarde (dans le même dossier que ce script)
SAVE_FILE = os.path.join(os.path.dirname(__file__), "level.json")