import pygame

class Button:
    """
    Classe représentant un bouton graphique dans Pygame.
    Permet d'afficher un bouton et de détecter les clics dessus.
    """

    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font, bg_color=(100,100,100), text_color=(255,255,255)):
        """
        Initialise le bouton.
        - rect : zone du bouton (position et taille)
        - text : texte affiché sur le bouton
        - font : police utilisée pour le texte
        - bg_color : couleur de fond du bouton (optionnel)
        - text_color : couleur du texte (optionnel)
        """
        self.rect = rect
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        # Prépare le texte à afficher (surface Pygame)
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw(self, surface):
        """
        Dessine le bouton sur la surface donnée (l'écran ou une image).
        """
        pygame.draw.rect(surface, self.bg_color, self.rect)  # Dessine le rectangle du bouton
        txt_rect = self.text_surface.get_rect(center=self.rect.center)  # Centre le texte dans le bouton
        surface.blit(self.text_surface, txt_rect)  # Affiche le texte

    def is_hover(self, pos):
        """
        Vérifie si la position (pos) de la souris est sur le bouton.
        Utile pour détecter les clics.
        """
        return self.rect.collidepoint(pos)
