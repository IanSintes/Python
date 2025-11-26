def nums_que_comencen_per(llista_noms):
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith('a'):
            comptador += 1
    return comptador

# Prova
noms = ["Anna", "Pere", "Albert", "maria", "Andreu", "Joan"]

resultat = nums_que_comencen_per(noms)

print("Noms que comencen per la lletra A:", resultat)
