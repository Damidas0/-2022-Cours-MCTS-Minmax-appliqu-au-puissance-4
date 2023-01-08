from P4 import * 
import copy
import random

MAX_DEPTH_MINMAX = 2.0


def robot_joue_mieux(liste, grille, max_depth):
    colonneAJouer = score(grille, max_depth, 1)
    return colonneAJouer



def EvaluerGrille(grille):

    if verif_gagnage(MINMAX_COULEUR, grille):
        return 100 
    if verif_gagnage(MCTS_COULEUR, grille):
        return -100
    else:
        # les scores sont a modifier pour que ce soit pertinent 
        scorePourTrois = 5
        scorePourDeux = 2
        scorePourDeuxPiege = 3

        #compter le nombre de coup pour trois 
        score = 0; 

        val = MINMAX_COULEUR.value 

        for c in range (NB_COLONNES) : 
            for l in range (NB_LIGNES) : 
                if (grille[c][l] == val) :

                    if (c < NB_COLONNES - 2) :
                        if (l > 2) :    
                            #Verification de la diagonale bas droite
                            if (grille[c + 1][l - 1] == val):
                                if (grille[c+2][l - 2] == val) : 
                                    if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                        if (grille[c+3][l-3] == " ") : 
                                            score = score + scorePourTrois
                                    elif ((c > 0) and (l < NB_LIGNES - 1)) :
                                        if (grille[c-1][l+1] == " ") : 
                                            score = score + scorePourTrois
                                elif (grille[c+2][l-2] == " ") : 
                                    if ((c > 0) and (l < NB_LIGNES - 1)) :
                                        if (grille[c-1][l+1] == " ") : 
                                            score = score + scorePourDeux



                        if (l < NB_LIGNES - 2) : 
                            #Verification de la diagonale haut droite
                            if (grille[c + 1][l + 1] == val):
                                if (grille[c+2][l+2] == val) : 
                                    if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                        if (grille[c+3][l+3] == " ") : 
                                            score = score + scorePourTrois
                                    elif ((c > 0) and (l > 0)) :
                                        if (grille[c-1][l-1] == " ") : 
                                            score = score + scorePourTrois
                                elif (grille[c+2][l+2] == " ") : 
                                    if ((c > 0) and (l > 0)) :
                                        if (grille[c-1][l-1] == " ") : 
                                            score = score + scorePourDeux
                        
                        #verification ligne
                        if (grille[c + 1][l] == val):
                                if (grille[c+2][l] == val) : 
                                    if (c < NB_COLONNES - 3) :
                                        if (grille[c+3][l] == " ") : 
                                            score = score + scorePourTrois
                                    elif (c > 0) :
                                        if (grille[c-1][l] == " ") : 
                                            score = score + scorePourTrois
                                elif (grille[c+2][l] == " ") : 
                                    if (c > 0) :
                                        if (grille[c-1][l] == " ") : 
                                            if (c > 1) : 
                                                if (grille[c-2][l] == " ") :
                                                    score = score + scorePourDeuxPiege
                                            if (c < NB_COLONNES - 3) : 
                                                if (grille[c+2][l] == " ") :
                                                    score = score + scorePourDeuxPiege
                                            score = score + scorePourDeux
                    if (l < NB_LIGNES - 3) :
                        #verification colonne
                        if (grille[c][l + 1] == val):
                            if (grille[c][l+2] == val) : 
                                if (grille[c][l+3] == " ") : 
                                    score = score + scorePourTrois
                            if (grille[c][l+2] == val) :
                                score = score + scorePourDeux


                                
        val = MCTS_COULEUR.value 

        for c in range (NB_COLONNES) : 
            for l in range (NB_LIGNES) : 
                if (grille[c][l] == val) :

                    if (c < NB_COLONNES - 2) :
                        if (l > 2) :    
                            #Verification de la diagonale bas droite
                            if (grille[c + 1][l - 1] == val):
                                if (grille[c+2][l - 2] == val) : 
                                    if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                        if (grille[c+3][l-3] == " ") : 
                                            score = score - scorePourTrois
                                    elif ((c > 0) and (l < NB_LIGNES - 1)) :
                                        if (grille[c-1][l+1] == " ") : 
                                            score = score - scorePourTrois
                                elif (grille[c+2][l-2] == " ") : 
                                    if ((c > 0) and (l < NB_LIGNES - 1)) :
                                        if (grille[c-1][l+1] == " ") : 
                                            score = score - scorePourDeux



                        if (l < NB_LIGNES - 2) : 
                            #Verification de la diagonale haut droite
                            if (grille[c + 1][l + 1] == val):
                                if (grille[c+2][l+2] == val) : 
                                    if ((c < NB_COLONNES - 3) and (l < NB_LIGNES - 3)) :
                                        if (grille[c+3][l+3] == " ") : 
                                            score = score - scorePourTrois
                                    elif ((c > 0) and (l > 0)) :
                                        if (grille[c-1][l-1] == " ") : 
                                            score = score - scorePourTrois
                                elif (grille[c+2][l+2] == " ") : 
                                    if ((c > 0) and (l > 0)) :
                                        if (grille[c-1][l-1] == " ") : 
                                            score = score - scorePourDeux
                        
                        #verification ligne
                        if (grille[c + 1][l] == val):
                                if (grille[c+2][l] == val) : 
                                    if (c < NB_COLONNES - 3) :
                                        if (grille[c+3][l] == " ") : 
                                            score = score - scorePourTrois
                                    elif (c > 0) :
                                        if (grille[c-1][l] == " ") : 
                                            score = score - scorePourTrois
                                elif (grille[c+2][l] == " ") : 
                                    if (c > 0) :
                                        if (grille[c-1][l] == " ") : 
                                            if (c > 1) : 
                                                if (grille[c-2][l] == " ") :
                                                    score = score - scorePourDeuxPiege
                                            if (c < NB_COLONNES - 3) : 
                                                if (grille[c+2][l] == " ") :
                                                    score = score - scorePourDeuxPiege
                                            score = score - scorePourDeux
                    if (l < NB_LIGNES - 3) :
                        #verification colonne
                        if (grille[c][l + 1] == val):
                            if (grille[c][l+2] == val) : 
                                if (grille[c][l+3] == " ") : 
                                    score = score - scorePourTrois
                            if (grille[c][l+2] == val) :
                                score = score - scorePourDeux
        return score


