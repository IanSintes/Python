for i in range(1,1000):
    if (i%9==0 or i%7==0) and (i%5!=0 and i%8!=0):
        print(i)
print("Has inserit un nombre que no vui, adéu!")



"""
v1 = 2
while ((v1>=1 and v1<=1000) and (v1%2==0) and (v1%8==0)):
    v1 = int(input("Introdueix l'operador: "))
while ((v1>=5 and v1<=10) or (v1>=15 and v1<=20) or (v1>=25 and v1<=30)) and v1!=6 and v1!=16 and v1!=26:
def ordenar(x,y):
    #Prec: Donats dos nombres
    #Post: Els retorna mab ordre, primer el major i despres el menor
    if x>y:
        return x,y
    elif y>x:
        return y,x
    else:
        return x,y

v1 = int(input("Introdueix el primer operador: "))
v2 = int(input("Introdueix el segon operador: "))
v1, v2 = ordenar(v1,v2)
for e in range(v2, v1+1):
    print(e)

r = v1 == v2
print(r)
r = v1 != v2
print(r)
r = v1 > v2
print(r)
r = v1 < v2
print(r)
r = v1 >= v2
print(r)
r = v1 <= v2
print(r)




r = v1 + v2
print(r)
r = v1 - v2
print(r)
r = v1 * v2
print(r)
r = v1 // v2 #Divisio entera
print(r)
r = v1 / v2 # Divisio real
print(r)
r = v1 % v2
print(r)
r = v1 ** v2
print(r)
r = v1 + (v2**2 / v1 - (v1%v2))
print(r)
"""