"""
Cours Pygame : Collision Solide – Empêcher le nuage de traverser le rectangle

Ce cours présente comment empêcher l'image du nuage de passer à travers un rectangle.
Au lieu de simplement changer la couleur du rectangle lors d'une collision, nous allons empêcher
la mise à jour de la position du nuage si le mouvement provoque une collision avec le rectangle.

Approche utilisée :
    - Pour chaque axe (horizontal et vertical), on calcule une position candidate.
    - On crée un Rect pour l'image du nuage à cette position candidate.
    - Si ce Rect ne collisionne pas avec le rectangle cible, on met à jour la position sur cet axe.
    - Sinon, on ne met pas à jour la position, empêchant ainsi le nuage de se déplacer dans le rectangle.
    
Étapes principales :
    1. Initialiser Pygame, charger l'image et créer la fenêtre.
    2. Gérer la lecture des touches pour obtenir un mouvement envisagé.
    3. Tester séparément le mouvement horizontal et vertical pour éviter la collision.
    4. Afficher le nuage et le rectangle dans la fenêtre.
    5. Gérer la fermeture de la fenêtre proprement.
"""

# region Importations et initialisation
import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre (largeur, hauteur)
taille = (800, 600)
fenetre = pygame.display.set_mode(taille)
pygame.display.set_caption("Collision Solide – Empêcher le nuage de passer dans le rectangle")

# Obtenir le dossier du fichier courant
dossier_courant = os.path.dirname(__file__)

# Construire le chemin absolu vers l'image du nuage
chemin_image = os.path.join(dossier_courant, "..", "data", "images", "clouds", "cloud_1.png")
chemin_image = os.path.abspath(chemin_image)

# Charger l'image du nuage et définir la couleur de transparence (optionnel)
image_nuage = pygame.image.load(chemin_image)
image_nuage.set_colorkey((0, 0, 0))  # Optionnel : supprime le fond noir

# endregion

# region Variables de position et vitesse

# Position initiale du nuage
position_x = 100
position_y = 100

# Vitesse de déplacement du nuage (pixels par frame)
vitesse = 5

# endregion

# region Définition du rectangle fixe (cible)

# Définir le rectangle fixe (cible) – position et dimensions
rect_target = pygame.Rect(300, 200, 150, 100)

# Couleurs pour affichage (facultatif, ici juste pour dessin)
couleur_rectangle = (255, 0, 0)  # Rouge

# endregion

# Horloge pour contrôler le framerate
clock = pygame.time.Clock()

# Boucle principale
en_cours = True
while en_cours:
    # region Event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # endregion
    
    # Récupérer l'état des touches
    touches = pygame.key.get_pressed()

    # region ----- Traitement du mouvement horizontal -----
    
    # Calculer la position candidate sur l'axe horizontal
    nouvelle_position_x = position_x
    if touches[pygame.K_LEFT]:
        nouvelle_position_x = position_x - vitesse
    if touches[pygame.K_RIGHT]:
        nouvelle_position_x = position_x + vitesse
        
    # Créer un rectangle candidat pour le nuage (mouvement horizontal uniquement)
    rect_candidate = image_nuage.get_rect(topleft=(nouvelle_position_x, position_y))
    
    # Mettre à jour la position horizontale uniquement si le mouvement n'engendre pas de collision
    if not rect_candidate.colliderect(rect_target):
        position_x = nouvelle_position_x

    # endregion

    # region ----- Traitement du mouvement vertical -----
    
    # Calculer la position candidate sur l'axe vertical
    nouvelle_position_y = position_y
    if touches[pygame.K_UP]:
        nouvelle_position_y = position_y - vitesse
    if touches[pygame.K_DOWN]:
        nouvelle_position_y = position_y + vitesse
    # Créer un rectangle candidat pour le nuage (mouvement vertical uniquement)
    rect_candidate = image_nuage.get_rect(topleft=(position_x, nouvelle_position_y))
    # Mettre à jour la position verticale uniquement si le mouvement n'engendre pas de collision
    if not rect_candidate.colliderect(rect_target):
        position_y = nouvelle_position_y

    # endregion

    # region Affichage

    # Remplir la fenêtre avec une couleur de fond (bleu ciel)
    fenetre.fill((135, 206, 235))

    # Dessiner le nuage à la position actuelle
    fenetre.blit(image_nuage, (position_x, position_y))

    # Dessiner le rectangle cible
    pygame.draw.rect(fenetre, couleur_rectangle, rect_target)

    # Actualiser l'affichage
    pygame.display.flip()

    # Limiter à 60 images par seconde
    clock.tick(60)
    
    # endregion

# Quitter Pygame et fermer proprement le programme
pygame.quit()
sys.exit()