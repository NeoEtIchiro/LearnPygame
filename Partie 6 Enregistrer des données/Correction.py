import json
import os

# Exercice 1 : Sauvegarder un dictionnaire en JSON
animal = {"nom": "Rex", "espece": "chien", "age": 5}
with open("animal.json", "w", encoding="utf-8") as f:
    json.dump(animal, f, indent=4)

# Exercice 2 : Lire un fichier JSON
with open("animal.json", "r", encoding="utf-8") as f:
    animal_lu = json.load(f)
print("Animal lu :", animal_lu)

# Exercice 3 : Sauvegarder une liste de scores
scores = [
    {"nom": "Alice", "score": 120},
    {"nom": "Bob", "score": 95},
    {"nom": "Charlie", "score": 150}
]
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, indent=4)

# Exercice 4 : Lire et afficher les scores
with open("scores.json", "r", encoding="utf-8") as f:
    scores_lus = json.load(f)
for s in scores_lus:
    print(f"{s['nom']} : {s['score']} points")

# Exercice 5 : Ajouter un score à la liste existante
with open("scores.json", "r", encoding="utf-8") as f:
    scores = json.load(f)
scores.append({"nom": "David", "score": 110})
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, indent=4)

# Exercice 6 : Trier les scores
with open("scores.json", "r", encoding="utf-8") as f:
    scores = json.load(f)
scores_tries = sorted(scores, key=lambda x: x["score"], reverse=True)
for s in scores_tries:
    print(f"{s['nom']} : {s['score']} points")

# Exercice 7 : Supprimer un joueur
nom_supprimer = "Bob"

nouveaux_scores = []

# On parcourt chaque score dans la liste existante
for score in scores:
    # Si le nom du score est différent de celui à supprimer
    if score["nom"] != nom_supprimer:
        # On ajoute ce score à la nouvelle liste
        nouveaux_scores.append(score)

# On remplace l'ancienne liste par la nouvelle, sans le score supprimé
scores = nouveaux_scores
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(nouveaux_scores, f, indent=4)

# Exercice 8 : Modifier un score
nom_modifier = "Alice"
nouveau_score = 200
for s in scores:
    if s["nom"] == nom_modifier:
        s["score"] = nouveau_score
with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, indent=4)

# Exercice 9 : Fusionner deux fichiers JSON
liste1 = [{"nom": "Eve"}, {"nom": "Frank"}]
liste2 = [{"nom": "Grace"}, {"nom": "Heidi"}]
with open("liste1.json", "w", encoding="utf-8") as f:
    json.dump(liste1, f)
with open("liste2.json", "w", encoding="utf-8") as f:
    json.dump(liste2, f)
with open("liste1.json", "r", encoding="utf-8") as f:
    l1 = json.load(f)
with open("liste2.json", "r", encoding="utf-8") as f:
    l2 = json.load(f)
fusion = l1 + l2
with open("fusion.json", "w", encoding="utf-8") as f:
    json.dump(fusion, f, indent=4)

# Exercice 10 : Générer un rapport texte depuis un JSON
with open("scores.json", "r", encoding="utf-8") as f:
    scores = json.load(f)
scores_tries = sorted(scores, key=lambda x: x["score"], reverse=True)
with open("rapport.txt", "w", encoding="utf-8") as f:
    for i, s in enumerate(scores_tries, 1):
        f.write(f"{i}. {s['nom']} : {s['score']} points\n")

# Exercice 11 : Vérifier l'existence d'une clé
with open("animal.json", "r", encoding="utf-8") as f:
    animal = json.load(f)
cle = "espece"
if cle in animal:
    print(f"La clé '{cle}' existe dans le dictionnaire.")
else:
    print(f"La clé '{cle}' n'existe pas dans le dictionnaire.")