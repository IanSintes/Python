def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
# Programa principal
a = int(input("Introdueix un nombre per fer el factorial: "))
print(factorial(a))

"""
def sumaun(m):
    for i,e in enumerate(m):
        m[i]=e + 1

# Programa principal
l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)
sumaun(l)
print(l)


# Llegir 2 nombres
# Imprimir tots els nombres entre el menor i el major ambos inclosos
def ordenar(x,y):
    #Post: donat dos nombres
    #Prec: Retorna el menor i despres el major
    if x>y:
        return y,x
    elif y>x:
        return x,y
    else:
        return x,y
    
# Programa principal
v1 = int(input("Introdueix el primer nombre: "))
v2 = int(input("Introdueix el segon nombre: "))
v1, v2 = ordenar(v1, v2)
for e in range(v2, v1+1, 2):
    if e%2==1:
        print(e)

# Llegir 2 nombres
v1 = int(input("Introdueix el primer nombre: "))
v2 = int(input("Introdueix el segon nombre: "))
# Multiplicar-los i dividir-los per 2
r = (v1*v2) // 2
# Imprimir fins el 0
for i in range(r, -1, -1):
    print(i)

v1 = int(input("Introdueix el primer nombre: "))
v2 = int(input("Introdueix el segon nombre: "))
r = v1*v2
if (r>=25 and r<=35) or (r>=105 and r<= 125):
    print("A")
elif (r>=45 and r<=65) or (r>=145 and r<=165):
    print("B")
else:
    print("C")
"""