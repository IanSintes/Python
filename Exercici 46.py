num = int(input("Introdueix un número: "))

print("Dígits parells:")
for digit in str(num):
    if int(digit) % 2 == 0:
        print(digit, end=" ")
print()