import pygame

class Button:
    def __init__(self, rect, color, text, font):
        # Initialise le bouton avec sa position, couleur, texte et police
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.font = font

    def draw(self, screen):
        # Dessine le bouton sur l'écran
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255,255,255))
        screen.blit(text_surf, (self.rect.x+10, self.rect.y+5))

    def is_clicked(self, pos):
        # Retourne True si le bouton a été cliqué (collision avec la souris)
        return self.rect.collidepoint(pos)