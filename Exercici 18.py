def es_vocal(car):
    return car.lower() in 'aeiou'

# Exemples de prova
print("es_vocal('a') =", es_vocal('a'))
print("es_vocal('E') =", es_vocal('E'))
print("es_vocal('b') =", es_vocal('b'))
print("es_vocal('O') =", es_vocal('O'))
print("es_vocal('z') =", es_vocal('z'))

#Programa fet amb en joan
def ex18(c):
    v = "aeiouAEIOUàáèéìíòóùúÀÁÈÉÌÍÒÓÙÚ"
    if c in v:
        return True
    else:
        return False
c= input("Escriu un caracter per a provar si es vocal o no")