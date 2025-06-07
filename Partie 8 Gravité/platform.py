import pygame

class Platform:
    def __init__(self, x, y, w, h):
        # On crée un rectangle Pygame pour représenter la plateforme
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surface):
        # Dessine la plateforme en vert sur la surface donnée
        pygame.draw.rect(surface, (0, 255, 0), self.rect)