WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 0.5
PLAYER_MAX_SPEED = 10

TILE_SIZE = 40  # Taille d'une case en pixels

BLOCK_MAP = {
    0: None,             # Vide
    1: "herbe",         # Normal (vert)
    2: "glace",         # Normal (vert)
    3: "lave",          # Glace (bleu clair)
    7: "rebond",          # Rebond (à implémenter)
}

BLOCK_TYPES = {
  'herbe': {
    'slowing_speed': 0.5,
    'color': (0, 255, 0),
    'jump_multiplier': 1,
    'speed_multiplier': 1,
  },
  "rebond":{
    'slowing_speed': 0.5,
    'color': (255, 165, 0),
    'jump_multiplier': 1.5,
    'speed_multiplier': 1,
  },
  "glace":{
    'slowing_speed': 0.2,
    'color': (0, 165, 255),
    'jump_multiplier': 1,
    'speed_multiplier': 2,
  },
  "lave":{
    'slowing_speed': 1,
    'color': (255, 0, 0),
    'jump_multiplier': 0,
    'speed_multiplier': 0.2,
  }
}