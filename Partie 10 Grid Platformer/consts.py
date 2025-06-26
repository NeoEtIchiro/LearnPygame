WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 0.5
PLAYER_MAX_SPEED = 10


TILE_SIZE = 40  # Taille d'une case en pixels

BLOCK_TYPES = {
    0: None,             # Vide
    1: "normal",         # Normal (vert)
    2: "glace",         # Normal (vert)
    3: "lave",          # Glace (bleu clair)
    7: "rebond"          # Rebond (à implémenter)
}