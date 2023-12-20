# Projet_BJ
Black Jack

Le jeu de black est ici présent est des plus basiques.

Pour pouvoir lancer le jeu vous devez préalablement installer PIP sur visualStudio.


Règles:
Vous pouvez jouer entre 1 et 4 joueurs en plus du croupier qui joue indépendament des autres joueurs.
L'objectif est d'obtenir un score se rapprochant le plus possible de 21 sans pour autant le dépasser tout en ayant un nombre supérieur à celui du croupier.



Fonctionnement:
Les valeurs des cartes on été généré dans une liste et sont appellés dans une autre de manière aléatoire pour chaque joueur.
Les valeurs ont bien été respecter, surtout pour l'AS, il s'adapte automatiquement pour que sa valeur soit de 1 ou de 11 selon le jeu du joueur.
Le calcul des cartes se fait automatiquement et est directement affiché sur l'écran.
Les cartes se tirent joueur par joueur, tant que les joueurs demande de nouvelle carte il continue de piocher jusqu'à ce que l'on clique sur "non"


Blackjack en Python
Description
Ce projet est une implémentation du jeu classique de Blackjack conçu pour être joué en local sur un ordinateur. Le jeu est écrit en Python et utilise la bibliothèque Pygame pour l'interface graphique.

'Fonctionnalités'
Jeu de Blackjack multijoueur en local
Interaction avec l'utilisateur via une interface graphique
Gestion des tours de jeu pour plusieurs joueurs
Affichage des scores et des résultats en temps réel

Dépendances
Pour exécuter ce jeu, vous aurez besoin de Python et de Pygame installés sur votre machine.
Python (3.x recommandé)
Pygame

Installation
Pour installer Pygame, exécutez la commande suivante dans votre terminal:
pip install pygame


Utilisation
Pour démarrer le jeu, exécutez le fichier main.py avec Python depuis votre terminal:
python main.py


Contrôles du jeu
Utilisez la souris pour interagir avec les boutons à l'écran.
Cliquez sur "Tirer" pour obtenir une nouvelle carte.
Cliquez sur "Rester" pour terminer votre tour.
