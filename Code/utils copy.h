#include <stdbool.h>
#ifndef UTILS_H_INCLUDED
#define UTILS_H_INCLUDED

typedef struct _individu{
    int * DNA; // Tableau dynamique d'entiers représentant le chromosome.
    int value; // Valeur d'adaptation "fitness value"
    int nb; // Taille du sous-ensemble extrait de l'individu. "Nbre d'élts "on" de l'ensemble"
    struct _individu * next; // Elément suivant de la liste chaînée
}Individu;

Individu * getNewIndividu(int l, int *t);

Individu * getCopy(Individu * indiv, int l);

Individu * getElementByIndex (Individu* gen , int idx);

Individu * GetBestElements(Individu * gen, int k);

Individu * inser(Individu * get, Individu * indiv, int l);

Individu * getInitialGeneration( int n, int* t, int l);

Individu * addChildGen(Individu * gen , int n , int l, int *t);

void mutation(Individu * indiv, int l);

void croisement(Individu * father, Individu * mother , int *t, int l );

int fitness(Individu * ind, int l, int t[]);

int fit_nb(Individu* indiv, int l);

int cmp(Individu *  indiv1 , Individu * indiv2);

int eq(Individu *  indiv1 , Individu * indiv2,int l);

int checkIndiv(Individu * indiv, int l);

void printIndiv(Individu * indiv, int *t, int l);

void printIndivForInterface(Individu * indiv, int *t, int l);

#endif // UTILS_H_INCLUDED
