"""
Cours Pygame : Déplacer un nuage avec les flèches

Ce cours présente :
    - Comment charger et afficher une image (ici, un nuage) sur une fenêtre Pygame.
    - Comment déplacer cette image vers la gauche et la droite en maintenant les touches fléchées.
    
Étapes principales :
    1. Initialiser Pygame et créer une fenêtre.
    2. Charger l'image du nuage et définir une position de départ.
    3. Dans la boucle principale, vérifier l'état des touches avec pygame.key.get_pressed().
    4. Mettre à jour la position de l'image selon la touche pressée (flèche gauche ou droite).
    5. Actualiser l'affichage pour montrer le déplacement continu.
    6. Gérer la fermeture de la fenêtre proprement.
    
Exerice :
    - Faire bouger le nuage de haut en bas (Utilisé K_UP et K_DOWN).
    - Ajouter des limites pour empêcher le nuage de sortir de l'écran (Vérifie dans la boucle que la position du nuage ne dépasse pas la taille de l'écran).
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
pygame.display.set_caption("Déplacement du nuage avec les flèches")

# Vitesse de déplacement (en pixels par frame)
vitesse = 5

# Obtenir le dossier du fichier courant
dossier_courant = os.path.dirname(__file__)

# Construire le chemin absolu vers l'image du nuage
chemin_image = os.path.join(dossier_courant, "..", "data", "images", "clouds", "cloud_1.png")
chemin_image = os.path.abspath(chemin_image)

# Charger l'image du nuage
image_nuage = pygame.image.load(chemin_image)
# Optionnel : Définir une couleur de transparence (par exemple, noir)
image_nuage.set_colorkey((0, 0, 0))

# Position initiale du nuage
position_x = 100
position_y = 100

# Horloge pour contrôler le framerate
clock = pygame.time.Clock()

# Boucle principale
en_cours = True
while en_cours:
    # Remplir la fenêtre avec une couleur de fond (bleu ciel)
    fenetre.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Vérifier l'état des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        position_x -= vitesse
    if touches[pygame.K_RIGHT]:
        position_x += vitesse

    # Afficher le nuage à la position actuelle
    fenetre.blit(image_nuage, (position_x, position_y))

    # Actualiser l'affichage
    pygame.display.update()
    
    # Limiter à 60 images par seconde
    clock.tick(60)

# Quitter Pygame et fermer proprement le programme
pygame.quit()
sys.exit()