# Donat una llista, determinar quantes vegades es repeteixen els elements

a = (1,1,2,2,3,3,4,4,5,5,6,1,2,1,3,5) # Llista
b = set(a) # Conjunt/set
c = list() # Llista buida on guardarem elements i numero de repeticions
for e in b:
    c.append([e,a.count(e)])
print(c)


"""
a = (1, 2, 3, 1, 2, 3, 1, 4)
b = a.index(1,4)
print(b)
b = a.count(1)
print(b)
x,y,z = a
print("x={}, y={}, z={}".format(x, y, z))
"""