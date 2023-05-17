import streamlit as st  # Importation de la bibliothèque Streamlit pour la création de l'interface utilisateur
import subprocess  # Importation de la bibliothèque subprocess
from helpers import run_genetic_algorithm, create_file, generate_sequence, calculate_sum  # Importation des fonctions auxiliaires

nb_pop = 125  # Nombre de populations par défaut
nb_iter = 200  # Nombre d'itérations par défaut

st.write("""
# Interface Graphique - Algorithmes Génétiques
## Projet IN104
### Problème de la somme des sous-ensembles
""")  # Affichage du titre et de la description de l'interface graphique

with st.sidebar:
    nb_pop_input = st.text_input("Veuillez entrer la taille de la population :")  # Champ de saisie pour la taille de la population
    nb_pop_submit_button = st.button(label="Entrer la taille de la population")  # Bouton de soumission pour la taille de la population
    if nb_pop_submit_button:
        nb_pop = int(nb_pop_input)  # Mise à jour de la taille de la population si le bouton est cliqué

    nb_iter_input = st.text_input("Veuillez entrer le nombre d'itérations :")  # Champ de saisie pour le nombre d'itérations
    nb_iter_submit_button = st.button(label="Entrer le nombre d'itérations")  # Bouton de soumission pour le nombre d'itérations
    if nb_iter_submit_button:
        nb_iter = int(nb_iter_input)  # Mise à jour du nombre d'itérations si le bouton est cliqué

    from PIL import Image  # Importation de la bibliothèque PIL pour le traitement d'images
    img = Image.open("logo_enit.png")  # Chargement de l'image
    new_size = (500, 500)
    img = img.resize(new_size)  # Redimensionnement de l'image
    st.image(img, caption="ENIT", use_column_width=True)  # Affichage de l'image

user_input = st.text_input("Veuillez entrer un ensemble sous la forme : nbr1 nbr2 nbr3 ... :")  # Champ de saisie pour l'ensemble
submit_button = st.button("Envoyer")  # Bouton de soumission

def generate_response(user_input, nb_pop, nb_iter):
    L = user_input.split()  # Conversion de la saisie utilisateur en liste d'entiers
    L = [int(x) for x in L]
    create_file(L=L, nbr_population=nb_pop, nbr_iteration=nb_iter)  # Création d'un fichier avec l'ensemble, la taille de la population et le nombre d'itérations
    response = run_genetic_algorithm()  # Exécution de l'algorithme génétique et récupération de la réponse
    return response

L1 = user_input.split()  # Séparation de la saisie utilisateur en liste d'éléments
compteur = 0
for element in L1:
    if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
        compteur += 1  # Comptage du nombre d'entiers dans la liste

compteur1 = 0
nombre_temporaire = ''


if submit_button:  # Si le bouton "Envoyer" est cliqué
    try:
        response = generate_response(user_input, int(nb_pop_input), int(nb_iter_input))  # Générer la réponse en utilisant la saisie utilisateur, la taille de population et le nombre d'itérations
        solution = generate_sequence(response)  # Générer la séquence à partir de la réponse
        fitness = calculate_sum(response)  # Calculer la somme de la réponse (fitness)
        st.write("La taille de l'ensemble de départ : ")
        st.write(compteur)  # Afficher la taille de l'ensemble initial
        st.write("La solution est : ")
        st.write(solution)  # Afficher la solution trouvée
        st.write("Résultat = {}".format(fitness))  # Afficher le résultat (fitness)

        for caractere in str(solution):
            if caractere.isdigit() or (caractere == '-' and nombre_temporaire == ''):
                nombre_temporaire += caractere  # Construire le nombre temporaire caractère par caractère
            elif nombre_temporaire:
                compteur1 += 1  # Comptage du nombre d'entiers dans la séquence
                nombre_temporaire = ''

        # Vérification pour le dernier nombre dans la chaîne
        if nombre_temporaire:
            compteur1 += 1

        st.write("Taille de l'ensemble trouvé : ")
        st.write(compteur1)  # Afficher la taille de l'ensemble trouvé
    except subprocess.CalledProcessError as e:
        st.write("Veuillez changer la taille de la population ou bien le nombre d'itérations.")  # Afficher un message d'erreur en cas d'erreur lors de l'exécution de l'algorithme génétique

img = Image.open("cover_enit.jpg")  # Chargement de l'image

st.image(img, caption="ENIT", use_column_width=True)  # Afficher l'image avec une légende

      

