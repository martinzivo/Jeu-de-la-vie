from Cellule import Cellule
import random as rdm

class Grille:

    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.matrice = [[Cellule() for j in range(nb_colonnes)] for i in range(nb_lignes)]
        
    def get_cellule(self, x, y):
        """Cette méthode renvoie la cellule de coordonnées x et y"""
        return self.matrice[x][y]

    def trouve_voisins(self):
        """Cette méthode trouve les voisins de chaque cellule et les stocke
        dans l'attribut voisins"""
        for x in range(self.nb_lignes):
            for y in range(self.nb_colonnes):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not(x == 0 and x == y and y == 0):
                            xx = ((x + i) + self.nb_lignes) % self.nb_lignes
                            yy = ((y + j) + self.nb_colonnes) % self.nb_colonnes
                            if self.get_cellule(x, y) != self.get_cellule(xx, yy):
                                self.get_cellule(x, y).set_voisin(self.get_cellule(xx, yy))

    def maj_grille(self):
        """Cette méthode met à jour la grille"""
        for x in range(self.nb_lignes):
            for y in range(self.nb_colonnes):
                elt = self.get_cellule(x, y)
                elt.maj_etat(elt.give_etat_suivant())
                
    def calcul_etat_suivant(self):
        for x in range(self.nb_lignes):
            for y in range(self.nb_colonnes):
                elt = self.get_cellule(x, y)
                elt.calcul_etat_suivant()
                


    def remplir_aleatoirement(self, taux):
        """Cette méthode initialise l'état des cellules avec un taux de
        cellules vivantes"""
        for x in range(self.nb_lignes):
            for y in range(self.nb_colonnes):
                if rdm.random() > taux:
                    self.get_cellule(x, y).maj_etat(False)
                else:
                    self.get_cellule(x, y).maj_etat(True)

    def __str__(self):
        result = ""
        for x in range(self.nb_lignes):
            for y in range(self.nb_colonnes):
                result += str(self.matrice[x][y]) + " "
            result += "\n"
        return result
        
if __name__ == "__main__":
    grille = Grille(10, 10)
    grille.remplir_aleatoirement(0.2)
    print(grille)
    assert grille.nb_lignes == 10
    assert grille.nb_colonnes == 10
    assert len(grille.matrice) == 10

