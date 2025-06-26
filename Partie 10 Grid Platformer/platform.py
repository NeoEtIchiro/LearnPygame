import pygame

class Platform:
    def __init__(self, x, y, w, h, type="normal"):
        # On crée un rectangle Pygame pour représenter la plateforme
        self.rect = pygame.Rect(x, y, w, h)
        self.type = type
        print(f"Création d'une plateforme de type: {type}")
        # Différentes propriétés selon le type
        if type == "glace":
            self.slowing_speed = 0.1
            self.color = (173, 216, 230)
        elif type == "rebond":
            self.slowing_speed = 0.5
            self.color = (255, 165, 0)  
        elif type == "normal":  
            self.slowing_speed = 0.5
            self.color = (0, 255, 0)     
        elif type == "lave":  
            self.slowing_speed = 1
            self.color = (255, 0, 0)    

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)