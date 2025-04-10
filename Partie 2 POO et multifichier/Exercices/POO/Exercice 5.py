"""
Exercice POO 5 : Compte Bancaire

Objectif :
    - Créez une classe "CompteBancaire" avec un attribut "solde" initialisé à 0.
    - Ajoutez une méthode "deposer" qui ajoute un montant au solde.
    - Ajoutez une méthode "retirer" qui soustrait un montant du solde uniquement si le solde est suffisant.
    - Ajoutez une méthode "afficher_solde" qui affiche le solde actuel.

Conseils :
    - Utilisez le nom de la variable ou le compte a été initialisé suivi d'un point pour accéder au attributs de l'instance
    - Gérez les erreurs en vérifiant si le solde est suffisant avant un retrait.
"""

class CompteBancaire:
    def __init__(self):
        self.solde = 0

    def deposer(self, montant):
        """
        Ajoute le montant spécifié au solde.
        """
        if montant > 0:
            self.solde += montant
            print(f"Déposé : {montant}€. Nouveau solde : {self.solde}€")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        """
        Retire le montant spécifié du solde si possible.
        """
        if montant > self.solde:
            print("Solde insuffisant pour ce retrait.")
        elif montant <= 0:
            print("Le montant à retirer doit être positif.")
        else:
            self.solde -= montant
            print(f"Retiré : {montant}€. Nouveau solde : {self.solde}€")

    def afficher_solde(self):
        """
        Affiche le solde actuel.
        """
        print(f"Solde actuel : {self.solde}€")

# Test de la classe CompteBancaire
compte = CompteBancaire()
compte.deposer(150)
compte.retirer(40)
compte.afficher_solde()
print("Accès via propriété 'solde' :", compte.solde)