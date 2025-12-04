num = int(input("Introdueix un número: "))

suma = 0
n = num

while n > 0:
    suma += n % 10
    n = n // 10

print("La suma dels dígits és:", suma)

if suma % 2 == 0:
    print("La suma és parell")
else:
    print("La suma és senar")