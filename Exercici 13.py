opcio = float(input("""Escriu una opció:
                    1. Suma
                    2. Resta
                    3. Multiplicació
                    4. Divisió
                    5. Resto
                    6. Quocient
                    7.Potencia
                    0. Sortir
                    """))
A = float(input("Insereix el primer nombre: "))
B = float(input("Insereix el segon nombre: "))

if opcio==1:
    print("La suma de {} + {} és {}".format(A, B, A+B))
elif opcio==2:
    print("La resta de {} - {} és {}".format(A, B, A-B))
elif opcio==3:
    print("La multiplicació de {} * {} és {}".format(A, B, A*B))
elif opcio==4:
    print("La divisió de {} / {} és {}".format(A, B, A/B))
elif opcio==5:
    print("El resto de {} % {} és {}".format(A, B, A%B))
elif opcio==6:
    print("La quocient de {} // {} és {}".format(A, B, A//B))
elif opcio==7:
    print("La potencia de {} ** {} és {}".format(A, B, A**B))