while True:
    num = int(input("Introdueix un número (1 - 20): "))
    if 1 <= num <= 20:
        break
    print("Número fora de rang.")

print(f"Taula de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")