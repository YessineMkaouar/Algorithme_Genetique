# Problème de la somme des sous-ensembles

Ce problème consiste à trouver le nombre maximum d'éléments dans un ensemble dont la somme est égale à 0 après avoir multiplié chaque élément par -1 ou 1. La résolution de ce problème se fait en utilisant une structure de données de liste chaînée.

## Instructions d'exécution

### main.c

1. Assurez-vous d'avoir un fichier `test0.txt` contenant la taille de l'ensemble et ses éléments.
2. Assurez-vous d'avoir les fichiers utils.c et utils.h dans le meme dossier.
3. Compilez et exécutez le fichier `main.c` pour résoudre le problème.
Exemple de contenu du fichier `test0.txt` :
5
1 2 3 4 5


### main_for_interface.c

1. Assurez-vous d'avoir un fichier `test0.txt` avec le contenu suivant :
   - Première ligne : nombre de populations
   - Deuxième ligne : nombre d'itérations
   - Troisième ligne : taille de l'ensemble de départ
   - Quatrième ligne : éléments de l'ensemble de départ

Exemple de contenu du fichier `test0.txt` :
125
200
4
-2 1 -3 4


### Interface graphique

1. Assurez-vous d'avoir Python et le module Streamlit installés sur votre système.
2. Compilez le fichier `interface.py` en exécutant la commande suivante dans le terminal :

streamlit run interface.py

3. Accédez à l'interface graphique en ouvrant un navigateur web et en accédant à l'URL indiquée après avoir exécuté la commande ci-dessus.
