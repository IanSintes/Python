def crear_llista_fitxer(nom_fitxer):
    llista = []
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            for linia in f:
                paraules = linia.split()
                llista.extend(paraules)
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer: {nom_fitxer}")
    return llista

nom_fitxer = "exemple.txt"
llista_paraules = crear_llista_fitxer(nom_fitxer)
print("Paraules llegides del fitxer:", llista_paraules)