import os

# Taille de la grille (nombre de cases par côté)
GRID_WIDTH = 20
GRID_HEIGHT = 15

# Taille d'une case en pixels
CELL_SIZE = 40

# Marge entre les cases
MARGIN = 2

# Dimensions de la fenêtre
WIDTH = GRID_WIDTH * CELL_SIZE + 60
HEIGHT = GRID_HEIGHT * CELL_SIZE + 60  # espace pour les boutons

# Chemin du fichier de sauvegarde (dans le même dossier que ce script)
dossier_courant = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(dossier_courant, "level.json")

COLORS = {
  0: (30, 30, 30),  # Couleur par défaut (case éteinte)
  1: (255, 255, 0),  # Couleur jaune
  2: (0, 255, 0),    # Couleur verte
  3: (255, 0, 0),    # Couleur rouge
  4: (0, 0, 255),    # Couleur bleue
  5: (255, 165, 0),  # Couleur orange
  6: (128, 0, 128),  # Couleur violette
  7: (0, 255, 255),  # Couleur cyan
  8: (192, 192, 192)   # Couleur grise
}