def menu_principal():
        opcio=0
        while opcio<1 or opcio>3:  
            opcio = int(input("""Elegeixi una opció:
                               1. Calculadora decimal
                               2. Calculadora real (floats)
                               3. Sortir \n"""))
        if opcio>0 and opcio<4:
            return opcio
        else:
            print("L'opcio tornada no es correcte, torna a probar! \n")

def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio = int(input("""Escriu una opció:
                    1. Suma
                    2. Resta
                    3. Multiplicació
                    4. Divisió
                    5. Sortir
                    """))
    if opcio>0 and opcio<6:
        return opcio
    else:
        print("L'opcio tornada no es correcte, torna a probar!")

def calculadora_decimal(opcio):
    if opcio>0 and opcio<6:
        A = int(input("Insereix el primer nombre: "))
        B = int(input("Insereix el segon nombre: "))
    match(opcio):
        case 1:
            print("Estic fent la suma! \n")
            C = A + B
            print("La suma de {} + {} és {}".format(A, B, C))
        case 2:
            print("Estic fent la resta! \n")
            C = A - B
            print("La resta de {} - {} és {}".format(A, B, C))
        case 3:
            print("Estic fent la multiplicaicó! \n")
            C = A * B
            print("La multiplicació de {} * {} és {}".format(A, B, C))
        case 4:
            print("Estic fent la divisó! \n")
            C = A // B
            print("La divisió de {} / {} és {}".format(A, B, C))
        case _:
            print("Gracies, fins dema!")

def calculadora_real(opcio):
     if opcio>0 and opcio<6:
        A = float(input("Insereix el primer nombre: "))
        B = float(input("Insereix el segon nombre: "))
     match(opcio):
        case 1:
            print("Estic fent la suma! \n")
            C = A + B
            print("La suma de {} + {} és {}".format(A, B, C))
        case 2:
            print("Estic fent la resta! \n")
            C = A - B
            print("La resta de {} - {} és {}".format(A, B, C))
        case 3:
            print("Estic fent la multiplicaicó! \n")
            C = A * B
            print("La multiplicació de {} * {} és {}".format(A, B, C))
        case 4:
            print("Estic fent la divisó! \n")
            C = A / B
            print("La divisió de {} / {} és {}".format(A, B, C))
        case _:
            print("Gracies, fins dema!")

def conversio_bases():
    print("""
        Conversió de bases
        1. Binari → Decimal
        2. Decimal → Binari
        3. Hexadecimal → Decimal
        4. Decimal → Hexadecimal
        5. Octal → Decimal
        6. Decimal → Octal
        7. Sortir
    """)

    op = int(input("Esculli una opció: "))

    if op == 1:
        num = input("Introdueix un binari: ")
        print(int(num, 2))

    elif op == 2:
        num = int(input("Introdueix un decimal: "))
        print(bin(num))

    elif op == 3:
        num = input("Introdueix un hexadecimal: ")
        print(int(num, 16))

    elif op == 4:
        num = int(input("Introdueix un decimal: "))
        print(hex(num))

    elif op == 5:
        num = input("Introdueix un octal: ")
        print(int(num, 8))

    elif op == 6:
        num = int(input("Introdueix un decimal: "))
        print(oct(num))

    elif op == 7:
        print("Sortint del menú de bases...")

    else:
        print("Opció no vàlida.")


def menu_principal_extens():
    print("""
       1. Calculadora decimal
       2. Calculadora real (floats)
       3. Conversió de bases
       4. Sortir
    """)

    op = int(input("Esculli una opció: "))
    return op


#  Programa Principal

op = 1
while op != 0:

    op = menu_principal_extens()

    if op == 1:
        print("Estic passsant per calculadora decimal \n")
        calculadora_decimal(menu_calculadora())

    elif op == 2:
        print("Estic passsant per calculadora real \n")
        calculadora_real(menu_calculadora())

    elif op == 3:
        conversio_bases()

    elif op == 4:
        print("Gracies per utilitzar la meva calculadora!")
        op = 0

    else:
        print("Opció no vàlida, torna-ho a intentar.")