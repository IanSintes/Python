def sumar_llista(llista):
    total = 0
    for num in llista:
        total += num
    return total

def multiplicar_llista(llista):
    if not llista:
        return 0  # Retorna 0 si la llista està buida
    total = 1
    for num in llista:
        total *= num
    return total

# Exemples de prova
print("sumar_llista([1, 2, 3, 4]) =", sumar_llista([1, 2, 3, 4]))
print("sumar_llista([5, 10, 2]) =", sumar_llista([5, 10, 2]))
print("multiplicar_llista([1, 2, 3, 4]) =", multiplicar_llista([1, 2, 3, 4]))
print("multiplicar_llista([5, 10, 2]) =", multiplicar_llista([5, 10, 2]))
print("multiplicar_llista([]) =", multiplicar_llista([]))