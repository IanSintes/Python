# app2_fitxers.py

def treball_fitxers():
    print("\n--- APLICACIÓ 2: Agenda guardada en un fitxer ---")
    fitxer = "agenda.txt"

    while True:
        print("\n1. Afegir contacte")
        print("2. Mostrar agenda")
        print("3. Esborrar agenda")
        print("4. Tornar al menú principal")

        op = input("Escull una opció: ")

        if op == "1":
            nom = input("Nom: ")
            telefon = input("Telèfon: ")
            with open(fitxer, "a") as f:
                f.write(f"{nom} - {telefon}\n")
            print("Contacte afegit!")

        elif op == "2":
            try:
                with open(fitxer, "r") as f:
                    print("\n--- AGENDA ---")
                    print(f.read())
            except FileNotFoundError:
                print("L'agenda està buida.")

        elif op == "3":
            open(fitxer, "w").close()
            print("Agenda esborrada.")

        elif op == "4":
            break

        else:
            print("Opció no vàlida")

