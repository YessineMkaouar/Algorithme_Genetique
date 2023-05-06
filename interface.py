import streamlit as st
from helpers import run_genetic_algorithm,create_file,generate_sequence,calculate_sum

st.write("""
# Interface Graphique IN104

Veuillez entrer un ensemble de la forme : nbr1 nbr2 nbr3 ...

""")
user_input = st.text_input("Veuillez entrer votre message :")
submit_button = st.button("Envoyer")


def generate_response(user_input):

    L = user_input.split()
    L = [int(x) for x in L]
    create_file(L = L,nbr_population = len(L), nbr_iteration = 300)
    response = run_genetic_algorithm()
    return response

if submit_button:
    response = generate_response(user_input)
    solution = generate_sequence(response)
    fitness = calculate_sum(response)
    st.write("La solution est ")
    st.write(" ".join(solution))
    st.write("fitness = {}".format(fitness))