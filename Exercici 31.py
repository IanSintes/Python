any_actual = int(input("Introdueix l'any actual: "))

noms = []
anys_naixement = []
edats = []

for i in range(4):
    nom = input("Nom de la persona: ")
    any_naix = int(input("Any de naixement: "))
    
    noms.append(nom)
    anys_naixement.append(any_naix)
    edats.append(any_actual - any_naix)

print("\nNom\t\tData naixement\tAnys que farà aquest any")

for i in range(4):
    print(noms[i], "\t\t", anys_naixement[i], "\t\t", edats[i])
