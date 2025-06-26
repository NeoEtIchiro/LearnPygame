import pygame

class Platform:
    def __init__(self, x, y, w, h, properties):
        # On crée un rectangle Pygame pour représenter la plateforme
        self.rect = pygame.Rect(x, y, w, h)
        self.type = type
        
        # Différentes propriétés selon le type
        self.properties = properties
        print(self.properties)
