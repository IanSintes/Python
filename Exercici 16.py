def gran_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Exemples de prova de la funció gran_de_tres():")
print("gran_de_tres(5, 3, 7) =", gran_de_tres(5, 3, 7))
print("gran_de_tres(10, 20, 15) =", gran_de_tres(10, 20, 15))
print("gran_de_tres(-4, -9, -2) =", gran_de_tres(-4, -9, -2))
print("gran_de_tres(7.5, 7.5, 7.2) =", gran_de_tres(7.5, 7.5, 7.2))