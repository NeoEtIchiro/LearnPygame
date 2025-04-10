# ------------------------------------------------------------
print(" 1. Programmation Orientée Objet (POO)")
# ------------------------------------------------------------

# Définition d'une classe "Personne" avec un constructeur et une méthode pour afficher les informations.
class Personne:
    def __init__(self, nom, age):
        """
        Le constructeur initialise les attributs 'nom' et 'age'.
        """
        self.nom = nom
        self.age = age

    def afficher_info(self):
        """
        Affiche les informations de la personne.
        """
        print("Nom: ", self.nom, "Âge: ", self.age)

# Création d'une instance de la classe Personne
personne1 = Personne("Alice", 30)
personne2 = Personne("Jean", 40)
personne92 = Personne("92", 92)

print("Exemple d'objet (Personne92):")
personne92.afficher_info()
print()

print("Exemple d'objet (Personne2):")
personne2.afficher_info()
print()

print("Accéder directmenet à un attribur de l'objet:")
print(personne1.nom)
print()

# ------------------------------------------------------------
print(" 2. Héritage en POO")
# ------------------------------------------------------------
# L'héritage permet de créer une classe dérivée qui hérite des attributs et méthodes de la classe parente.
# Exemple : Création de la classe "Employe" qui hérite de "Personne"

class Employe(Personne):
    def __init__(self, nom, age, salaire):
        """
        Le constructeur initialise les attributs hérités de Personne et ajoute 'salaire'.
        """
        super().__init__(nom, age)  # Appel du constructeur de la classe parente
        self.salaire = salaire

    def afficher_info(self):
        """
        Affiche les informations de l'employé en complétant celles de la classe Personne.
        """
        super().afficher_info()
        print(f"Salaire: {self.salaire}")

# Création d'une instance de la classe Employe
employe1 = Employe("Bob", 40, 3000)

print("Exemple d'objet avec héritage:")
employe1.afficher_info()

# ------------------------------------------------------------
print(" 3. Importation de modules personnalisés")
# ------------------------------------------------------------
# Importation du module "module_utilitaires" depuis le dossier "Scripts cours"
import module_utilitaires as mu

print("Exemple d'importation d'un module personnalisé depuis 'Scripts cours':")
message = mu.dire_bonjour("Alice")
print(message)

# Importation de fonction spécifique
from module_utilitaires import dire_bonjour # Pour importer plusieurs fonction sépare les part une virgule, exemple : from module_utilitaires import dire_bonjour, dire_bonsoir

print("Autre exemple :")
message = dire_bonjour("Alice")
print(message)

# Importation de toute les fonctions d'un coup
from module_utilitaires import *

print("Autre exemple :")
message = dire_bonjour("Alice")
print(message)