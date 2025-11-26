def mostrar_majors_que(tupla, x):
    for num in tupla:
        if num > x:
            print(num)

# Programa de prova
valors = []

print("Introdueix nombres enters (0 per acabar):")
while True:
    n = int(input())
    if n == 0:
        break
    valors.append(n)

tupla = tuple(valors)

print("Valors majors de 18:")
mostrar_majors_que(tupla, 18)
