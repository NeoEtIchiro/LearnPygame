"""
Cours Pygame : Utilisation de blit

Ce cours présente :
    - Comment charger une image avec pygame.image.load().
    - Comment utiliser la méthode blit pour dessiner l'image sur la fenêtre.
    - Comment positionner l'image sur l'écran.

Image utilisée :
    ../data/images/clouds/cloud_1.png

    .. permet de remonter d'un répertoire par rapport à l'emplacement du script.

Étapes principales :
    1. Initialiser Pygame et créer une fenêtre.
    2. Charger l'image avec pygame.image.load().
    3. Utiliser la méthode blit pour dessiner l'image à une position précise.
    4. Actualiser l'écran pour afficher l'image.
    5. Gérer la boucle d'événements pour fermer la fenêtre proprement.
    
Exercice :
    - Modifier la position de l'image pour la centrer sur l'écran.
    - Charger une autre image et l'afficher à une position différente.
"""

import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre (largeur, hauteur)
taille = (800, 600)
fenetre = pygame.display.set_mode(taille)

# Définition du titre de la fenêtre
pygame.display.set_caption("Utilisation de blit - Affichage d'une image")

# Obtenir le dossier du fichier courant
dossier_courant = os.path.dirname(__file__)

# Construire le chemin absolu vers l'image à partir du fichier courant
chemin_image = os.path.join(dossier_courant, "../data/images/clouds/cloud_1.png")
chemin_image = os.path.abspath(chemin_image)

# Charger l'image avec pygame.image.load()
image_cloud = pygame.image.load(chemin_image)
# Définir la couleur de transparence (noir) pour l'image
image_cloud.set_colorkey((0, 0, 0)) 

# Position où l'image sera affichée (par exemple, en haut à gauche)
position = (100, 100)

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir la fenêtre avec une couleur de fond (bleu ciel)
    fenetre.fill((135, 206, 235))

    # Utilisation de blit pour dessiner l'image sur la fenêtre à la position spécifiée
    fenetre.blit(image_cloud, position)

    # Actualisation de l'affichage
    pygame.display.flip()

# Quitter Pygame et fermer proprement le programme
pygame.quit()
sys.exit()