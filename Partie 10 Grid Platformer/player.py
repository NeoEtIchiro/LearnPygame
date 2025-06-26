import pygame
from consts import GRAVITY, JUMP_STRENGTH, PLAYER_SPEED, PLAYER_MAX_SPEED

class Player:
    def __init__(self, x, y, w, h):
        # Création du rectangle qui représente le joueur (position et taille)
        self.rect = pygame.Rect(x, y, w, h)
        self.vel_y = 0           # Vitesse verticale du joueur (pour la gravité et le saut)
        self.vel_x = 0           # Vitesse horizontale du joueur (pour les déplacements)
        self.on_ground = False   # Indique si le joueur touche une plateforme ou le sol
        self.slowing_speed = 2

    def handle_input(self, keys):
        # Gestion des déplacements horizontaux avec les touches fléchées
        if keys[pygame.K_LEFT]:
            if(self.vel_x > 0):
                self.vel_x = 0
            
            self.vel_x -= PLAYER_SPEED  # Déplacement vers la gauche
        elif keys[pygame.K_RIGHT]:
            if(self.vel_x < 0):
                self.vel_x = 0
            
            self.vel_x += PLAYER_SPEED  # Déplacement vers la droite
        elif(self.vel_x != 0):
          if(self.vel_x > 0):
            self.vel_x -= self.slowing_speed  # Ralentit le joueur s'il ne bouge pas
            if(self.vel_x < 0):
                self.vel_x = 0
          elif(self.vel_x < 0):
            self.vel_x += self.slowing_speed
            if(self.vel_x > 0):
                self.vel_x = 0
            
        # Limite la vitesse horizontale pour éviter de dépasser une certaine valeur
        if self.vel_x > PLAYER_MAX_SPEED:
            self.vel_x = PLAYER_MAX_SPEED
        elif self.vel_x < -PLAYER_MAX_SPEED:
            self.vel_x = -PLAYER_MAX_SPEED
            
        self.rect.x += int(self.vel_x)  # Applique le déplacement horizontal au rectangle du joueur

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
                
                # Si c'est un bloc rebond, le joueur rebondit automatiquement
                if plat.type == "rebond":
                    self.vel_y = JUMP_STRENGTH * 1.2  # Rebond plus fort que le saut normal
                
                self.slowing_speed = plat.slowing_speed
                
        if(not self.on_ground):
            self.slowing_speed = 0.3

    def update(self, platforms, keys):
        # Met à jour l'état du joueur à chaque frame
        self.handle_input(keys)           # Déplacement gauche/droite
        self.apply_gravity()              # Applique la gravité
        self.check_collision(platforms)   # Vérifie les collisions avec les plateformes

    def draw(self, surface):
        # Dessine le joueur en rouge sur la surface donnée
        pygame.draw.rect(surface, (255, 0, 0), self.rect)