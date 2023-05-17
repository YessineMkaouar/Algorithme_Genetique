#include <stdio.h>
#include <stdlib.h>
#include "utils.h"
#include "time.h"

int *t ; // Les éléments de l'ensemble
int n;  // Nombre d'individus dans la génération
int l; // Taille de l'ensemble

Individu *gen; // Pointeur vers le premier élément de la liste chaînée de la génération
Individu *best; // Pour stocker le meilleur individu sur l'ensemble des générations et individus
int bestScore = 1000000000; // Pour stocker la meilleure valeur de fitness
int num_iteration; // Nombre d'itérations

int main()
{
    srand(time(NULL));  // Initialisation du générateur de nombres aléatoires

    /********________________________Lecture des entiers relatifs à partir d'un fichier____________________________********/
    FILE *f; // Pointeur pour le fichier
    f = fopen("test0.txt", "r"); // Lire le fichier dans lequel l'ensemble est stocké
    printf("La taille de l'ensemble : ");
    fscanf(f, "%d", &l); // Lire la taille de l'ensemble
    t = malloc(l * sizeof(int)); // Initialiser le tableau pour stocker l'ensemble

    printf("%d\n", l);
    for (int i = 0; i < l; i++) {
        printf("La %d-ème élément de l'ensemble : ", i);
        fscanf(f, "%d", t + i); // Lire les valeurs de l'ensemble
        printf("%d\n", *(t + i));
    }
    fclose(f); // Fermer le fichier

    /********________________________Saisie des paramètres en entrée____________________________********/
    printf("Nombre d'individus par génération : ");
    scanf("%d", &n); // Lire la taille de la population dans chaque génération
    printf("Nombre d'itérations : ");
    scanf("%d", &num_iteration); // Lire le nombre d'itérations



  /********___________________________________Initialisation__________________________________********/
gen = getInitialGeneration(n, t, l); // Générer la génération initiale
best = getCopy(gen, l); // Obtenir le meilleur élément et le stocker
bestScore = best->value; // Mettre à jour le meilleur score
clock_t tic = clock(); // Début du calcul du temps d'exécution


for (int i = 0; i < num_iteration; i++) {
    /********___________________________________Sélection/Reproduction__________________________________********/
    gen = addChildGen(gen, n, l, t); // Générer et ajouter la génération d'enfants
    gen = GetBestElements(gen, n); // Obtenir les meilleurs n éléments de la dernière population
    if (cmp(gen, best)) { // Si le nouvel élément meilleur est meilleur que le précédent meilleur, nous le mettons à jour
        bestScore = gen->value; // Mettre à jour le meilleur score
        best = getCopy(gen, l); // Mettre à jour le meilleur individu
    }
}

/********___________________________________Affichage__________________________________********/
clock_t toc = clock(); // Fin du calcul du temps d'exécution
printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC); // Afficher le temps d'exécution
printf("bestScore = %d\n", bestScore); // Afficher le meilleur score
printIndiv(best, t, l); // Afficher l'individu
return 0;
}
