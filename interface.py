import streamlit as st
from helpers import run_genetic_algorithm,create_file,generate_sequence,calculate_sum
nb_pop=0
nb_iter=0
st.write("""
# Interface Graphique - Algorithmes Génétiques
## Projet IN104
### Problème de la somme des sous-ensembles


""")
nb_pop_input = st.text_input("Veuillez entrer la taille de la population :")
nb_pop_submit_button = st.button("Entrer")
if nb_pop_submit_button:
    nb_pop = int(nb_pop_input)

nb_iter_input = st.text_input("Veuillez entrer le nombre d'itérations :")
nb_iter_submit_button = st.button("Send")
if nb_iter_submit_button:
    nb_iter = int(nb_iter_input)

user_input = st.text_input("Veuillez entrer un ensemble sous la forme : nbr1 nbr2 nbr3 ... :")
submit_button = st.button("Envoyer")


def generate_response(user_input):

    L = user_input.split()
    L = [int(x) for x in L]
    create_file(L = L,nbr_population = nb_pop, nbr_iteration = nb_iter)
    response = run_genetic_algorithm()
    return response

if submit_button:
    response = generate_response(user_input)
    solution = generate_sequence(response)
    fitness = calculate_sum(response)
    st.write("La solution est : ")
    st.write(" ".join(solution))
    st.write("Fitness = {}".format(fitness))

from PIL import Image

img = Image.open("logo_TA.jpg")
new_size = (500, 500)
img = img.resize(new_size)
st.image(img, caption="TA", use_column_width=True)
