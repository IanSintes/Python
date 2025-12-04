n = int(input("Introdueix un nombre menor de 100: "))

suma = 0
i = n - 4

while i >= 0:
    suma += i ** 2
    i -= 4

print("La suma és:", suma)