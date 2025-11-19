def gran_llista(llista):
    if not llista:
        return None
    major = llista[0]
    for num in llista[1:]:
        if num > major:
            major = num
    return major

# Exemples de prova
print(gran_llista([3, 4, 2, 3, 10]))
print(gran_llista([5, 7, 1, 9, 4]))
print(gran_llista([-3, -7, -1, -9]))
print(gran_llista([]))
