def run_genetic_algorithm():
    import subprocess
    output = subprocess.check_output(["./program_for_interface"]) #Lire l'output du main_interface
    best = output.decode('utf-8').split() #Convertir l'output en liste
    return best

def create_file(L: list, nbr_population: int, nbr_iteration: int):
    with open("test0.txt", "w") as f:
        f.write(str(nbr_population) + "\n")
        f.write(str(nbr_iteration) + "\n")
        f.write(str(len(L)) + "\n")
        f.write(" ".join(map(str, L)))