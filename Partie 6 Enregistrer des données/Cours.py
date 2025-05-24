"""
Cours : Enregistrer et lire des données en JSON avec Python

Objectifs :
- Comprendre le format JSON
- Savoir sauvegarder des données en JSON
- Savoir lire des données depuis un fichier JSON
- Manipuler différents types de données (dictionnaires, listes)
- Gérer les erreurs courantes

Étape 1 : Introduction au format JSON
-------------------------------------
JSON (JavaScript Object Notation) est un format léger d'échange de données.
Il est lisible par l'homme et facile à manipuler en Python grâce au module `json`.

Étape 2 : Sauvegarder un dictionnaire en JSON
---------------------------------------------
"""

import json

# # Exemple de données à sauvegarder
# utilisateur = {
#     "nom": "Alice",
#     "age": 25,
#     "langages": [{"langage": "Python", "niveau": "intermédiaire"},
#                  {"langage": "JavaScript", "niveau": "débutant"}],
# }

# # Sauvegarde dans un fichier
# with open("utilisateur.json", "w", encoding="utf-8") as json_file: # w pour write
#   json.dump(utilisateur, json_file, indent=4)
    
    
# print("Données sauvegardées dans utilisateur.json")


# """
# Étape 3 : Lire des données depuis un fichier JSON
# -------------------------------------------------
# """

# with open("utilisateur.json", "r", encoding="utf-8") as json_file: # r pour read
#     donnees = json.load(json_file)
    
# print("Données lues :", donnees)

# """
# Étape 4 : Sauvegarder une liste de dictionnaires
# ------------------------------------------------
# """

# utilisateurs = [
#     {"nom": "Alice", "age": 25},
#     {"nom": "Bob", "age": 30},
#     {"nom": "Charlie", "age": 22}
# ]

# with open("utilisateurs.json", "w", encoding="utf-8") as f:
#     json.dump(utilisateurs, f, indent=4)
    
# print("Liste d'utilisateurs sauvegardée.")

# """
# Étape 5 : Lire une liste de dictionnaires
# -----------------------------------------
# """

# with open("utilisateurs.json", "r", encoding="utf-8") as f:
#     liste = json.load(f)
# for user in liste:
#     print(f"{user['nom']} a {user['age']} ans.")

# """
# Étape 6 : Gérer les erreurs lors de la lecture
# ----------------------------------------------
# """

# try:
#     with open("utilisateur.json", "r", encoding="utf-8") as f:
#         data = json.load(f)
# except FileNotFoundError:
#     print("Erreur : le fichier n'existe pas.")
# except json.JSONDecodeError:
#     print("Erreur : le fichier n'est pas un JSON valide.")

"""
Étape 7 : Sérialiser des objets non standards
---------------------------------------------
Par défaut, json ne sait pas enregistrer certains objets (ex : datetime).
On peut utiliser une fonction personnalisée.
"""

import datetime

def encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Type non sérialisable : {type(obj)}")

evenement = {
    "nom": "Rendez-vous",
    "date": datetime.datetime.now()
}

with open("evenement.json", "w", encoding="utf-8") as f:
    json.dump(evenement, f, default=encoder, indent=4)
print("Evenement sauvegardé avec date sérialisée.")