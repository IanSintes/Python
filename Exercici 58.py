def elements_parells(llista):
    return [llista[i] for i in range(len(llista)) if i % 2 == 0]

paraules = ["Hola", "Paco", "Ian", "Maria", "Izan", "Lucas"]
print(elements_parells(paraules))