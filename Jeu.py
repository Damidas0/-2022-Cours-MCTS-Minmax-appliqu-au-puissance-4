import random
import os
import openpyxl as px
import time 
from P4 import * 
from MCTS import *
from Minmax import *



def returnString(grille):
    ret = ""
    for i in range(6):
        for j in range(7):
            ret += "[" + grille[j][5 - i] + "]"
        ret += "\n"
    ret += " ========================================"
    ret += "\n"
    return ret


def jouerMinMax(grille):
    joue = True
    no_tour = 0
    if(MINMAX_COULEUR==couleur.jaune):
        while joue:
            print(no_tour)
            if (no_tour % 2) == 0:
                coup = humain_joue(grille)
                grille = jouer_coup(couleur.rouge,coup,grille)
                joue = not (verif_gagnage(couleur.rouge, grille))
            else:
                coup = robot_joue_mieux(liste_coup_possible(grille), grille)
                grille = jouer_coup(couleur.jaune, coup, grille)
                joue = not (verif_gagnage(couleur.jaune, grille))
            afficher_grille(grille)
            no_tour = no_tour + 1
    else:
        while joue:
            print(no_tour)
            if (no_tour % 2) != 0:
                coup = humain_joue(grille)
                grille = jouer_coup(couleur.jaune,coup,grille)
                joue = not (verif_gagnage(couleur.jaune, grille))
            else:
                coup = robot_joue_mieux(liste_coup_possible(grille), grille)
                grille = jouer_coup(couleur.rouge, coup, grille)
                joue = not (verif_gagnage(couleur.rouge, grille))
            afficher_grille(grille)
            no_tour = no_tour + 1


def jouerMCTS(grille) : 
    joue = True
    no_tour = 0
    noeud_racine = Node(grille, None, 0, None)
    if(MCTS_COULEUR==couleur.jaune):
        while joue :
            if (no_tour % 2) == 0 :           
                coup = humain_joue(grille)
                grille = jouer_coup(couleur.rouge, coup, grille)
                joue = not (verif_gagnage(couleur.rouge, grille))
                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                
                else : 
                    noeud_racine = Node(grille, None, 1, None)
            else :
                coup = robot_joue_encore_mieux(noeud_racine, MCTS_COULEUR)[0]
                print (coup, " coup joué")
                afficher_grille(noeud_racine.etat)
                grille = jouer_coup(couleur.jaune, coup, grille)
                joue = not (verif_gagnage(couleur.jaune, grille))
                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()               
                else : 
                    noeud_racine = Node(grille, None, 0, None)
            afficher_grille(grille)
            no_tour = no_tour + 1
    else:
        while joue :
            if (no_tour % 2) != 0 :           
                coup = humain_joue(grille)
                grille = jouer_coup(couleur.jaune, coup, grille)
                joue = not (verif_gagnage(couleur.jaune, grille))
                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                
                else : 
                    noeud_racine = Node(grille, None, 1, None)
            else :
                coup = robot_joue_encore_mieux(noeud_racine, MCTS_COULEUR)[0]
                print (coup, " coup joué")
                afficher_grille(noeud_racine.etat)
                grille = jouer_coup(couleur.rouge, coup, grille)
                joue = not (verif_gagnage(couleur.rouge, grille))
                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()               
                else : 
                    noeud_racine = Node(grille, None, 0, None)
            afficher_grille(grille)
            no_tour = no_tour + 1

def choisirCouleurIAs():
    couleurMinMax = random.choice([couleur.rouge,couleur.jaune])
    if(couleurMinMax==couleur.rouge):
        couleurMCTS=couleur.jaune
        return [couleurMinMax, couleurMCTS]
    else:
        couleurMCTS=couleur.rouge
        return [couleurMinMax, couleurMCTS]


