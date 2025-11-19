def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False

# Exemples de prova
print(superposicio([1, 2, 3], [3, 4, 5]))
print(superposicio([10, 20, 30], [40, 50]))
print(superposicio(['a', 'b'], ['c', 'b']))
print(superposicio([], [1, 2]))
print(superposicio([1, 2], []))