def score(grille,max_depth,minimizer):
    grille_tampon=copy.deepcopy(grille)
    scoreTampon=0
    scoreJouer = 0
    colonneAJouer = 0
    liste_coup = liste_coup_possible(grille)
    #print(liste_coup, "c'est la liste de coups possible")
    liste_colonne_jouable=[]
    for j in range(len(liste_coup)):
        colonne = liste_coup[j][0]
        if minimizer:
            grille_tampon=jouer_coup(MINMAX_COULEUR, colonne, grille_tampon)
            #afficher_grille(grille_tampon)
            scoreTampon = minmax(grille_tampon, 4, not(minimizer))
            #print (scoreTampon," pour la colonne ", colonne)
            if (j==0) : 
                scoreJouer = scoreTampon 
            if(scoreTampon==scoreJouer):
                liste_colonne_jouable.append(colonne)
                #colonneAJouer=random.choice([colonneAJouer, colonne])
            elif (scoreTampon>scoreJouer):
                scoreJouer=scoreTampon
                liste_colonne_jouable=[colonne]
                #colonneAJouer = colonne
            #print(colonneAJouer, " est pour le moment la meilleure colonne")
        else :
            grille_tampon=jouer_coup(MCTS_COULEUR, colonne, grille_tampon)
            scoreTampon = minmax(grille_tampon, 4, not(minimizer))
            #print (scoreTampon)
            if (j==0) : 
                scoreJouer = scoreTampon
            if(scoreTampon==scoreJouer):
                liste_colonne_jouable.append(colonne)
                #colonneAJouer=random.choice([colonneAJouer, colonne])
            elif (scoreTampon>scoreJouer):
                scoreJouer=scoreTampon
                liste_colonne_jouable=[colonne]
                #colonneAJouer = colonne
        #print("hi there")
        grille_tampon=copy.deepcopy(grille)
    colonneAJouer=random.choice(liste_colonne_jouable)
    return colonneAJouer



def minmax(grille_virt, max_depth, minimizer):
    liste = []
    #afficher_grille (grille_virt)
    #print (max_depth)
#---Conditions d'arrets-------#
    evaluation=EvaluerGrille(grille_virt)
    if verif_gagnage(MINMAX_COULEUR, grille_virt) : 
        return 100 * max_depth
    if verif_gagnage(MCTS_COULEUR, grille_virt) :
        return -100 * max_depth


    if (max_depth == 0):  # remettre elif quand on aura la fin de partie
        #return evalue_grille(grille_virt);
        return evaluation
#---BOUCLE D'APPLICATION-------#
    else:
        liste_coup = liste_coup_possible(grille_virt)
        for i in range(len(liste_coup)):
            coup = liste_coup[i][0]
            #print(liste_coup[i])
            if (minimizer):
                #print("a")
                grille_tmp = copy.deepcopy(grille_virt)
                grille_tmp = jouer_coup(MINMAX_COULEUR, coup, grille_tmp)

            else:
                #print("b")
                grille_tmp = copy.deepcopy(grille_virt)
                grille_tmp = jouer_coup(MCTS_COULEUR, coup, grille_tmp)

            #print(liste)
            liste.append(minmax(grille_tmp, max_depth - 1, not (minimizer)))

        if ((minimizer)):
            #print (liste)
            return max(liste, default=0)
        else:
            #print (liste)
            return min(liste, default=0)