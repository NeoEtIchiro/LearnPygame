"""
Cours Pygame : Créer une fenêtre

Ce cours présente les étapes de base pour créer une fenêtre avec Pygame.

Étapes principales :
    1. Initialiser Pygame.
    2. Définir la taille de la fenêtre.
    3. Créer la fenêtre avec pygame.display.set_mode().
    4. Définir un titre pour la fenêtre avec pygame.display.set_caption().
    6. Quitter proprement Pygame.
    
Exercie :
    1. Mettre la largeur et la longueur de la de fenêtre dans des variables.
    2. Changer le nom de la fenetre
    
"""

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre (largeur, hauteur)
taille = (800, 600)
fenetre = pygame.display.set_mode(taille)

# Définition du titre de la fenêtre
pygame.display.set_caption("Ma Première Fenêtre Pygame")

# Quitter Pygame et fermer le programme
pygame.quit()
sys.exit()