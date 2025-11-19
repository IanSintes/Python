def filtrar_paraules(llista_paraules, x):
    resultat = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat

# Exemples de prova
print(filtrar_paraules(["Hola", "Ramis", "IES", "Paraula"], 4))
print(filtrar_paraules(["Python", "es", "genial", "IA"], 2))
print(filtrar_paraules(["a", "ab", "abc", "abcd"], 2))
print(filtrar_paraules([], 3))