def jouerMinmaxMCTS(grille) : 
    chemin = os.getcwd()
    print(chemin)
    if os.path.exists( chemin + "\\temps.xlsx") : 
        wb = px.load_workbook(chemin + "\\temps.xlsx")
    else : 
        wb = px.Workbook()
    nom = str(MCTS_ITERATION)+ '_' + str(MAX_DEPTH_MINMAX) + '_' + str(C)
    if not nom in wb.sheetnames :
        wb.create_sheet(nom)
        wb.active = wb[nom]
        
        ws = wb.active
        ws['A1'] = 'Nombre de partie jouée'
        ws['A2'] = 0
        ws['B1'] = 'Numero Tour'
        ws['C1'] = 'nb de passage'
        ws['D1'] = "MCTS temps moyen"
        ws['E1'] = "MINMAX temps moyen" 
        ws['F1'] = "Nombre Victoire MCTS"
        ws['G1'] = "Nombre Victoire Minmax"
        ws['F2'] = 0
        ws['G2'] = 0
    
    else : 
        wb.active = wb[nom]
        
        ws = wb.active
    ws['A2'] = ws['A2'].value + 1
        
    
    joue = True
    no_tour = 0
    noeud_racine = Node(grille, None, 1, None)
    tempsMCTS=0
    tempsMINMAX=0
    compteur = 1
    if(MCTS_COULEUR==couleur.rouge):
        while joue :
            
            
            compteur += no_tour % 2
            ws['B'+str(compteur+2)] = compteur

            if  ws['C'+str(compteur+2)].value == None : 
                ws['C'+str(compteur+2)] = 1
            else : 
                ws['C'+str(compteur+2)] = ws['C'+str(compteur+2)].value + 1 
                
            if (no_tour % 2) == 0 :
                
                tmpMCTS = time.perf_counter()
                coup = robot_joue_encore_mieux(noeud_racine, MCTS_COULEUR)[0]
                
                tmpMCTS = time.perf_counter() - tmpMCTS
                tempsMCTS += tmpMCTS
                if  ws['D'+str(compteur+2)].value == None : 
                    ws['D'+str(compteur+2)] = tmpMCTS
                else : 
                    ws['D'+str(compteur+2)] = ((tmpMCTS) + (ws['C'+str(compteur+2)].value -1) *  ws['D'+str(compteur+2)].value ) / ws['C'+str(compteur+2)].value
                
                print (coup, " coup joué")
                afficher_grille(noeud_racine.etat)
                grille = jouer_coup(MCTS_COULEUR, coup, grille)
                joue = not (verif_gagnage(MCTS_COULEUR, grille))

                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                    
                else : 
                    noeud_racine = Node(grille, None, 0, None)
            else :
                tmpMinMax = time.perf_counter()
                coup = robot_joue_mieux(liste_coup_possible(grille), grille)
                tmpMinMax = time.perf_counter() - tmpMinMax
                tempsMINMAX += tmpMinMax
                
                if ws['E'+str(compteur+1)].value == None : 
                    ws['E'+str(compteur+1)] = tmpMinMax
                else : 
                    ws['E'+str(compteur+1)] = ((tmpMCTS) + (ws['C'+str(compteur+1)].value - 1) *  ws['E'+str(compteur+1)].value) / ws['C'+str(compteur+1)].value
                
                
                print (coup, " coup joué")
                grille = jouer_coup(MINMAX_COULEUR, coup, grille)
                joue = not (verif_gagnage(MINMAX_COULEUR, grille))
                

                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                    
                else : 
                    noeud_racine = Node(grille, None, 1, None)
            afficher_grille(grille)
            no_tour = no_tour + 1

            
            
            if grille_est_pleine(grille) : 
                return 0
        
        if (no_tour % 2 == 0) :
            ws['G2'] =  ws['G2'].value + 1
            wb.save(chemin + "\\temps.xlsx") 
            return -1 #victoire de Minmax
        else :
            
            ws['F2'] =  ws['F2'].value + 1
            wb.save(chemin + "\\temps.xlsx") 
            return 1 #victoire de MCTS
    else :  
        while joue :
            
            
            compteur += no_tour % 2
            ws['B'+str(compteur+2)] = compteur

            if  ws['C'+str(compteur+1)].value == None : 
                ws['C'+str(compteur+1)] = 1
            else : 
                ws['C'+str(compteur+1)] = ws['C'+str(compteur+1)].value + 1 
                
            if (no_tour % 2) != 0 :
                
                tmpMCTS = time.perf_counter()
                coup = robot_joue_encore_mieux(noeud_racine, MCTS_COULEUR)[0]
                
                tmpMCTS = time.perf_counter() - tmpMCTS
                tempsMCTS += tmpMCTS
                if  ws['D'+str(compteur+1)].value == None : 
                    ws['D'+str(compteur+1)] = tmpMCTS
                else : 
                    ws['D'+str(compteur+1)] = ((tmpMCTS) + (ws['C'+str(compteur+1)].value -1) *  ws['D'+str(compteur+1)].value ) / ws['C'+str(compteur+1)].value
                
                print (coup, " coup joué")
                afficher_grille(noeud_racine.etat)
                grille = jouer_coup(MCTS_COULEUR, coup, grille)
                joue = not (verif_gagnage(MCTS_COULEUR, grille))

                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                    
                else : 
                    noeud_racine = Node(grille, None, 0, None)
            else :
                
                
                tmpMinMax = time.perf_counter()
                coup = robot_joue_mieux(liste_coup_possible(grille), grille)
                tmpMinMax = time.perf_counter() - tmpMinMax
                tempsMINMAX += tmpMinMax
                
                if ws['E'+str(compteur+2)].value == None : 
                    ws['E'+str(compteur+2)] = tmpMinMax
                else : 
                    if ws['C'+str(compteur+2)].value == None:
                        ws['C'+str(compteur+2)].value = 1
                    
                    ws['E'+str(compteur+2)] = ((tmpMinMax) + (ws['C'+str(compteur+2)].value - 1) *  ws['E'+str(compteur+2)].value) / ws['C'+str(compteur+2)].value
                
                
                print (coup, " coup joué")
                grille = jouer_coup(MINMAX_COULEUR, coup, grille)
                joue = not (verif_gagnage(MINMAX_COULEUR, grille))
                

                if (len(noeud_racine.enfants)>0) : 
                    no_enfant = noeud_racine.retrouveEnfant(coup)
                    noeud_racine = noeud_racine.enfants[no_enfant]
                    noeud_racine.devient_racine()
                    
                else : 
                    noeud_racine = Node(grille, None, 1, None)
            afficher_grille(grille)
            no_tour = no_tour + 1

            
            
            if grille_est_pleine(grille) : 
                return 0
        
        if (no_tour % 2 != 0) :
            ws['G2'] =  ws['G2'].value + 1
            wb.save(chemin + "\\temps.xlsx") 
            return -1 #victoire de Minmax
        else :
            
            ws['F2'] =  ws['F2'].value + 1
            wb.save(chemin + "\\temps.xlsx") 
            return 1 #victoire de MCTS


def humain_joue(grille):
    print("veuiller entre le numero de la colonne (allant de 0 à 6) dans laquelle vous voulez jouer")
    a = saisir(grille)
    #grille = jouer_coup(couleur.rouge, a, grille)
    return a

def saisir(grille):
    a = input()
    if not (a.isnumeric()):
        a = saisir(grille)
    a = int(a)
    if a < 0 or a > 6:
        print(
            "Cette colonne n'existe pas, rentrez a nouveau une colonne (allant de 0 à 6) dans laquelle vous voulez jouer")
        a = saisir(grille)
    if grille[a][5] != ' ':
        a = saisir(grille)
    return a


def choixModeDeJeu():
    print("Veuillez choisir le mode de jeu")
    print("Tapez 1 pour jouer contre MinMax, tapez 2 pour jouer contre MCTS, et tapez 3 pour se faire affronter les deux IAs")
    choix=input()
    if(not(choix.isnumeric())):
        ("erreur, entrez un nombre")
        choixModeDeJeu()
    print(choix)
    choix = int(choix)
    if(choix!=1 and choix!=2 and choix!=3):
        print("erreur, veuillez réessayez")
        choixModeDeJeu()
    return choix
