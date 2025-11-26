def nums_que_comencen_per(llista_noms, lletra):
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador

noms = []

print("Introdueix noms (enter per acabar):")
while True:
    nom = input()
    if nom == "":
        break
    noms.append(nom)

lletra = input("Introdueix una lletra: ")

resultat = nums_que_comencen_per(noms, lletra)

print("Noms que comencen per la lletra", lletra, ":", resultat)