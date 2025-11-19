def comptar_majuscules(cadena):
    comptador = 0
    for car in cadena:
        if car.isupper():
            comptador += 1
    return comptador

# Exemples de prova
print(comptar_majuscules("Hola Mon"))
print(comptar_majuscules("Python ES GENIAL"))
print(comptar_majuscules("aBCdEfG"))
print(comptar_majuscules("senseMajuscules"))
print(comptar_majuscules(""))
