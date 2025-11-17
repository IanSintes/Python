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
            #Suma 
            print("Estic fent la suma! \n")
            C = A + B
            print("La suma de {} + {} és {}".format(A, B, C))
        case 2:      
            #Resta 
            print("Estic fent la resta! \n")
            C = A - B
            print("La resta de {} - {} és {}".format(A, B, C))
        case 3: 
             #Multiplicacó 
             print("Estic fent la multiplicaicó! \n")
             C = A * B
             print("La multiplicació de {} * {} és {}".format(A, B, C))
        case 4: 
             #Divisió
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
            #Suma 
            print("Estic fent la suma! \n")
            C = A + B
            print("La suma de {} + {} és {}".format(A, B, C))
        case 2:      
            #Resta 
            print("Estic fent la resta! \n")
            C = A - B
            print("La resta de {} - {} és {}".format(A, B, C))
        case 3: 
             #Multiplicacó 
             print("Estic fent la multiplicaicó! \n")
             C = A * B
             print("La multiplicació de {} * {} és {}".format(A, B, C))
        case 4: 
             #Divisió
             print("Estic fent la divisó! \n")
             C = A / B
             print("La divisió de {} / {} és {}".format(A, B, C))
        case _:
             print("Gracies, fins dema!")

#Programa principal

op = 1
while op!=0:
    op = menu_principal()
    if op==1:
        #Calculadora decimal
        print("Estic passsant per calculadora decimal \n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        #Calculadora real
        print("Estic passsant per calculadora real \n")
        calculadora_real(menu_calculadora())
    else:
        print("Gracies per utilitzar la meva calculadora, fins un altre dia!")
        op=0