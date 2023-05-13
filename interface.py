import streamlit as st
from helpers import run_genetic_algorithm,create_file,generate_sequence,calculate_sum
nb_pop=125
nb_iter=200
st.write("""
# Interface Graphique - Algorithmes Génétiques
## Projet IN104
### Problème de la somme des sous-ensembles


""")
with st.sidebar:
    nb_pop_input = st.text_input("Veuillez entrer la taille de la population :")
    nb_pop_submit_button = st.button(label = "Entrer la taille de la population")
    if nb_pop_submit_button:
        nb_pop = int(nb_pop_input)

    nb_iter_input = st.text_input("Veuillez entrer le nombre d'itérations :")
    nb_iter_submit_button = st.button(label = "Entrer le nombre d'itérations")
    if nb_iter_submit_button:
        nb_iter = int(nb_iter_input)

user_input = st.text_input("Veuillez entrer un ensemble sous la forme : nbr1 nbr2 nbr3 ... :")
submit_button = st.button("Envoyer")


def generate_response(user_input,nb_pop,nb_iter):

    L = user_input.split()
    L = [int(x) for x in L]
    create_file(L = L,nbr_population = nb_pop, nbr_iteration = nb_iter)
    response = run_genetic_algorithm()
    return response

if submit_button:
    response = generate_response(user_input,int(nb_pop_input),int(nb_iter_input))
    solution = generate_sequence(response)
    fitness = calculate_sum(response)
    st.write("La solution est : ")
    st.write(solution)
    st.write("Fitness = {}".format(fitness))

from PIL import Image

img = Image.open("logo_TA.jpg")
new_size = (500, 500)
img = img.resize(new_size)
st.image(img, caption="TA", use_column_width=True)
