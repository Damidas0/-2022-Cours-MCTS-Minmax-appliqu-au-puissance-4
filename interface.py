from Jeu import *

choix=choixModeDeJeu()
if(choix==1):
    print("HUMAIN VS MinMax")
    print("Choisissez la profondeur de MinMax (pas plus de 5)")
    MAX_DEPTH_MINMAX=input()
    if(not(MAX_DEPTH_MINMAX.isnumeric())):
        print("Vous n'avez pas entré de nombre. Choisissez la profondeur de MinMax (pas plus de 5)")
        MAX_DEPTH_MINMAX=input() 
    MAX_DEPTH_MINMAX = int(MAX_DEPTH_MINMAX)         
    if(MAX_DEPTH_MINMAX!=1 and MAX_DEPTH_MINMAX!=2 and MAX_DEPTH_MINMAX!=3 and MAX_DEPTH_MINMAX!=4 and MAX_DEPTH_MINMAX!=5):
        print("Choisissez la profondeur de MinMax (pas plus de 5)")
        MAX_DEPTH_MINMAX=input()               
    listeCouleur=choisirCouleurIAs()
    MCTS_COULEUR = listeCouleur[0]
    MINMAX_COULEUR = listeCouleur[1]
    if(MINMAX_COULEUR==couleur.rouge):
        print("MINMAX Commence")
    else:
        print("Vous commencez")
    grille_jeu=grille_initialisation()
    jouerMinMax(grille_jeu)

elif(choix==2):
    print("HUMAIN VS MCTS")
    print("Choisissez le nombre d'itérations de MCTS (cela doit-être un entier strictement positif")
    MCTS_ITERATION=input()
    MCTS_ITERATION = int(MCTS_ITERATION)
    #listeCouleur=choisirCouleurIAs()
    #MCTS_COULEUR = listeCouleur[0]
    #MINMAX_COULEUR = listeCouleur[1]
    MCTS_COULEUR=couleur.jaune # pour une raison que j'ignore, quand on appelle jouerMCTS, MCTS joue n'importe quand il débute
    if(MCTS_COULEUR==couleur.rouge):
        print("MCTS Commence")
    else:
        print("Vous commencez")
    grille_jeu=grille_initialisation()
    jouerMCTS(grille_jeu)

elif(choix==3):
    print("MCTS VS MinMax")
    print("Choisissez la profondeur de MinMax (pas plus de 5)")
    MAX_DEPTH_MINMAX=input()

    if(not(MAX_DEPTH_MINMAX.isnumeric())):
        print("Choisissez la profondeur de MinMax (pas plus de 5)")
        MAX_DEPTH_MINMAX=input() 

    MAX_DEPTH_MINMAX = int(MAX_DEPTH_MINMAX)
    if(MAX_DEPTH_MINMAX!=1 and MAX_DEPTH_MINMAX!=2 and MAX_DEPTH_MINMAX!=3 and MAX_DEPTH_MINMAX!=4 and MAX_DEPTH_MINMAX!=5):
            print("Choisissez la profondeur de MinMax (pas plus de 5)")
            MAX_DEPTH_MINMAX=input()
    print("Choisissez le nombre d'itérations de MCTS (cela doit-être un entier strictement positif")
    MCTS_ITERATION=input()

    if(not(MCTS_ITERATION.isnumeric() and int(MCTS_ITERATION)>0)):
        print("Choisissez le nombre d'itérations de MCTS (cela doit-être un entier strictement positif")
        MCTS_ITERATION=input()
    MCTS_ITERATION = int(MCTS_ITERATION)
    print("Choississez le nombre de parties à effectuer (entier strictement positif")
    nbrParties=input()

    if(not(nbrParties.isnumeric() and int(nbrParties)>0)):
        print("Choississez le nombre de parties à effectuer (entier strictement positif")
        nbrParties=input() 
        
    nbrParties=int(nbrParties)
    print("le résumé des résultats sera retranscrit dans un fichier qui sera dans votre répertoire")                          
    fichier = open("result_"+str(MAX_DEPTH_MINMAX)+"_"+str(MCTS_ITERATION)+"_.txt", "a")
    fichier.write("L'IA avec les x est l'IA qui joue en première " + "\n") 
    listeScore = []

    for c in range (15) : 
        C = C + (1/10)
        for i in range (nbrParties) :
            listeCouleur=choisirCouleurIAs()
            MCTS_COULEUR = listeCouleur[0]
            MINMAX_COULEUR = listeCouleur[1]
            if(MINMAX_COULEUR==couleur.rouge):
                print("MINMAX Commence")
            else:
                print("MCTS Commence")
            fichier.write("MCTS: " + MCTS_COULEUR.value + "\nMinMax: " + MINMAX_COULEUR.value + "\n") 
            grille_jeu = grille_initialisation()
            res = jouerMinmaxMCTS(grille_jeu)
            listeScore.append(res)
        fichier.write(returnString(grille_jeu))
        fichier.write("Pour MCTS de " + str(MCTS_ITERATION) + " d'iteration et MinMax a " + str(MAX_DEPTH_MINMAX) + " de profondeur : \n")
        fichier.write("Nombre de victoire de MinMax : " + str(listeScore.count(-1)) + "\n")
        fichier.write("Nombre de victoire de MCTS : " + str(listeScore.count(1)) + "\n")
        moy = sum(listeScore) / len(listeScore)