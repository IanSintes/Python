def comptar_vocals(paraula):
    vocals = "aeiou"
    conte = {v: 0 for v in vocals}
    for car in paraula.lower():
        if car in vocals:
            conte[car] += 1
    return conte

# Prova
paraula = "Ratapinyada"
resultat = comptar_vocals(paraula)

for v in "aeiou":
    print(f"{v}: {resultat[v]}")
