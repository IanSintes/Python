def paraula_mes_llarga(llista_paraules):
    if not llista_paraules:
        return None
    mes_llarga = llista_paraules[0]
    for paraula in llista_paraules[1:]:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

# Exemples de prova
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))
print(paraula_mes_llarga(["Python", "es", "genial"]))
print(paraula_mes_llarga(["a", "ab", "abc", "abcd"]))
print(paraula_mes_llarga([]))
