# Ce fichier est un cours intermédiaire sur Python.
# Il aborde notamment la manipulation des chaînes de caractères et quelques autres concepts avancés.

# ------------------------------------------------------------
print(" 1. Manipulation de chaînes de caractères")
# ------------------------------------------------------------

# Une chaîne de caractères (string) est une séquence immuable de caractères.
message = "Bienvenue dans le cours intermédiaire de Python"

# Accéder à un caractère ou une sous-chaîne (slicing)
print("Caractère à l'index 0 :", message[0])
print("Sous-chaîne (de l'index 11 à 18) :", message[11:19])

# Les méthodes utiles sur les chaînes
# - upper() et lower()
print("Message en majuscules :", message.upper())
print("Message en minuscules :", message.lower())

# - strip() pour enlever les espaces en début et fin de chaîne
texte = "   Python est génial!   "
print("Texte original :", f"'{texte}'")
print("Après strip() :", f"'{texte.strip()}'")

# - replace() pour remplacer des sous-chaînes
print("Remplacer 'Python' par 'Java' :", message.replace("Python", "Java"))

# - split() pour diviser une chaîne en liste
liste_mots = message.split()
print("Liste des mots :", liste_mots)

# - join() pour réunir une liste de chaînes en une seule chaîne
print("Rejoindre les mots avec '-' :", "-".join(liste_mots))

print()

# ------------------------------------------------------------
print(" 2. Formatage de chaînes")
# ------------------------------------------------------------

# Utilisation des f-strings (introduit dans Python 3.6) pour un formatage lisible
nom = "Alice"
age = 30
print(f"Félicitations {nom} ! Vous avez {age} ans.")

# La méthode format() est également utilisée pour substituer des valeurs dans une chaîne
template = "Bonjour {0}, votre solde est de {1:.2f}€."
solde = 1234.5678
print(template.format(nom, solde))

print()

# ------------------------------------------------------------
print(" 3. Expressions régulières (Notion avancée)")
# ------------------------------------------------------------

# Les expressions régulières permettent de rechercher, valider ou modifier des chaînes selon des motifs précis.
import re

exemple_texte = "Contactez-nous à l'adresse email: contact@example.com pour plus d'informations."

# Rechercher une adresse email dans une chaîne
motif = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultat = re.search(motif, exemple_texte)
if resultat:
    print("Adresse email trouvée :", resultat.group())
else:
    print("Aucune adresse email trouvée.")

# Utiliser re.findall pour récupérer tous les motifs dans une chaîne
texte_multi = "Les emails de contact sont: alice@example.com, bob@site.org et charlie@mail.net."
emails = re.findall(motif, texte_multi)
print("Liste d'emails trouvée :", emails)

print()

# ------------------------------------------------------------
print(" 4. Autres compétences intermédiaires")
# ------------------------------------------------------------

# Exemple de compréhension de liste pour manipuler des chaînes
# Convertir tous les mots d'une phrase en majuscules
mots_maj = [mot.upper() for mot in liste_mots]
print("Mots en majuscules :", mots_maj)

# Concaténer des chaînes avec condition
mots_courts = [mot for mot in liste_mots if len(mot) <= 6]
print("Mots de 6 lettres ou moins :", mots_courts)

print("\nFin du cours intermédiaire sur la manipulation de chaînes et d'autres compétences en Python.")