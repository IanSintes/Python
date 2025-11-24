#a = [1,"a","Capça",[2], 1, "a"]
a = [10,9,8,7,6,1,2,3,4]
#Pasar els elements de la llista a string
for i in range(len(a)):
    a[i]=str(a[i])
#Crear un unic string separat per guio
print("-".join(a))



"""
b = a.copy()
b[0]
print(a)
print(a[::-1]) #Retorna una llista invertida, pero no modifica l'original.
print(a)
print(a.reverse()) #No retorna res, pero modifica la llista original.
print(a)
a.sort()
print(a)
for i in range(len(a)):
    a[i]=str(a[i])
a.sort()
print(a)
c = "capça" in a 
print(c)
c = a.pop(2)
print(c)
a[0]= "Hola, som en Ramis"
del a[:]
a.append(10)
a.append("Cadena nova")
a.append([10,11,12])
a.extend((10, "Cadena nova", [10,11,12]))
print(a)
"""


"""
for e in a:
    print(e)
for i in range(len(a)):
    a[i]*=2 # --> a[i]= a[i]*2
    print("La posicó {} te el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("La posicó {} te el valor {}".format(i,e))
"""