import pygame

class Platform:
    def __init__(self, x, y, w, h, type="normal"):
        # On crée un rectangle Pygame pour représenter la plateforme
        self.rect = pygame.Rect(x, y, w, h)
        self.type = type
        
        self.slowing_speed = 0.1 if type=="glace" else 0.5

    def draw(self, surface):
        if(self.type == "normal"):
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
        elif(self.type == "glace"):
            pygame.draw.rect(surface, (173, 216, 230), self.rect)