#include <stdio.h>
#include <stdlib.h>
#include "utils.h"
#include "time.h"

int *t; // Les éléments de l'ensemble
int n;  // Nombre d'individus dans la génération
int l; // Taille de l'ensemble

Individu *gen; // Pointeur vers le premier élément de la liste chaînée de la génération
Individu *best; // Pour stocker le meilleur individu parmi toutes les générations et individus
int bestScore = 1000000000; // Pour stocker la meilleure valeur de fitness
int num_iteration; // Nombre d'itérations

int main()
{
    /********________________________Lecture des entiers relatifs à partir d'un fichier____________________________********/
    FILE *f; // Pointeur pour le fichier
    f = fopen("test0.txt", "r"); // Lire le fichier où l'ensemble est stocké
    
    fscanf(f, "%d", &n); // Lire la taille de la population dans chaque génération
    fscanf(f, "%d", &num_iteration); // Lire le nombre d'itérations
    fscanf(f, "%d", &l); // Lire la taille de l'ensemble
    t = malloc(l * sizeof(int)); // Initialiser le tableau pour stocker l'ensemble
    for (int i = 0; i < l; i++) {
        fscanf(f, "%d", t + i); // Lire les valeurs de l'ensemble
    }
    fclose(f); // Fermer le fichier

    /********___________________________________Initialisation__________________________________********/
    gen = getInitialGeneration(n, t, l); // Générer la génération initiale
    best = getCopy(gen, l); // Obtenir le meilleur élément et le stocker
    bestScore = best->value; // Mettre à jour le meilleur score

    for (int i = 0; i < num_iteration; i++) {
        /********___________________________________Sélection/Reproduction__________________________________********/
        gen = addChildGen(gen, n, l, t); // Générer et ajouter la génération enfant
        gen = GetBestElements(gen, n); // Obtenir les n meilleurs éléments de la dernière population
        if (cmp(gen, best)) { // Si le nouvel élément meilleur est meilleur que le dernier meilleur, on le met à jour
            bestScore = gen->value; // Mettre à jour le meilleur score
            best = getCopy(gen, l); // Mettre à jour le meilleur individu
        }
    }

    /********___________________________________Affichage__________________________________********/
    printIndivForInterface(best, t, l); // Afficher l'individu
    return 0;
}

