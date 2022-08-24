class Cellule:

    def __init__(self, etat = False):
        self.etat = etat
        self.etat_suivant = etat
        self.voisins = []

    def calcul_etat_suivant(self):
        acc = 0
        for voisin in self.voisins:
            if voisin.give_etat() == True:
                acc += 1
        if self.etat:
            if acc != 2 and acc != 3:
                self.etat_suivant = False    
        else:
            if acc == 3:
                    self.etat_suivant = True

    def give_etat(self):
        return self.etat

    def give_etat_suivant(self):
        return self.etat_suivant

    def give_voisins(self):
        return self.voisins

    def maj_etat(self, v):
        self.etat = v

    def maj_etat_suivant(self, v):
        self.etat_suivant = v

    def __str__(self):
        if self.etat:
            return "♥"
        return "."

    def set_voisin(self, voisin):
        self.voisins += [voisin]

if __name__ == "__main__":
    assert Cellule(True).etat == True
    assert Cellule(True).etat_suivant == True
    assert Cellule(True).voisins == []
