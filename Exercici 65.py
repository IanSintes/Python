def llista_a_diccionari(llista):
    return {valor: index for index, valor in enumerate(llista)}

# Prova
elements = ("casa", "cotxe", "cadira", "taula")
print(llista_a_diccionari(elements))