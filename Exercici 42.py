while True:
    num = int(input("Introdueix un número (1 - 900000): "))
    if 1 <= num <= 900000:
        break
    print("Número fora de rang.")

comptador = 0
n = num

while n > 0:
    n = n // 10
    comptador += 1

print("El número té", comptador, "dígits.")