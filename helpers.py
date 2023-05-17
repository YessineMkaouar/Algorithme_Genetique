def run_command(command):
    import subprocess
    try:
        subprocess.run(command, shell=True, check=True)  # Exécute la commande spécifiée dans un sous-processus
    except subprocess.CalledProcessError as e:
        print(f"Échec de l'exécution de la commande avec le code d'erreur {e.returncode} : {e.output}")

def run_genetic_algorithm():
    import subprocess
    command = "gcc -o program_for_interface main_for_interface.c utils.c"
    run_command(command)  # Exécute la commande pour compiler le programme principal
    output = subprocess.check_output(["./program_for_interface"])  # Lit la sortie du programme principal
    best = output.decode('utf-8').split()  # Convertit la sortie en liste
    return best

def create_file(L: list, nbr_population: int, nbr_iteration: int):
    with open("test0.txt", "w") as f:
        f.write(str(nbr_population) + "\n")  # Écrit le nombre de populations dans le fichier
        f.write(str(nbr_iteration) + "\n")  # Écrit le nombre d'itérations dans le fichier
        f.write(str(len(L)) + "\n")  # Écrit la taille de la liste dans le fichier
        f.write(" ".join(map(str, L)))  # Écrit les éléments de la liste séparés par des espaces dans le fichier


def generate_sequence(L):
    res = ''.join(L)
    res = res.replace('--', '+')  # remplace les '--' par des '+'
    res = res.replace('+-', '-')  # remplace les '+-' par des '-'
    if res.startswith('+'):  # vérifie si la chaîne commence par '+'
        res = res[1:]  # supprime le premier caractère s'il est '+'
    return res

def calculate_sum(L):
    # Initialiser le signe courant et la somme courante
    signe = '+'
    somme = 0
    
    # Itérer à travers la liste
    for item in L:
        # Vérifier si l'élément est un signe
        if item in ('+', '-'):
            # Mettre à jour le signe courant
            signe = item
        else:
            # Convertir l'élément en nombre entier
            nombre = int(item)
            # Ajouter ou soustraire de la somme courante en fonction du signe courant
            if signe == '+':
                somme += nombre
            else:
                somme -= nombre
    
    # Renvoyer la somme finale
    return somme