def sumar_llista(llista):
    total = 0
    for num in llista:
        total += num
    return total

def multiplicar_llista(llista):
    if not llista:
        return 0  
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

#Programa Principal (Programa fet amb en Joan)
a = [1,3,5,7,10]
print("La suma dels elements de la llista {} val {}".format(a,sumar_llista(a)))
print("La multiplicacó dels elements de la llista {} val {}".format(a,multiplicar_llista(a)))