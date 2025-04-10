"""
Cours Pygame : Gestion des événements

Ce cours présente les étapes de base pour gérer les événements utilisateur dans Pygame.

Étapes principales :
    1. Initialiser Pygame et créer une fenêtre.
    2. Utiliser une boucle principale pour écouter et gérer les événements.
    3. Traiter certains événements tels que la fermeture de la fenêtre, l'appui sur une touche ou un clic de souris.
    
"""

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre (largeur, hauteur)
taille = (800, 600)
fenetre = pygame.display.set_mode(taille)

# Définition du titre de la fenêtre
pygame.display.set_caption("Gestion des événements - Pygame")

# Boucle principale pour gérer les événements
en_cours = True
while en_cours:
    # Parcourir la liste des événements
    for event in pygame.event.get():
        # Quitter si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            en_cours = False
        
        # Détection de l'appui sur une touche
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                # Quitter si la touche ECHAP est pressée
                en_cours = False
            else:
                # Afficher le nom de la touche pressée
                print("Touche pressée :", pygame.key.name(event.key))

        # Détection du relâchement d'une touche
        elif event.type == pygame.KEYUP:
            # Afficher le nom de la touche relâchée
            print("Touche relâchée :", pygame.key.name(event.key))

        # Détection d'un clic de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Clic de souris détecté en position :", event.pos)

# Quitter Pygame et fermer proprement le programme
pygame.quit()
sys.exit()