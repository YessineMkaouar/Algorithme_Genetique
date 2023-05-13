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
    
    /********________________________Lecture des entiers relatifs � partir d'un fichier____________________________********/
    FILE * f; //  pointer for the file
    f=fopen("test0.txt","r"); //  read the file where the set is stored in
    
    fscanf(f,"%d",&n); //  read the size of the population in each generation
    fscanf(f,"%d",&num_iteration); //  read the number of iterations
    fscanf(f,"%d",&l); //  read the size of the set
    t = malloc(l*sizeof(int)); // initialize the array to store the set
    for(int i=0;i<l;i++){
        fscanf(f,"%d",t+i); // read the set values
    }
    fclose(f); //  close the file

   /********___________________________________Initialisation__________________________________********/
    gen = getInitialGeneration(n,t,l); //  generate the initial generation
    best = getCopy(gen,l); // get the best element and store it
    bestScore = best->value; // update the best score
    

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
    
    printIndivForInterface(best,t,l);    // show the individual
    return 0;
}
