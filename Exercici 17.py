def longitud(obj):
    comptador = 0
    for _ in obj:
        comptador += 1
    return comptador

# Exemples de prova
print("longitud([1, 2, 3, 4]) =", longitud([1, 2, 3, 4]))
print("longitud('Hola món') =", longitud('Hola món'))
print("longitud([]) =", longitud([]))
print("longitud('') =", longitud(''))
print("longitud([10, 20, 30]) =", longitud([10, 20, 30]))