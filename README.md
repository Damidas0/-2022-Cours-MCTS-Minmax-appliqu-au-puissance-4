<h1>Intelligence artificielle appliquée au puissance 4</h1>
<p>Ce projet de cours a pour but de mettre en place l'algorithme MinMax ainsi que le MCTS dans le jeu puissance 4</p>
<p>Il a une fonctionnalité d'analyse des résultats avec la mesure des temps des différents algorithmes selon les paramètres choisis dans un fichier Excel </p> 
<h2>Prérequis : </h2>
<p>Il faut installer la librairie Openpyxl pour la sauvegarde et l'analyse des résultats (ce qui peut se faire avec la commande "pip install openpyxl") </p> 
<h2>Démarrage : </h2>
<p>Le programme se lance depuis le fichier "interface.py", il faut alors choisir si l'on veut affronter l'ordinateur avec MinMax ou MCTS ou faire s'affronter MinMax et MCTS.  <P>
<p> Dans le cas d'une partie entre les deux intelligence artificielle, il y a en sortie deux fichiers : <br>
Un fichier txt (appelé result_[profondeur_minmax]_[nombre_iteration].txt ) qui détaille le résultat des "match"  <br>
Dans le fichier "temps.xlsx" une feuille nommée [nombre_iteration]_[profondeur_minmax]_[Constante_MCTS] avec le temps moyen des coups, le nombre de partie et le nombre de victoire  
</p>
<h2>Auteurs : </h2>
<p>BRAND Rémi, BRUN Luc, CARRIER Nicolas, LAQUEUVRE Damien</p>