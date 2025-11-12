A = float(input("Escriure el primer nombre: "))
B = float(input("Escriure el segon nombre: "))
C = float(input("Escriure el tercer nombre: "))
D = A + B + C
print("El resultat del a suma {} + {} + {} és {}".format(A,B,C,D))
if D>20:
    print("La suma es major de 20, que és {}".format(D))
else:
    print("La suma es menor de 20, que és {}".format(D))

D = A * B * C
print("El resultat de la multiplicacio {} * {} * {} és {}".format(A,B,C,D))
if D>100:
    print("La multiplicaó es major de 100, que és {}".format(D))
else:
    print("La multiplicaó es menor de 100, que és {}".format(D))