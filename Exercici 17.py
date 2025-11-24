def longitud(a):
    return len(a)

# Exemples de prova
print("longitud([1, 2, 3, 4]) =", longitud([1, 2, 3, 4]))
print("longitud('Hola món') =", longitud('Hola món'))
print("longitud([]) =", longitud([]))
print("longitud('') =", longitud(''))
print("longitud([10, 20, 30]) =", longitud([10, 20, 30]))

#Codig fet amb en Joan
a=[1, 3, 4, "Pere", [3,4], "a", [1,[3,4], 5]]
print(longitud(a))
b=("Soc Ian Sintes. Que tal estas?")
print(longitud(b))
c=[]
print(longitud(c))