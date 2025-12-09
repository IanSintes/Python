def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            contingut = f.read()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
    except IOError:
        print(f"Error: No s'ha pogut llegir el fitxer '{nom_fitxer}'.")

# Proves
nom = "exemple.txt"
resultat = llegir_fitxer(nom)
if resultat:
    print("Contingut del fitxer:")
    print(resultat)