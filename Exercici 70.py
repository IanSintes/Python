def dividir(a, b):
    if b == 0:
        print("Error: No es pot dividir per zero!")
        return None
    return a / b

# Proves
print(dividir(10, 2))
print(dividir(7, 0))
print(dividir(8, 4))
