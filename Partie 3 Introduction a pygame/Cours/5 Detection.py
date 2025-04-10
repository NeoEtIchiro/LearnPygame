"""
Cours Pygame : Détection de collision – Changement de couleur d'un rectangle

Ce cours combine la gestion du déplacement d'un nuage et la détection de collision avec un rectangle.
Lorsque le nuage (déplacé à l'aide des flèches) recoupe le rectangle, celui-ci change de couleur.

Étapes principales :
    1. Initialiser Pygame et créer une fenêtre.
    2. Charger l'image du nuage et définir sa position de départ.
    3. Dessiner un rectangle fixe sur la fenêtre.
    4. Détecter la collision entre le nuage et le rectangle en utilisant les Rects de Pygame.
    5. Changer la couleur du rectangle lors de la collision.
    6. Actualiser l'affichage dans une boucle principale et gérer la fermeture de la fenêtre.
"""

import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
taille = (800, 600)
fenetre = pygame.display.set_mode(taille)
pygame.display.set_caption("Collision : Nuage et Rectangle")

# Vitesse de déplacement du nuage (pixels par frame)
vitesse = 5

# Obtenir le dossier du fichier courant
dossier_courant = os.path.dirname(__file__)

# Construire le chemin absolu vers l'image du nuage (remonter d'un répertoire avec "..")
chemin_image = os.path.join(dossier_courant, "..", "data", "images", "clouds", "cloud_1.png")
chemin_image = os.path.abspath(chemin_image)

# Charger l'image du nuage et définir la couleur de transparence (optionnel)
image_nuage = pygame.image.load(chemin_image)
image_nuage.set_colorkey((0, 0, 0))  # Suppression du fond noir si présent

# Position initiale du nuage
position_x = 100
position_y = 100

# Définir le rectangle fixe qui changera de couleur lors de la collision
# Exemple : rectangle positionné à (300, 200) avec une largeur de 150 et une hauteur de 100
rect_target = pygame.Rect(300, 200, 150, 100)
couleur_normal = (255, 0, 0)      # Rouge
couleur_collision = (0, 255, 0)   # Vert

# Horloge pour contrôler le framerate
clock = pygame.time.Clock()

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Vérification des touches pressées pour déplacer le nuage
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        position_x -= vitesse
    if touches[pygame.K_RIGHT]:
        position_x += vitesse
    if touches[pygame.K_UP]:
        position_y -= vitesse
    if touches[pygame.K_DOWN]:
        position_y += vitesse

    # Créer le rectangle du nuage à partir de son image et de sa position actuelle
    rect_nuage = image_nuage.get_rect(topleft=(position_x, position_y))

    # Déterminer la couleur du rectangle selon la collision
    if rect_target.colliderect(rect_nuage):
        couleur_rect = couleur_collision
    else:
        couleur_rect = couleur_normal

    # Remplir la fenêtre avec une couleur de fond (bleu ciel)
    fenetre.fill((135, 206, 235))

    # Dessiner le nuage et le rectangle
    fenetre.blit(image_nuage, (position_x, position_y))
    pygame.draw.rect(fenetre, couleur_rect, rect_target)

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter à 60 images par seconde
    clock.tick(60)

# Quitter Pygame et fermer le programme proprement
pygame.quit()
sys.exit()