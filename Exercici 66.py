def coincidencia_valor_index(llista):
    comptador = 0
    for index, valor in enumerate(llista):
        if index == valor:
            comptador += 1
    return comptador

# Proves
print(coincidencia_valor_index([0, 2, 3, 3, 4]))
print(coincidencia_valor_index([0, 1, 2, 3]))
print(coincidencia_valor_index([1, 2, 3]))