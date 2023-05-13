def run_command(command):
    import subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error code {e.returncode}: {e.output}")


def run_genetic_algorithm():
    import subprocess
    command = "gcc -o program_for_interface main_for_interface.c utils.c"
    run_command(command)
    output = subprocess.check_output(["./program_for_interface"]) #Lire l'output du main_interface
    best = output.decode('utf-8').split() #Convertir l'output en liste
    return best

def create_file(L: list, nbr_population: int, nbr_iteration: int):
    with open("test0.txt", "w") as f:
        f.write(str(nbr_population) + "\n")
        f.write(str(nbr_iteration) + "\n")
        f.write(str(len(L)) + "\n")
        f.write(" ".join(map(str, L)))

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