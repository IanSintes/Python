import random

def generar_llista_aleatoria(n, a=0, b=100):
    return [random.randint(a, b) for _ in range(n)]

def treball_llistes():
    while True:
        print("\n--- App1: Llistes i números aleatoris ---")
        print("1: Generar llista aleatòria")
        print("2: Mostrar suma, mitjana, min, max")
        print("3: Ordenar asc/desc")
        print("4: Comptar duplicats")
        print("5: Tornar al menú principal")
        op = input("Opció: ").strip()
        if op == "1":
            n = int(input("Quants elements? "))
            a = int(input("Valor mínim? "))
            b = int(input("Valor màxim? "))
            llista = generar_llista_aleatoria(n, a, b)
            print("Llista generada:", llista)
        elif op == "2":
            try:
                print("Suma:", sum(llista))
                print("Mitjana:", sum(llista)/len(llista))
                print("Min:", min(llista))
                print("Max:", max(llista))
            except Exception:
                print("No hi ha cap llista generada. Genera una llista primer (opció 1).")
        elif op == "3":
            try:
                ordre = input("asc o desc? ").strip().lower()
                if ordre == "asc":
                    print(sorted(llista))
                else:
                    print(sorted(llista, reverse=True))
            except Exception:
                print("Genera una llista primer (opció 1).")
        elif op == "4":
            try:
                vistos = set()
                dup = False
                for x in llista:
                    if x in vistos:
                        dup = True
                        break
                    vistos.add(x)
                print("Hi ha duplicats?" , dup)
            except Exception:
                print("Genera una llista primer (opció 1).")
        elif op == "5":
            break
        else:
            print("Opció no vàlida.")

