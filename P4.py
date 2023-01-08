from enum import Enum

NB_LIGNES = 6
NB_COLONNES = 7

class couleur(Enum):
    rouge = 'x'
    jaune = 'o'

MCTS_COULEUR = couleur.rouge
MINMAX_COULEUR = couleur.jaune

def grille_initialisation():
    grille= [[' ' for i in range(6)] for i in range(7)]
    return grille

def grille_est_pleine(grille) : 
    for c in range (7) : 
        if (grille[c][5] == " ") : 
            return False 
    return True

def jouer_coup(couleur, no_colonne, grille):
    for i in range(6):
        if grille[no_colonne][i] == ' ':
            grille[no_colonne][i] = couleur.value
            return grille
    return grille

#Ponderer en fonction de la profondeur 
#sur de gagner ou sur de perdre mettre +-100 
#essayez d'évaluer lorsqu'il ya des alignements de 3
#Fonction d'évalution totale de la grille à chaque état

def liste_coup_possible(grille):  # Renvoi la liste des tout les coups possibles
    liste_coup = []
    for i in range(7):  # aller jusqu'à 7 me semble assez délirant
        possible = coup_possible(i, grille)
        if (possible != "nan"):
            liste_coup.append((i, possible))
    return liste_coup


def coup_possible(col, grille):  # Renvoie si une colonne est jouable
    for i in range(6):
        if (grille[col][i] == " "):
            return i
    return "nan"


def afficher_grille(grille):
    for i in range(6):
        for j in range(7):
            print("[", grille[j][5 - i], "]", end=" ")
        print("\n")
    print(" ========================================")
    print("\n")


def verif_gagnage(couleur, grille):
    val = couleur.value #est ce qu'on devrait pas vérifier que ce soit vide autour dans un 1er temps pour l'opti ?
    for c in range(NB_COLONNES - 3):
        for l in range(NB_LIGNES):
            if (grille[c][l] == val and grille[c + 1][l] == val and grille[c + 2][l] == val and grille[c + 3][l] == val):
                return True

    for c in range(NB_COLONNES):
        for l in range(NB_LIGNES - 3):
            if (grille[c][l] == val and grille[c][l + 1] == val and grille[c][l + 2] == val and grille[c][l + 3] == val):
                return True

    for c in range(NB_COLONNES - 3):
        for l in range(NB_LIGNES - 3):
            if (grille[c][l] == val and grille[c + 1][l + 1] == val and grille[c + 2][l + 2] == val and grille[c + 3][l + 3] == val):
                return True

    for c in range(NB_COLONNES - 3):
        for l in range(3, NB_LIGNES):
            if (grille[c][l] == val and grille[c + 1][l - 1] == val and grille[c + 2][l - 2] == val and grille[c + 3][l - 3] == val):
                return True
    return False