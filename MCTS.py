import random
import copy
from P4 import *
from math import sqrt, log

MCTS_ITERATION = 4000
C = 1.1

class Node:
    def __init__(self, etat, parent, joue, mouvement):
        self.etat = copy.deepcopy(etat)
        self.mouvement = mouvement
        self.joue = joue # booleen : donne a qui est le tour, True = c'est l'ordi qui joue
        self.parent = parent
        self.enfants = []
        self.listeScore=[0,0,0]
        self.nb_visites = 1
        

    def selection(self):
        if(self.enfants != []):
            poids = []
            for enfant in self.enfants:
                poids.append(int (100*enfant.calculerValeurNoeud()))
            #print(poids)
            
            tmp = random.choices(self.enfants, weights=poids)
            return tmp[0].selection()
        else:
            return self


    def extension (self) :
        if not (verif_gagnage(couleur.rouge, self.etat) or verif_gagnage(couleur.jaune, self.etat)) :
            coup_possible = liste_coup_possible(self.etat)
            for c in range (len(coup_possible)) :
                grille_tampon=copy.deepcopy(self.etat) 
                colonne = coup_possible[c][0]
                if (self.joue and MCTS_COULEUR == couleur.jaune) or ((not self.joue) and MCTS_COULEUR == couleur.rouge) :
                    jouer_coup(couleur.jaune, colonne, grille_tampon)
                else : 
                    jouer_coup(couleur.rouge, colonne, grille_tampon)
                noeud_tampon = Node(grille_tampon, self, not(self.joue), coup_possible[c])
                self.enfants.append(noeud_tampon)
                #afficher_grille(self.etat)
    

    def devient_racine(self) : 
        del self.parent
        self.parent = None

    def est_racine(self) :
        return self.parent == None
    
        


    def simulation (self):
        res = 0
        indicateur = True 
        iteration = 0
        temp = copy.deepcopy(self.etat)

        while (indicateur == True):
            
            liste_coup = liste_coup_possible(temp)
            if (len(liste_coup) > 0) :
                i =random.randint(0, len(liste_coup)-1)
                coup = liste_coup[i][0]

                
                if (self.joue and MCTS_COULEUR == couleur.jaune) or ((not self.joue) and MCTS_COULEUR == couleur.rouge):
                    val = couleur.jaune
                    val2 = couleur.rouge
                else:
                    val = couleur.rouge
                    val2 = couleur.jaune
                
                if (iteration % 2 == 0) : 
                    temp = jouer_coup(val, coup, temp)
                    if (verif_gagnage(val, temp)):
                        #afficher_grille(temp)
                        if (self.joue) : 
                            res = 1
                        else : 
                            res = -1
                        indicateur = 0        
                    
                else : 
                    temp = jouer_coup(val2, coup, temp)
                    if (verif_gagnage(val2, temp)):
                        #afficher_grille(temp)
                        if (self.joue) : 
                            res = -1
                        else : 
                            res = 1
                        indicateur = 0

                iteration += 1
            else :
                #afficher_grille(temp)
                res = 0
                indicateur = 0
                
        return res 
        





    def propagationDuResultat (self, resultat): #resultat designe le resultat de simulation
        tampon=self
        while (tampon.parent != None) :          
            if(resultat==0): #nulle
                tampon.listeScore[1]+=1
            elif(resultat==1): #vicroite
                tampon.listeScore[0]+=1
            elif(resultat==-1): #perdudos
                tampon.listeScore[2]+=1   #exemple : score est de la forme [nbrVictoires,nbrNulles,nbrDefaites]
            tampon.nb_visites+=1
            tampon=tampon.parent
        if(resultat==0): #nulle
            tampon.listeScore[1]+=1
        elif(resultat==1): #vicroite
            tampon.listeScore[0]+=1
        elif(resultat==-1): #perdudos
            tampon.listeScore[2]+=1   #exemple : score est de la forme [nbrVictoires,nbrNulles,nbrDefaites]
        tampon.nb_visites+=1
        


    def calculerValeurNoeud(self):     
        if(self.joue==True):
            nbVictoire=self.listeScore[0]
        if(self.joue==False): 
            nbVictoire=self.listeScore[2] #on souhaite qu'un noeud soit perdant pour l'adversaire   
        valeurMoyenne=nbVictoire/self.nb_visites

        #print(valeurMoyenne, "c'est la valeur moyenne")
        #print(self.parent.nb_visites/self.nb_visites, "c'est cette merde")
        #print(log(self.parent.nb_visites)/self.nb_visites, "pour voir")

        ret = valeurMoyenne + C*sqrt(log(self.parent.nb_visites)/self.nb_visites)
        #print (ret, " Valeur qui est en dessous de 0 apparement")
        return ret

    
    def meilleurEnfant(self):
        meilleurScore = 'nul'
        listeEnfants = []
        for c in range(len(self.enfants)) :
            listeScore=self.enfants[c].listeScore
            if (listeScore == [0, 0, 0]) :
                score = 0
            else :
                score = (listeScore[0] + 0.2 * listeScore[1]) / (listeScore[0] + listeScore[1] + listeScore[2])
            #afficher_grille(self.enfants[c].etat)
            #print ("Enfant no : ", c, " avec un score de ", score)
            if (meilleurScore == 'nul') :
                meilleurScore=score
                listeEnfants.append(self.enfants[c])
            if (score == meilleurScore):
                listeEnfants.append(self.enfants[c])
            if (score > meilleurScore):
                listeEnfants = [self.enfants[c]]
                meilleurScore = score 
        return random.choice(listeEnfants)

    def retrouveEnfant(self, mouvement) : 
        for e in range (len(self.enfants)) :
            if self.enfants[e].mouvement[0] == mouvement : 
                return e
        return 0



def robot_joue_encore_mieux(noeud_racine, val): #MCTS
    if (val == couleur.rouge) : 
        val2 = couleur.jaune 
    else :
        val2 = couleur.rouge
    for i in range (MCTS_ITERATION) :
        tmp = noeud_racine.selection()
        tmp.extension()
        if (len(tmp.enfants) != 0) :
            tmp = random.choice(tmp.enfants)
            simulation = tmp.simulation()
            tmp.propagationDuResultat(simulation)
        else : 
            
            if (verif_gagnage(val, tmp.etat)):
                simulation = 1
            elif (verif_gagnage(val2, tmp.etat)) :
                simulation = -1
            else : 
                simulation = 0 
            
        tmp.propagationDuResultat(simulation)
    
    return noeud_racine.meilleurEnfant().mouvement