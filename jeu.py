from Grille import Grille
import time as tm

class Jeu:
    
    def __init__(self, nb_colonnes, nb_lignes, taux = 0.5, vitesse = 0.1):
        self.grille = Grille(nb_lignes, nb_colonnes)
        self.grille.remplir_aleatoirement(taux)
        self.grille.trouve_voisins()
        self.vitesse = vitesse

    def start(self):
        """"Cette méthode affiche la grille"""
        self.calcul_etat_suivant()
        self.maj_grille()
        tm.sleep(self.vitesse)
        
    def maj_grille(self):
        """Cette méthode fait la mise à jour de la grille"""
        self.grille.maj_grille()

    def calcul_etat_suivant(self):
        """Cette méthode calcule l'état suivant des cellules de la grille"""
        self.grille.calcul_etat_suivant()
        
    def __str__(self):
        return jeu.grille.__str__()


if __name__ == "__main__":
    jeu = Jeu(30, 30, 0.3)
    while True:
        print(jeu)
        jeu.start()
        print("\u001B[H\u001B[J")
