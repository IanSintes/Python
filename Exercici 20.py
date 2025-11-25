def invertir(cadena):
    return cadena[::-1]

# Exemples de prova
print(invertir("Soc del Ramis"))
print(invertir("Hola món"))
print(invertir("Python"))
print(invertir(""))

cadena= "Soc del ramis"
print("La inversa de la cadena {} es {}".format(cadena, invertir(cadena)))