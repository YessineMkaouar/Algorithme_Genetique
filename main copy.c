#include <stdio.h>
#include <stdlib.h>
#include "utils.h"
#include "time.h"

int *t ; //  the elements of the set
int n;  // number of units in the generation
int l; //  the size of the set

Individu * gen; //  pointer to the first element in the linked list of the generation
Individu * best; //  to store the best individual over all generations and individuals
int bestScore=1000000000; //  to store the best fitness value
int num_iteration; //  number of iterations



int main()
{
    srand(time(NULL));

    /********______Lecture des entiers relatifs à partir d'un fichier______********/

    FILE * f; // Pointeur pour le fichier
    f=fopen("test0.txt","r"); //  Lire le fichier dans lequel l'ensemble est stocké
    fscanf(f,"%d",&l); //  Lire la taille de l'ensemble
    t = malloc(l*sizeof(int)); // Initialiser le tableau pour stocker l'ensemble

    for(int i=0;i<l;i++){
        fscanf(f,"%d",t+i); // Lire et stocker le i ème élément de l'ensemble
    }
    fclose(f); // Fermer le fichier


    /*******______Saisie des paramétres en entrée_________********/

    printf("Nombre d'individu par génération  : "); 
    scanf("%d",&n); //Lire la taille de la population des générations
    printf("Nombre d'itération  : ");
    scanf("%d",&num_iteration); // Lire le nombre d'itérations 


   /********_________________Initialisation________________*******/

    gen = getInitialGeneration(n,t,l); // Générer la génération initiale
    best = getCopy(gen,l); // Obtenir le meilleur élément et le stocker
    bestScore = best->value; // Mettre à jour le meilleur score
    clock_t tic = clock(); // Démarrer le chronomètre de calcul


    for(int i=0;i<num_iteration;i++)
        {
        /********___________________________________Sélection/Reproduction__________________________________********/
        gen = addChildGen(gen,n,l,t); // generate and add the child generation
        gen = GetBestElements(gen,n); // get the best n element from the last population
        if(cmp(gen,best)){ //  if the new best element is better than the last best we update it
            bestScore = gen->value; // update the best score
            best= getCopy(gen,l);   // update best individual
        }
       }



    /********___________________________________Affichage__________________________________********/
    clock_t toc = clock(); //  end time of computation
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC); // print the execution time
    printf("bestScore = %d\n",bestScore); //  print the best score
    printIndiv(best,t,l);    // show the individual
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int *DNA;
} Individu;

int fitness(Individu * ind , int l , int*t){
    // fonction pour calculer la valeur de forme physique d'un individu
    int sum=0;
    for(int i=0;i<l;i++){
        sum+=(ind->DNA[i]-1)*t[i];
    }
    return abs(sum);
}
int main() {
    // créer un tableau d'ADN d'exemple
    int DNA_array[] = {2, 1, 1, 0, 0};
    int l = sizeof(DNA_array) / sizeof(int);
    // créer un objet Individu avec le tableau d'ADN
    Individu * indiv = (Individu *) malloc(sizeof(Individu));
    indiv->DNA = DNA_array;
    // créer un tableau de poids d'exemple
    int weight_array[] = {5, 3, 2, 4, 1};
    // appeler la fonction fitness pour calculer la valeur de forme physique de l'individu
    int result = fitness(indiv, l, weight_array);
    // afficher le résultat
    printf("La valeur de forme physique de l'individu est: %d\n", result);
    // libérer la mémoire allouée pour l'objet Individu
    free(indiv);
    return 0;
}



