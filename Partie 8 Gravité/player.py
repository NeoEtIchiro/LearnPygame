import pygame
from consts import GRAVITY, JUMP_STRENGTH, PLAYER_SPEED

class Player:
    def __init__(self, x, y, w, h):
        # Création du rectangle qui représente le joueur (position et taille)
        self.rect = pygame.Rect(x, y, w, h)
        self.vel_y = 0           # Vitesse verticale du joueur (pour la gravité et le saut)
        self.on_ground = False   # Indique si le joueur touche une plateforme ou le sol

    def handle_input(self, keys):
        # Gestion des déplacements horizontaux avec les touches fléchées
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED  # Déplacement vers la gauche
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED  # Déplacement vers la droite

    def jump(self):
        # Permet au joueur de sauter uniquement s'il est sur le sol
        if self.on_ground:
            self.vel_y = JUMP_STRENGTH  # Applique une vitesse verticale négative (vers le haut)

    def apply_gravity(self):
        # Applique la gravité à la vitesse verticale du joueur
        self.vel_y += GRAVITY
        # Déplace le joueur verticalement selon sa vitesse
        self.rect.y += int(self.vel_y)

    def check_collision(self, platforms):
        # Crée un petit rectangle sous le joueur pour détecter s'il touche une plateforme
        foot_rect = pygame.Rect(self.rect.x, self.rect.bottom, self.rect.width, 5)
        self.on_ground = False  # On suppose d'abord que le joueur n'est pas sur le sol

        # On vérifie si le "pied" du joueur touche une des plateformes
        for plat in platforms:
            # Collision seulement si le joueur tombe (vel_y >= 0)
            if foot_rect.colliderect(plat.rect) and self.vel_y >= 0:
                self.rect.bottom = plat.rect.top  # Place le joueur juste au-dessus de la plateforme
                self.vel_y = 0                   # Annule la vitesse verticale (arrête la chute)
                self.on_ground = True            # Le joueur est maintenant sur le sol

    def update(self, platforms, keys):
        # Met à jour l'état du joueur à chaque frame
        self.handle_input(keys)           # Déplacement gauche/droite
        self.apply_gravity()              # Applique la gravité
        self.check_collision(platforms)   # Vérifie les collisions avec les plateformes

    def draw(self, surface):
        # Dessine le joueur en rouge sur la surface donnée
        pygame.draw.rect(surface, (255, 0, 0), self.rect)