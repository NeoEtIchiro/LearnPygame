class Grid:
    """
    Classe qui gère la grille du Jeu de la vie de Conway.
    Chaque cellule peut être vivante (1) ou morte (0).
    """

    def __init__(self, rows, cols):
        """
        Initialise la grille avec le nombre de lignes et de colonnes donné.
        Toutes les cellules sont mortes au départ.
        """
        self.rows = rows
        self.cols = cols
        self.reset()  # Crée la grille vide

    def reset(self):
        """
        Remet toutes les cellules à zéro (mortes).
        """
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def randomize(self, prob=0.2):
        """
        Remplit la grille avec des cellules vivantes aléatoirement.
        prob : probabilité qu'une cellule soit vivante (entre 0 et 1).
        """
        from random import random
        self.cells = [[1 if random() < prob else 0 for _ in range(self.cols)] for _ in range(self.rows)]

    def count_neighbors(self, r, c):
        """
        Compte le nombre de cellules vivantes autour de la cellule (r, c).
        Les voisins sont les 8 cellules autour (haut, bas, gauche, droite, diagonales).
        """
        count = 0
        for i in range(r-1, r+2):      # Parcourt les lignes voisines
            for j in range(c-1, c+2):  # Parcourt les colonnes voisines
                # Ignore la cellule centrale et les indices hors grille
                if (i == r and j == c) or i < 0 or j < 0 or i >= self.rows or j >= self.cols:
                    continue
                count += self.cells[i][j]  # Ajoute 1 si la cellule est vivante
        return count

    def next_generation(self):
        """
        Calcule la prochaine génération selon les règles du Jeu de la vie :
        - Une cellule vivante avec 2 ou 3 voisins survit.
        - Une cellule morte avec exactement 3 voisins devient vivante.
        - Sinon, la cellule meurt ou reste morte.
        """
        new = [[0] * self.cols for _ in range(self.rows)]  # Nouvelle grille
        for r in range(self.rows):
            for c in range(self.cols):
                n = self.count_neighbors(r, c)
                if self.cells[r][c] == 1 and n in (2, 3):
                    new[r][c] = 1  # Survie
                elif self.cells[r][c] == 0 and n == 3:
                    new[r][c] = 1  # Naissance
                # Sinon, reste morte (0)
        self.cells = new  # Met à jour la grille

    def toggle(self, r, c, value=None):
        """
        Change l'état d'une cellule (vivante/morte).
        - Si value est None : inverse l'état (vivant <-> mort).
        - Si value vaut 0 ou 1 : force la cellule à cette valeur.
        """
        if 0 <= r < self.rows and 0 <= c < self.cols:
            if value is None:
                self.cells[r][c] = 1 - self.cells[r][c]
            else:
                self.cells[r][c] = value
