# Ce fichier est un cours de base pour apprendre Python.
# Chaque section présente un concept fondamental accompagné d'exemples pratiques.

# ------------------------------------------------------------
print(" 1. Variables et types de données")
# ------------------------------------------------------------

# Les nombres entiers (int) erty
x = 10

# Les nombres à virgule (float)
y = 3.14

# Les chaînes de caractères (str)
nom = "Alice"

# Les booléens (bool)
est_vrai = True

print("Exemples de variables:")
print("x =", x)
print("y =", y)
print("nom =", nom)
print("est_vrai =", est_vrai)
print()  # Ligne vide pour la lisibilité

# ------------------------------------------------------------
print(" 2. Structures de données : Listes, Tuples et Dictionnaires")
# ------------------------------------------------------------

# Liste : collection ordonnée modifiable
liste_exemple = [1, 2, 3, 4, 5.0]

# Tuple : collection ordonnée non modifiable
tuple_exemple = (1, 2, 3)

# Dictionnaire : collection de paires clé/valeur
dictionnaire_exemple = {"nom": "Alice", "âge": 30}

print("Exemples de structures de données:")
print("Liste :", liste_exemple)
print("Tuple :", tuple_exemple)
print("Dictionnaire :", dictionnaire_exemple)
print()

# Accès aux données des structures :

# Pour une liste, utilisez un index (par exemple, accéder au premier élément)
print("Accès à la liste: le premier élément est", liste_exemple[0])

# Pour un tuple, utilisez également un index (par exemple, accéder au deuxième élément)
print("Accès au tuple: le deuxième élément est", tuple_exemple[1])
print("Remarque: Les tuples sont immuables, vous ne pouvez pas modifier leurs éléments.")

# Pour un dictionnaire, utilisez la clé correspondante pour accéder à la valeur
print("Accès au dictionnaire: la valeur associée à la clé 'nom' est", dictionnaire_exemple["nom"])
print()

# ------------------------------------------------------------
print(" 3. Conditions : if, elif, else")
# ------------------------------------------------------------

# Exemple d'utilisation des conditions
nombre = 7

print("Exemple de conditions:")
if nombre > 10:
    print(nombre, "est supérieur à 10")
elif nombre == 10:
    print(nombre, "est égal à 10")
else:
    print(nombre, "est inférieur à 10")
print()

# Exemple avec input de l'utilisateur :
# On demande à l'utilisateur d'entrer un nombre, puis on affiche s'il est positif, négatif ou zéro.
user_input = input("Entrez un nombre: ")  # L'utilisateur saisit un nombre
nombre_utilisateur = int(user_input)       # Conversion de l'entrée en entier

if nombre_utilisateur > 0:
    print("Le nombre est positif.")
elif nombre_utilisateur < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est zéro.")
print()

# ------------------------------------------------------------
print(" 4. Boucles : for et while")
# ------------------------------------------------------------

# Boucle for pour itérer sur une liste
print("Boucle for:")
for element in liste_exemple:
    print("Élément :", element)

# Boucle while pour répéter une opération jusqu'à ce qu'une condition soit fausse
print("\nBoucle while:")
compteur = 0
while compteur < 5:
    print("Compteur =", compteur)
    compteur += 1
print()

# Boucle for pour itérer sur une liste
print("Boucle for (accès aux éléments et modification à l'aide de leur index):")
# Utilisation de enumerate pour accéder à l'indice et à l'élément
for index in range(len(liste_exemple)):
    # Accès à l'élément
    element = liste_exemple[index]

    print("Index:", index, "Valeur originale:", element)

    # Modification de l'élément en multipliant par 2
    element = element * 2

print("Liste après modification:", liste_exemple)
print()

# Boucle while pour parcourir la liste avec accès par index
print("Boucle while (accès aux éléments avec leur index):")
index = 0
while index < len(liste_exemple):
    print("Index:", index, "Valeur:", liste_exemple[index])
    index += 1
print()

# ------------------------------------------------------------
print(" 5. Fonctions")
# ------------------------------------------------------------

# Définition d'une fonction qui calcule le carré d'un nombre.
def carre(nombre):
    """
    Retourne le carré du nombre fourni.
    """
    return nombre * nombre

print("Exemple de fonction:")
resultat = carre(5)
print("Le carré de 5 est", resultat)
print()

# ------------------------------------------------------------
print(" 6. Importation de modules")
# ------------------------------------------------------------

# Exemple utilisant le module random pour générer un nombre aléatoire
import random

nombre_aleatoire = random.randint(1, 100)
print("Nombre aléatoire entre 1 et 100 :", nombre_aleatoire)
print()

# Fin du cours de base en Python.
print("Fin du cours sur les bases de Python.")